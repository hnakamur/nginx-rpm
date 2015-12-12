FROM fedora:23
# NOTE: We use fedora:23 or later since I'd like to use the feature of
# uploading a SRPM file to copr introduced in python-copr-1.58.1.
# See https://bugzilla.redhat.com/show_bug.cgi?id=1045744

MAINTAINER Hiroaki Nakamura <hnakamur@gmail.com>

RUN dnf -y install python copr-cli mock rpm-build rpmdevtools patch sudo curl less scl-utils scl-utils-build \
 && useradd -G mock builder \
 && echo 'builder ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/builder

USER builder
RUN rpmdev-setuptree
WORKDIR /home/builder/rpmbuild

ADD SPECS/ ./SPECS/
ADD SOURCES/ ./SOURCES/
ADD scripts/ ./
RUN sudo chown -R builder:builder . \
 && chmod +x ./*.sh

CMD ["./build.sh", "copr"]
