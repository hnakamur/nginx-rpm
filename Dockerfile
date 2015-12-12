FROM centos:7
MAINTAINER Hiroaki Nakamura <hnakamur@gmail.com>

RUN yum -y install mock rpm-build rpmdevtools patch sudo curl less scl-utils scl-utils-build \
 && useradd -G mock builder \
 && echo 'builder ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/builder

USER builder
RUN rpmdev-setuptree
WORKDIR /home/builder/rpmbuild

ADD SPECS/ ./SPECS/
ADD SOURCES/ ./SOURCES/
ADD scripts/ ./
USER root
RUN chown -R builder:builder . \
 && chmod +x ./*.sh
USER builder

CMD ["./build.sh", "copr"]
