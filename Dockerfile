FROM centos:7
MAINTAINER Hiroaki Nakamura <hnakamur@gmail.com>

RUN yum -y install @"Development Tools" rpm-build rpmdevtools patch curl less vim-enhanced \
 && rpmdev-setuptree

WORKDIR /root/rpmbuild
ADD SPECS/ ./SPECS/
ADD SOURCES/ ./SOURCES/

RUN source_urls=`rpmspec -P ./SPECS/nginx.spec | awk '/^Source[0-9]*:\s*http/ {print $2}'` \
 && for source_url in $source_urls; do \
      source_file=${source_url##*/}; \
      (cd ./SOURCES && if [ ! -f ${source_file} ]; then curl -sLO ${source_url}; fi); \
    done

RUN yum install -y epel-release \
 && yum-builddep -y ./SPECS/nginx.spec \
 && rpmbuild -bb ./SPECS/nginx.spec \
 && yum install -y ./RPMS/x86_64/*.rpm
