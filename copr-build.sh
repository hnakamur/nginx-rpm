#!/bin/bash
set -e
copr_login=$1
copr_username=$2
copr_token=$3

project_name=nginx
spec_file=/root/rpmbuild/SPECS/nginx.spec

mkdir -p /root/.config
cat > /root/.config/copr <<EOF
[copr-cli]
login = ${copr_login}
username = ${copr_username}
token = ${copr_token}
copr_url = https://copr.fedoraproject.org
EOF

status=`curl -s -o /dev/null -w "%{http_code}" https://copr.fedoraproject.org/api/coprs/${copr_username}/${project_name}/detail/`
if [ $status = "404" ]; then
  copr-cli create --chroot epel-7-x86_64 --description \
'nginx: High performance web server.' \
--instructions \
"sudo curl -sL -o /etc/yum.repos.d/hnakamur-${project_name}.repo https://copr.fedoraproject.org/coprs/hnakamur/${project_name}/repo/epel-7/hnakamur-${project_name}-epel-7.repo
sudo yum install ${project_name}" \
${project_name}
fi
version=`awk '$1=="Version:" {print $2}' ${spec_file}`
release=`awk '$1=="Release:" {print $2}' ${spec_file}`
srpm_file=/root/rpmbuild/SRPMS/${project_name}-${version}-${release}.src.rpm
copr-cli build --nowait ${project_name} ${srpm_file}
