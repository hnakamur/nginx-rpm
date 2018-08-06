#!/bin/bash
set -ue

# Usage: download_github_repo -b branch user/repo
#     or download_github_repo -c commit user/repo
download_github_repo() {
  local branch_or_commit_opt=$1
  local branch_or_commit=$2
  local user_repo=$3

  local user=${user_repo%%/*}
  local repo=${user_repo##*/}

  if [ -d $repo ]; then
    rm -rf ${repo}
  fi

  local commit
  case "$branch_or_commit_opt" in
  -b)
    git clone --depth 1 -b ${branch_or_commit} https://github.com/${user}/${repo}.git > /dev/null 2>&1
    commit=$(cd ${repo} && git rev-parse HEAD)
    rm -rf ${repo}/.git
    ;;
  -c)
    mkdir ${repo}
    curl -sSL https://github.com/$user/$repo/archive/${commit}.tar.gz | tar zxf - --strip-component 1 -C ${repo}
    commit=${branch_or_commit}
    ;;
  esac

  tar cf - ${repo} | gzip -9 > SOURCES/${repo}.tar.gz
  rm -rf ${repo}
  echo "%define ${repo//-/_}_commit $commit"
}

download_github_repo -b master apcera/nginx-statsd
