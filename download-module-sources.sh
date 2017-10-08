#!/bin/bash
set -ue
download_github_repo() {
  local user=$1
  local repo=$2
  local commit=$3

  if [ ! -d $repo ]; then
    if [ $commit = master ]; then
      commit=$(curl -sS https://api.github.com/repos/$user/$repo/commits/master | jq -r .sha)
    fi
    mkdir ${repo}
    curl -sSL https://github.com/$user/$repo/archive/${commit}.tar.gz | tar zxf - --strip-component 1 -C ${repo}
    tar cf - ${repo} | gzip -9 > SOURCES/${repo}.tar.gz
    rm -rf ${repo}
    echo "%define ${repo//-/_}_commit $commit"
  fi
}


download_github_repo openresty echo-nginx-module master
download_github_repo openresty headers-more-nginx-module master
download_github_repo openresty lua-nginx-module master
download_github_repo openresty lua-upstream-nginx-module master
download_github_repo openresty memc-nginx-module master
download_github_repo openresty redis2-nginx-module master
download_github_repo openresty set-misc-nginx-module master
download_github_repo openresty srcache-nginx-module master
download_github_repo openresty lua-resty-core master

download_github_repo FRiCKLE ngx_cache_purge master
download_github_repo arut nginx-rtmp-module master
download_github_repo arut nginx-dav-ext-module master
download_github_repo bpaquet ngx_http_enhanced_memcached_module master
download_github_repo replay ngx_http_secure_download master
download_github_repo simpl ngx_devel_kit master
download_github_repo wandenberg nginx-sorted-querystring-module master
download_github_repo pandax381 ngx_http_pipelog_module master
