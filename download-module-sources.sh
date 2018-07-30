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


download_github_repo -b master openresty/echo-nginx-module
download_github_repo -b master openresty/headers-more-nginx-module
download_github_repo -b master openresty/lua-nginx-module
download_github_repo -b master openresty/lua-upstream-nginx-module
download_github_repo -b master openresty/memc-nginx-module
download_github_repo -b master openresty/redis2-nginx-module
download_github_repo -b master openresty/set-misc-nginx-module
download_github_repo -b master openresty/srcache-nginx-module
download_github_repo -b master openresty/lua-resty-core
download_github_repo -b master openresty/stream-lua-nginx-module
download_github_repo -b master openresty/lua-resty-string
download_github_repo -b master cloudflare/lua-resty-cookie
download_github_repo -b master pintsized/lua-resty-http

download_github_repo -b master FRiCKLE/ngx_cache_purge
download_github_repo -b master arut/nginx-rtmp-module
download_github_repo -b master arut/nginx-dav-ext-module
download_github_repo -b master bpaquet/ngx_http_enhanced_memcached_module
download_github_repo -b master replay/ngx_http_secure_download
download_github_repo -b master simplresty/ngx_devel_kit
download_github_repo -b master wandenberg/nginx-sorted-querystring-module
download_github_repo -b master pandax381/ngx_http_pipelog_module
download_github_repo -b master nginx-shib/nginx-http-shibboleth
download_github_repo -b master hnakamur/nginx-lua-saml-service-provider
download_github_repo -b master hnakamur/nginx-lua-session
download_github_repo -b master hamishforbes/lua-ffi-zlib
download_github_repo -b master Phrogz/SLAXML
