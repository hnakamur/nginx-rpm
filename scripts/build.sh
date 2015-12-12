#!/bin/bash -x
set -eu

# NOTE: Edit project_name and rpm_name.
project_name=nginx
rpm_name=nginx
arch=x86_64

spec_file=${rpm_name}.spec
mock_chroot=epel-7-${arch}

usage() {
  cat <<'EOF' 1>&2
Usage: build.sh subcommand

subcommand:
  srpm          build the srpm
  mock          build the rpm locally with mock
  copr          upload the srpm and build the rpm on copr
EOF
}

topdir=`rpm --eval '%{_topdir}'`
topdir_in_chroot=/builddir/build

download_source_files() {
  # NOTE: Edit commands here.
  cd ${topdir}/SOURCES
  nginx_tarball_file=nginx-${version}.tar.gz
  if [ ! -f ${nginx_tarball_file} ]; then
    curl -sLO http://nginx.org/download/${nginx_tarball_file}
  fi

  ngx_lua_tarball_file=lua-nginx-module-${ngx_lua_version}.tar.gz
  if [ ! -f ${ngx_lua_tarball_file} ]; then
    curl -sLO https://github.com/openresty/lua-nginx-module/archive/v${ngx_lua_version}.tar.gz#/${ngx_lua_tarball_file}
  fi

  nginx_upstream_check_module_tarball_file=nginx_upstream_check_module-master.tar.gz
  if [ ! -f ${nginx_upstream_check_module_tarball_file} ]; then
    curl -sLO https://github.com/yaoweibin/nginx_upstream_check_module/archive/master.tar.gz#/${nginx_upstream_check_module_tarball_file}
  fi

  ngx_http_consistent_hash_tarball_file=ngx_http_consistent_hash-master.tar.gz
  if [ ! -f ${ngx_http_consistent_hash_tarball_file} ]; then
    curl -sLO https://github.com/replay/ngx_http_consistent_hash/archive/master.tar.gz#/${ngx_http_consistent_hash_tarball_file}
  fi
}

build_srpm() {
  version=`rpmspec -P ${topdir}/SPECS/${spec_file} | awk '$1=="Version:" { print $2 }'`
  ngx_lua_version=`awk '/^%define ngx_lua_version/ { print $3 }' ${topdir}/SPECS/${spec_file}`
  download_source_files
  /usr/bin/mock -r ${mock_chroot} --init
  /usr/bin/mock -r ${mock_chroot} --no-clean --buildsrpm --spec "${topdir}/SPECS/${spec_file}" --sources "${topdir}/SOURCES/"
  release=`/usr/bin/mock -r ${mock_chroot} --chroot "rpmspec -P ${topdir_in_chroot}/SPECS/${spec_file}" | awk '$1=="Release:" { print $2 }'`
  rpm_version_release=${version}-${release}
  srpm_file=${rpm_name}-${rpm_version_release}.src.rpm
  mock_result_dir=/var/lib/mock/${mock_chroot}/result
  cp ${mock_result_dir}/${srpm_file} ${topdir}/SRPMS/
}

build_rpm_with_mock() {
  build_srpm
  /usr/bin/mock -r ${mock_chroot} --no-clean --rebuild ${topdir}/SRPMS/${srpm_file}

  mock_result_dir=/var/lib/mock/${mock_chroot}/result
  if [ -n "`find ${mock_result_dir} -maxdepth 1 -name \"${rpm_name}-*${rpm_version_release}.${arch}.rpm\" -print -quit`" ]; then
    mkdir -p ${topdir}/RPMS/${arch}
    cp ${mock_result_dir}/${rpm_name}-*${rpm_version_release}.${arch}.rpm ${topdir}/RPMS/${arch}/
  fi
  if [ -n "`find ${mock_result_dir} -maxdepth 1 -name \"${rpm_name}-*${rpm_version_release}.noarch.rpm\" -print -quit`" ]; then
    mkdir -p ${topdir}/RPMS/noarch
    cp ${mock_result_dir}/${rpm_name}-*${rpm_version_release}.noarch.rpm ${topdir}/RPMS/noarch/
  fi
}

build_rpm_on_copr() {
  build_srpm

  # Check the project is already created on copr.
  status=`curl -s -o /dev/null -w "%{http_code}" https://copr.fedoraproject.org/api/coprs/${COPR_USERNAME}/${project_name}/detail/`
  if [ $status = "404" ]; then
    # Create the project on copr.
    # We call copr APIs with curl to work around the InsecurePlatformWarning problem
    # since system python in CentOS 7 is old.
    # I read the source code of https://pypi.python.org/pypi/copr/1.62.1
    # since the API document at https://copr.fedoraproject.org/api/ is old.
    #
    # NOTE: Edit description here. You may or may not need to edit instructions.
    curl -s -X POST -u "${COPR_LOGIN}:${COPR_TOKEN}" \
      --data-urlencode "name=${project_name}" --data-urlencode "${mock_chroot}=y" \
      --data-urlencode "description=[nginx](http://nginx.org/) is a high performance web server. This rpm is built with consistent hash, upstream check and lua modules.

* [openresty/lua-nginx-module](https://github.com/openresty/lua-nginx-module)
* [yaoweibin/nginx_upstream_check_module](https://github.com/yaoweibin/nginx_upstream_check_module)
* [replay/ngx_http_consistent_hash](https://github.com/replay/ngx_http_consistent_hash)
" \
      --data-urlencode "instructions=\`\`\`
sudo curl -sL -o /etc/yum.repos.d/${COPR_USERNAME}-${project_name}.repo https://copr.fedoraproject.org/coprs/${COPR_USERNAME}/${project_name}/repo/epel-7/${COPR_USERNAME}-${project_name}-epel-7.repo
\`\`\`

\`\`\`
sudo yum install ${rpm_name}
\`\`\`" \
      https://copr.fedoraproject.org/api/coprs/${COPR_USERNAME}/new/
  fi
  # Add a new build on copr with uploading a srpm file.
  curl -s -X POST -u "${COPR_LOGIN}:${COPR_TOKEN}" \
    -F "${mock_chroot}=y" \
    -F "pkgs=@${topdir}/SRPMS/${srpm_file};type=application/x-rpm" \
    https://copr.fedoraproject.org/api/coprs/${COPR_USERNAME}/${project_name}/new_build_upload/
}

case "${1:-}" in
srpm)
  build_srpm
  ;;
mock)
  build_rpm_with_mock
  ;;
copr)
  build_rpm_on_copr
  ;;
*)
  usage
  ;;
esac
