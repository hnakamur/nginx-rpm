#!/bin/bash -x
set -eu

copr_project_name=nginx
rpm_name=nginx
arch=x86_64

luajit_repo_baseurl='https://copr-be.cloud.fedoraproject.org/results/hnakamur/luajit/epel-6-$basearch/'

copr_project_description="[nginx](http://nginx.org/) is a high performance web server.
This rpm includes the following modules as dynamic modules:

* [apcera/nginx-statsd](https://github.com/apcera/nginx-statsd)

Warning: Modules may be added or deleted without notice.
"

spec_file=${rpm_name}.spec
mock_chroots="epel-6-${arch}"

usage() {
  cat <<'EOF' 1>&2
Usage: build.sh subcommand

subcommand:
  srpm          build the srpm
  mock          build the rpm locally with mock
EOF
}

topdir=`rpm --eval '%{_topdir}'`

download_source_files() {
  source_urls=`rpmspec -P ${topdir}/SPECS/${spec_file} | awk '/^Source[0-9]*:\s*http/ {print $2}'`
  for source_url in $source_urls; do
    source_file=${source_url##*/}
    (cd ${topdir}/SOURCES && if [ ! -f ${source_file} ]; then curl -sLO ${source_url}; fi)
  done
}

build_srpm() {
  download_source_files
  rpmbuild -bs "${topdir}/SPECS/${spec_file}"
  version=`rpmspec -P ${topdir}/SPECS/${spec_file} | awk '$1=="Version:" { print $2 }'`
  release=`rpmspec -P ${topdir}/SPECS/${spec_file} | awk '$1=="Release:" { print $2 }'`
  rpm_version_release=${version}-${release}
  srpm_file=${rpm_name}-${rpm_version_release}.src.rpm
}

create_luajit_repo_file() {
  base_chroot=$1

  luajit_repo_file=luajit.repo
  if [ ! -f $luajit_repo_file ]; then
    # NOTE: Although https://copr.fedorainfracloud.org/coprs/hnakamur/luajit/repo/epel-6/hnakamur-luajit-epel-6.repo
    #       has the gpgkey in it, I don't use it since I don't know how to add it to /etc/mock/*.cfg
    cat > ${luajit_repo_file} <<EOF
[hnakamur-luajit]
name=Copr repo for luajit owned by hnakamur
baseurl=https://copr-be.cloud.fedoraproject.org/results/hnakamur/luajit/${base_chroot}/
enabled=1
gpgcheck=0
EOF
  fi
}

create_mock_chroot_cfg() {
  base_chroot=$1
  mock_chroot=$2

  create_luajit_repo_file $base_chroot

  # Insert ${scl_repo_file} before closing """ of config_opts['yum.conf']
  # See: http://unix.stackexchange.com/a/193513/135274
  #
  # NOTE: Support of adding repository was added to mock,
  #       so you can use it in the future.
  # See: https://github.com/rpm-software-management/ci-dnf-stack/issues/30
  (cd ${topdir} \
    && echo | sed -e '$d;N;P;/\n"""$/i\
' -e '/\n"""$/r '${luajit_repo_file} -e '/\n"""$/a\
' -e D /etc/mock/${base_chroot}.cfg - | sudo sh -c "cat > /etc/mock/${mock_chroot}.cfg")
}

build_rpm_with_mock() {
  build_srpm
  for mock_chroot in $mock_chroots; do
    base_chroot=$mock_chroot
    mock_chroot=${base_chroot}-with-luajit
    create_mock_chroot_cfg $base_chroot $mock_chroot
    /usr/bin/mock -r ${mock_chroot} --rebuild ${topdir}/SRPMS/${srpm_file}

    mock_result_dir=/var/lib/mock/${base_chroot}/result
    if [ -n "`find ${mock_result_dir} -maxdepth 1 -name \"${rpm_name}-*${version}-*.${arch}.rpm\" -print -quit`" ]; then
      mkdir -p ${topdir}/RPMS/${arch}
      cp ${mock_result_dir}/${rpm_name}-*${version}-*.${arch}.rpm ${topdir}/RPMS/${arch}/
    fi
    if [ -n "`find ${mock_result_dir} -maxdepth 1 -name \"${rpm_name}-*${version}-*.noarch.rpm\" -print -quit`" ]; then
      mkdir -p ${topdir}/RPMS/noarch
      cp ${mock_result_dir}/${rpm_name}-*${version}-*.noarch.rpm ${topdir}/RPMS/noarch/
    fi
  done
}



case "${1:-}" in
srpm)
  build_srpm
  ;;
mock)
  build_rpm_with_mock
  ;;
*)
  usage
  ;;
esac
