FROM centos:7
MAINTAINER Hiroaki Nakamura <hnakamur@gmail.com>

ENV NGINX_VERSION 1.9.7
ENV NGX_LUA_VERSION 0.9.19

RUN yum -y install epel-release \
 && yum -y install rpmdevtools rpm-build patch python-pip \
 && pip install copr-cli \
 && rpmdev-setuptree \
 && cd /root/rpmbuild/SRPMS \
 && curl -sLO http://nginx.org/packages/mainline/centos/7/SRPMS/nginx-${NGINX_VERSION}-1.el7.ngx.src.rpm \
 && rpm -i nginx-${NGINX_VERSION}-1.el7.ngx.src.rpm \
 && cd /root/rpmbuild/SOURCES \
 && curl -sLO https://github.com/openresty/lua-nginx-module/archive/v${NGX_LUA_VERSION}.tar.gz#/lua-nginx-module-${NGX_LUA_VERSION}.tar.gz \
 && curl -sLO https://github.com/yaoweibin/nginx_upstream_check_module/archive/master.tar.gz#/nginx_upstream_check_module-master.tar.gz \
 && curl -sLO https://github.com/replay/ngx_http_consistent_hash/archive/master.tar.gz#/ngx_http_consistent_hash-master.tar.gz

ADD nginx.spec.patch /root/rpmbuild/SPECS/

RUN cd /root/rpmbuild/SPECS \
 && patch -p0 < nginx.spec.patch \
 && rpmbuild -bs nginx.spec

ADD copr-build.sh /root/
ENTRYPOINT ["/bin/bash", "/root/copr-build.sh"]
