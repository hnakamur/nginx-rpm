#!/bin/sh
set -eu
imagename=nginxrpm

usage() {
  cat <<'EOF' 1>&2
Usage: docker_wrapper.sh subcommand args...

subcommands:
  build            build the docker image with tag "$imagename"
  run              run the docker image of tag "$imagename"
  bash             run /bin/bash in the docker image of tag "$imagename"
EOF
}

case "${1:-}" in
build)
  docker build -t $imagename .
  ;;
run)
  # NOTE: We need SYS_ADMIN capability to build rpm with mock
  docker run --cap-add=SYS_ADMIN -e "COPR_LOGIN=$COPR_LOGIN" -e "COPR_USERNAME=$COPR_USERNAME" -e "COPR_TOKEN=$COPR_TOKEN" -it $imagename
  ;;
bash)
  # NOTE: We need SYS_ADMIN capability to build rpm with mock
  docker run --cap-add=SYS_ADMIN -e "COPR_LOGIN=$COPR_LOGIN" -e "COPR_USERNAME=$COPR_USERNAME" -e "COPR_TOKEN=$COPR_TOKEN" -it $imagename /bin/bash
  ;;
*)
  usage
  ;;
esac
