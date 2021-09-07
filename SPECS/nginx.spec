#
%define nginx_home %{_localstatedir}/cache/nginx
%define nginx_user nginx
%define nginx_group nginx
%define nginx_loggroup adm

%define ngx_openssl_version 1.1.1l

%define echo_nginx_module_commit 6f8a4abea9dcf366b7cb43f6ce7f1e56d0d409e5
%define headers_more_nginx_module_commit f85af9649b858e21b400a2150a4c7b8ebd36e921
%define lua_nginx_module_commit 3820d0e118f834916fff66c66f2a29196832dcf8
%define lua_upstream_nginx_module_commit 8aa93ead98ba2060d4efd594ae33a35d153589bf
%define memc_nginx_module_commit 5ae511de2285e74d4f4129f4a00890c6bef1928e
%define redis2_nginx_module_commit 154bc51b9fc118267f9c3d30f52779320956a807
%define set_misc_nginx_module_commit 31c4ad67bb9e392a734e4e58ea8048e24012311f
%define srcache_nginx_module_commit b61755d098568cd78febf69e6d7499b1d0b7250a
%define stream_lua_nginx_module_commit ef1188d0f4a96d77e02efeb96b4cf2c5e48f012b
%define lua_resty_balancer_commit 56fd8ad03d5718f507a5129edc43a25948364b9f
%define lua_resty_core_commit efce3705c01a348eb6551c57cd56c3f12abba096
%define lua_resty_dns_commit 869d2fbb009b6ada93a5a10cb93acd1cc12bd53f
%define lua_resty_lock_commit ad94745a4731ee6ddbffbc3b602df25ca7c6f7ba
%define lua_resty_lrucache_commit dacd022b4b8e3a73ed25886f2f9db043075ddb31
%define lua_resty_limit_traffic_commit 121a320a4e1167f611a9634a410a49e8c41c2c8e
%define lua_resty_memcached_commit 1517409a3f23116bb63f080629a6a515cf332d87
%define lua_resty_memcached_shdict_commit 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
%define lua_resty_mysql_commit e40b9a11df87bd0bb2bab3116de9f94a96549fd4
%define lua_resty_redis_commit 91585affcd9a8da65cb664a5b1e926dde428095a
%define lua_resty_shdict_simple_commit 4d27246b16f86de49e6da8b8a6136cddfe7550b4
%define lua_resty_shell_commit 30ea64310c2c6aabc86774ac4f544a37dd458352
%define lua_resty_signal_commit 7b247bd3085007b4e9fa4c09bbb5f591aa19e0a1
%define lua_resty_string_commit b192878f6ed31b0af237935bbc5a8110a3c2256c
%define lua_resty_upload_commit 7baca92c7e741979ae5857989bbf6cc0402d6126
%define lua_resty_upstream_healthcheck_commit 27bf62336219cb4eb804f82e1263a00dff3be398
%define lua_resty_websocket_commit b341b7da72a7139cbe27b51c3b50511606e56636
%define lua_resty_cookie_commit 303e32e512defced053a6484bc0745cf9dc0d39e
%define lua_resty_openidc_commit 59d01573d7d8eeed4cd60666af1cdc90ff8be80b
%define lua_resty_session_commit 2cd1f8484fdd429505ac33abf7a44adda1f367bf
%define lua_resty_jwt_commit b8b1f6e00be74565111e0cbbc40bc7d26367a646
%define lua_resty_hmac_commit 193232acecb8bc15ee414651a53b11a1624e6a16
%define lua_resty_http_commit 0ce55d6d15da140ecc5966fa848204c6fd9074e8
%define ngx_cache_purge_commit 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
%define nginx_rtmp_module_commit 23e1873aa62acb58b7881eed2a501f5bf35b82e9
%define nginx_dav_ext_module_commit f5e30888a256136d9c550bf1ada77d6ea78a48af
%define ngx_http_enhanced_memcached_module_commit b58a4500db3c4ee274be54a18abc767219dcfd36
%define ngx_http_secure_download_commit f379a1acf2a76f63431a12fa483d9e22e718400b
%define ngx_devel_kit_commit a22dade76c838e5f377d58d007f65d35b5ce1df3
%define nginx_sorted_querystring_module_commit e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
%define ngx_http_pipelog_module_commit f59558ebf71c810ceff15d475deb98f15a0a19c9
%define nginx_http_shibboleth_commit 605f1ebbfd3e9c7d1328b885d6dd6edcb663c937
%define nginx_lua_saml_service_provider_commit ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
%define nginx_lua_session_commit 9c5053a7c9d2e8748f1153193d598dcea16417f4
%define lua_ffi_zlib_commit 1fb69ca505444097c82d2b72e87904f3ed923ae9
%define SLAXML_commit 108970cbcb4370365e79c619b0f06099c9ec9754
%define ngx_http_geoip2_module_commit a26c6beed77e81553686852dceb6c7fdacc5970d
%define ngx_upstream_jdomain_commit a5a8e07f76cbe82b0792f8e3091e011c0c12f230
%define lua_resty_woothee_commit 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
%define lua_resty_jump_consistent_hash_commit a01d2683bfe34cc4edaab7ecac7906d51dfbd125

%define luajit_inc /usr/include/luajit-2.1
%define luajit_lib /usr/lib64

# distribution specific definitions
%define use_systemd (0%{?fedora} && 0%{?fedora} >= 18) || (0%{?rhel} && 0%{?rhel} >= 7) || (0%{?suse_version} == 1315)

%if 0%{?rhel}  == 5
Group: System Environment/Daemons
Requires(pre): shadow-utils
Requires: initscripts >= 8.36
Requires(post): chkconfig
%endif

%if 0%{?rhel}  == 6
Group: System Environment/Daemons
Requires(pre): shadow-utils
Requires: initscripts >= 8.36
Requires(post): chkconfig
%define with_http2 1
%endif

%if 0%{?rhel}  == 7
Group: System Environment/Daemons
Requires(pre): shadow-utils
Requires: systemd
BuildRequires: systemd
Epoch: 1
%define tcp_fast_open 1
%define with_http2 1
%endif

%if 0%{?suse_version} == 1315
Group: Productivity/Networking/Web/Servers
BuildRequires: systemd
Requires(pre): shadow
Requires: systemd
%define with_http2 1
%define nginx_loggroup trusted
%endif

# end of distribution specific definitions

Summary: High performance web server
Name: nginx
Version: 1.21.3
Release: 1%{?dist}.ngx
Vendor: nginx inc.
URL: http://nginx.org/

Source0: http://nginx.org/download/%{name}-%{version}.tar.gz
Source1: logrotate
Source2: nginx.init.in
Source3: nginx.sysconf
Source4: nginx.conf
Source5: nginx.vh.default.conf
Source7: nginx-debug.sysconf
Source8: nginx.service
Source9: nginx.upgrade.sh
Source10: nginx.suse.logrotate
Source11: nginx-debug.service
Source12: COPYRIGHT

Source100: https://github.com/openresty/lua-nginx-module/archive/%{lua_nginx_module_commit}.tar.gz#/lua-nginx-module.tar.gz
Source101: https://github.com/openresty/headers-more-nginx-module/archive/%{headers_more_nginx_module_commit}.tar.gz#/headers-more-nginx-module.tar.gz
Source102: https://github.com/openresty/stream-lua-nginx-module/archive/%{stream_lua_nginx_module_commit}.tar.gz#/stream-lua-nginx-module.tar.gz
Source103: https://github.com/nginx-shib/nginx-http-shibboleth/archive/%{nginx_http_shibboleth_commit}.tar.gz#/nginx-http-shibboleth.tar.gz
Source104: https://github.com/wandenberg/nginx-sorted-querystring-module/archive/%{nginx_sorted_querystring_module_commit}.tar.gz#/nginx-sorted-querystring-module.tar.gz
Source105: https://github.com/arut/nginx-rtmp-module/archive/%{nginx_rtmp_module_commit}.tar.gz#/nginx-rtmp-module.tar.gz
Source106: https://github.com/FRiCKLE/ngx_cache_purge/archive/%{ngx_cache_purge_commit}.tar.gz#/ngx_cache_purge.tar.gz
Source107: https://github.com/replay/ngx_http_secure_download/archive/%{ngx_http_secure_download_commit}.tar.gz#/ngx_http_secure_download.tar.gz
Source108: https://github.com/cloudflare/lua-resty-cookie/archive/%{lua_resty_cookie_commit}.tar.gz#/lua-resty-cookie.tar.gz
Source109: https://github.com/openresty/srcache-nginx-module/archive/%{srcache_nginx_module_commit}.tar.gz#/srcache-nginx-module.tar.gz
Source110: https://github.com/openresty/redis2-nginx-module/archive/%{redis2_nginx_module_commit}.tar.gz#/redis2-nginx-module.tar.gz
Source111: https://github.com/openresty/memc-nginx-module/archive/%{memc_nginx_module_commit}.tar.gz#/memc-nginx-module.tar.gz
Source112: https://github.com/openresty/lua-upstream-nginx-module/archive/%{lua_upstream_nginx_module_commit}.tar.gz#/lua-upstream-nginx-module.tar.gz
Source113: https://github.com/openresty/echo-nginx-module/archive/%{echo_nginx_module_commit}.tar.gz#/echo-nginx-module.tar.gz
Source114: https://github.com/bpaquet/ngx_http_enhanced_memcached_module/archive/%{ngx_http_enhanced_memcached_module_commit}.tar.gz#/ngx_http_enhanced_memcached_module.tar.gz
Source115: https://github.com/arut/nginx-dav-ext-module/archive/%{nginx_dav_ext_module_commit}.tar.gz#/nginx-dav-ext-module.tar.gz
Source116: https://github.com/simplresty/ngx_devel_kit/archive/%{ngx_devel_kit_commit}.tar.gz#/ngx_devel_kit.tar.gz
Source117: https://github.com/openresty/set-misc-nginx-module/archive/%{set_misc_nginx_module_commit}.tar.gz#/set-misc-nginx-module.tar.gz
Source118: https://github.com/pandax381/ngx_http_pipelog_module/archive/%{ngx_http_pipelog_module_commit}.tar.gz#/ngx_http_pipelog_module.tar.gz
Source119: https://github.com/openresty/lua-resty-core/archive/%{lua_nginx_module_commit}.tar.gz#/lua-resty-core.tar.gz

Source120: https://openssl.org/source/openssl-%{ngx_openssl_version}.tar.gz

Source121: https://github.com/pintsized/lua-resty-http/archive/%{lua_resty_http_commit}.tar.gz#/lua-resty-http.tar.gz
Source122: https://github.com/openresty/lua-resty-string/archive/%{lua_resty_string_commit}.tar.gz#/lua-resty-string.tar.gz
Source123: https://github.com/hnakamur/nginx-lua-saml-service-provider/archive/%{nginx_lua_saml_service_provider_commit}.tar.gz#/nginx-lua-saml-service-provider.tar.gz
Source124: https://github.com/hnakamur/nginx-lua-session/archive/%{nginx_lua_session_commit}.tar.gz#/nginx-lua-session.tar.gz
Source125: https://github.com/hamishforbes/lua-ffi-zlib/archive/%{lua_ffi_zlib_commit}.tar.gz#/lua-ffi-zlib.tar.gz
Source126: https://github.com/Phrogz/SLAXML/archive/%{SLAXML_commit}.tar.gz#/SLAXML.tar.gz
Source127: https://github.com/openresty/lua-resty-lrucache/archive/%{lua_resty_lrucache_commit}.tar.gz#/lua-resty-lrucache.tar.gz
Source128: https://github.com/zmartzone/lua-resty-openidc/archive/%{lua_resty_openidc_commit}.tar.gz#/lua-resty-openidc.tar.gz
Source129: https://github.com/bungle/lua-resty-session/archive/%{lua_resty_session_commit}.tar.gz#/lua-resty-session.tar.gz
Source130: https://github.com/cdbattags/lua-resty-jwt/archive/%{lua_resty_jwt_commit}.tar.gz#/lua-resty-jwt.tar.gz
Source131: https://github.com/jkeys089/lua-resty-hmac/archive/%{lua_resty_hmac_commit}.tar.gz#/lua-resty-hmac.tar.gz
Source132: https://github.com/openresty/lua-resty-balancer/archive/%{lua_resty_balancer_commit}.tar.gz#/lua-resty-balancer.tar.gz
Source133: https://github.com/openresty/lua-resty-dns/archive/%{lua_resty_dns_commit}.tar.gz#/lua-resty-dns.tar.gz
Source134: https://github.com/openresty/lua-resty-lock/archive/%{lua_resty_lock_commit}.tar.gz#/lua-resty-lock.tar.gz
Source135: https://github.com/openresty/lua-resty-limit-traffic/archive/%{lua_resty_limit-traffic_commit}.tar.gz#/lua-resty-limit-traffic.tar.gz
Source136: https://github.com/openresty/lua-resty-memcached/archive/%{lua_resty_memcached_commit}.tar.gz#/lua-resty-memcached.tar.gz
Source137: https://github.com/openresty/lua-resty-memcached-shdict/archive/%{lua_resty_memcached-shdict_commit}.tar.gz#/lua-resty-memcached-shdict.tar.gz
Source138: https://github.com/openresty/lua-resty-mysql/archive/%{lua_resty_mysql_commit}.tar.gz#/lua-resty-mysql.tar.gz
Source139: https://github.com/openresty/lua-resty-redis/archive/%{lua_resty_redis_commit}.tar.gz#/lua-resty-redis.tar.gz
Source140: https://github.com/openresty/lua-resty-shdict-simple/archive/%{lua_resty_shdict-simple_commit}.tar.gz#/lua-resty-shdict-simple.tar.gz
Source141: https://github.com/openresty/lua-resty-shell/archive/%{lua_resty_shell_commit}.tar.gz#/lua-resty-shell.tar.gz
Source142: https://github.com/openresty/lua-resty-signal/archive/%{lua_resty_signal_commit}.tar.gz#/lua-resty-signal.tar.gz
Source143: https://github.com/openresty/lua-resty-upload/archive/%{lua_resty_upload_commit}.tar.gz#/lua-resty-upload.tar.gz
Source144: https://github.com/openresty/lua-resty-upstream-healthcheck/archive/%{lua_resty_upstream-healthcheck_commit}.tar.gz#/lua-resty-upstream-healthcheck.tar.gz
Source145: https://github.com/openresty/lua-resty-websocket/archive/%{lua_resty_websocket_commit}.tar.gz#/lua-resty-websocket.tar.gz
Source146: https://github.com/leev/ngx_http_geoip2_module/archive/%{ngx_http_geoip2_module_commit}.tar.gz#/ngx_http_geoip2_module.tar.gz
Source147: https://github.com/e98cuenc/ngx_upstream_jdomain/archive/%{ngx_upstream_jdomain_commit}.tar.gz#/ngx_upstream_jdomain.tar.gz
Source148: https://github.com/woothee/lua-resty-woothee/archive/%{lua_resty_woothee_commit}.tar.gz#/lua-resty-woothee.tar.gz
Source149: https://github.com/ruoshan/lua-resty-jump-consistent-hash/archive/%{lua_resty_jump_consistent_hash}.tar.gz#/lua-resty-jump-consistent-hash.tar.gz

Patch14: ngx_http_secure_download-dynamic_module.patch
Patch15: ngx_cache_purge-dynamic_module.patch
Patch16: ngx_cache_purge-fix_compatibility_with_nginx_1.11.6.patch
Patch17: ngx_cache_purge-feat_purge_all.patch
Patch18: ngx_cache_purge-feat_purge_partial_keys.patch
Patch19: ngx_cache_purge-select_response_type.patch
Patch20: nginx-1.11.2-ssl_cert_cb_yield.patch
Patch21: ngx_upstream_jdomain-dynamic_module.patch
Patch23: nginx-1.19.4-cache_manager.patch

License: 2-clause BSD-like license

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel
BuildRequires: pcre-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: gd-devel
BuildRequires: GeoIP-devel
BuildRequires: luajit-devel
BuildRequires: mhash-devel
BuildRequires: expat-devel
BuildRequires: libmaxminddb-devel

Provides: webserver

%description
nginx [engine x] is an HTTP and reverse proxy server, as well as
a mail proxy server.

%if 0%{?suse_version} == 1315
%debug_package
%endif

%prep
%setup -q -a 100 -a 101 -a 102 -a 103 -a 104 -a 105 -a 106 -a 107 -a 108 -a 109 -a 110 -a 111 -a 112 -a 113 -a 114 -a 115 -a 116 -a 117 -a 118 -a 119 -a 120 -a 121 -a 122 -a 123 -a 124 -a 125 -a 126 -a 127 -a 128 -a 129 -a 130 -a 131 -a 132 -a 133 -a 134 -a 135 -a 136 -a 137 -a 138 -a 139 -a 140 -a 141 -a 142 -a 143 -a 144 -a 145 -a 146 -a 147 -a 148 -a 149
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch23 -p1
cp %{SOURCE2} .
sed -e 's|%%DEFAULTSTART%%|2 3 4 5|g' -e 's|%%DEFAULTSTOP%%|0 1 6|g' \
    -e 's|%%PROVIDES%%|nginx|g' < %{SOURCE2} > nginx.init
sed -e 's|%%DEFAULTSTART%%||g' -e 's|%%DEFAULTSTOP%%|0 1 2 3 4 5 6|g' \
    -e 's|%%PROVIDES%%|nginx-debug|g' < %{SOURCE2} > nginx-debug.init

%build
LUAJIT_INC=%{luajit_inc} LUAJIT_LIB=%{luajit_lib} \
./configure \
        --prefix=%{_sysconfdir}/nginx \
        --sbin-path=%{_sbindir}/nginx \
        --modules-path=%{_libdir}/nginx/modules-debug \
        --conf-path=%{_sysconfdir}/nginx/nginx.conf \
        --error-log-path=%{_localstatedir}/log/nginx/error.log \
        --http-log-path=%{_localstatedir}/log/nginx/access.log \
        --pid-path=%{_localstatedir}/run/nginx.pid \
        --lock-path=%{_localstatedir}/run/nginx.lock \
        --http-client-body-temp-path=%{_localstatedir}/cache/nginx/client_temp \
        --http-proxy-temp-path=%{_localstatedir}/cache/nginx/proxy_temp \
        --http-fastcgi-temp-path=%{_localstatedir}/cache/nginx/fastcgi_temp \
        --http-uwsgi-temp-path=%{_localstatedir}/cache/nginx/uwsgi_temp \
        --http-scgi-temp-path=%{_localstatedir}/cache/nginx/scgi_temp \
        --user=%{nginx_user} \
        --group=%{nginx_group} \
        --with-http_ssl_module \
        --with-openssl=./openssl-%{ngx_openssl_version} \
        --with-http_realip_module \
        --with-http_addition_module \
        --with-http_sub_module \
        --with-http_dav_module \
        --with-http_flv_module \
        --with-http_mp4_module \
        --with-http_gunzip_module \
        --with-http_gzip_static_module \
        --with-http_random_index_module \
        --with-http_secure_link_module \
        --with-http_stub_status_module \
        --with-http_auth_request_module \
        --with-http_xslt_module=dynamic \
        --with-http_image_filter_module=dynamic \
        --with-http_geoip_module=dynamic \
        --with-threads \
        --with-stream \
        --with-stream_ssl_module \
        --with-http_slice_module \
        --with-mail=dynamic \
        --with-mail_ssl_module \
        --with-file-aio \
        --add-dynamic-module=./lua-nginx-module \
        --add-dynamic-module=./stream-lua-nginx-module \
        --add-dynamic-module=./headers-more-nginx-module \
        --add-dynamic-module=./nginx-sorted-querystring-module \
        --add-dynamic-module=./nginx-rtmp-module \
        --add-dynamic-module=./ngx_cache_purge \
        --add-dynamic-module=./ngx_http_secure_download \
        --add-dynamic-module=./redis2-nginx-module \
        --add-dynamic-module=./srcache-nginx-module \
        --add-dynamic-module=./memc-nginx-module \
        --add-dynamic-module=./lua-upstream-nginx-module \
        --add-dynamic-module=./echo-nginx-module \
        --add-dynamic-module=./ngx_http_enhanced_memcached_module \
        --add-dynamic-module=./nginx-dav-ext-module \
        --add-module=./ngx_devel_kit \
        --add-dynamic-module=./set-misc-nginx-module \
        --add-dynamic-module=./ngx_http_pipelog_module \
        --add-dynamic-module=./nginx-http-shibboleth \
        --add-dynamic-module=./ngx_http_geoip2_module \
        --add-dynamic-module=./ngx_upstream_jdomain \
        --with-debug \
        %{?with_http2:--with-http_v2_module} \
        --with-cc-opt="%{optflags} $(pcre-config --cflags)%{?tcp_fast_open: -DTCP_FASTOPEN=23} -Wno-uninitialized -Wno-unused-variable" \
        $*
make %{?_smp_mflags}
%{__mv} %{_builddir}/%{name}-%{version}/objs/nginx \
        %{_builddir}/%{name}-%{version}/objs/nginx-debug
%{__mkdir} %{_builddir}/%{name}-%{version}/objs-debug
%{__mv} %{_builddir}/%{name}-%{version}/objs/*.so \
        %{_builddir}/%{name}-%{version}/objs-debug
LUAJIT_INC=%{luajit_inc} LUAJIT_LIB=%{luajit_lib} \
./configure \
        --prefix=%{_sysconfdir}/nginx \
        --sbin-path=%{_sbindir}/nginx \
        --modules-path=%{_libdir}/nginx/modules \
        --conf-path=%{_sysconfdir}/nginx/nginx.conf \
        --error-log-path=%{_localstatedir}/log/nginx/error.log \
        --http-log-path=%{_localstatedir}/log/nginx/access.log \
        --pid-path=%{_localstatedir}/run/nginx.pid \
        --lock-path=%{_localstatedir}/run/nginx.lock \
        --http-client-body-temp-path=%{_localstatedir}/cache/nginx/client_temp \
        --http-proxy-temp-path=%{_localstatedir}/cache/nginx/proxy_temp \
        --http-fastcgi-temp-path=%{_localstatedir}/cache/nginx/fastcgi_temp \
        --http-uwsgi-temp-path=%{_localstatedir}/cache/nginx/uwsgi_temp \
        --http-scgi-temp-path=%{_localstatedir}/cache/nginx/scgi_temp \
        --user=%{nginx_user} \
        --group=%{nginx_group} \
        --with-http_ssl_module \
        --with-openssl=./openssl-%{ngx_openssl_version} \
        --with-http_realip_module \
        --with-http_addition_module \
        --with-http_sub_module \
        --with-http_dav_module \
        --with-http_flv_module \
        --with-http_mp4_module \
        --with-http_gunzip_module \
        --with-http_gzip_static_module \
        --with-http_random_index_module \
        --with-http_secure_link_module \
        --with-http_stub_status_module \
        --with-http_auth_request_module \
        --with-http_xslt_module=dynamic \
        --with-http_image_filter_module=dynamic \
        --with-http_geoip_module=dynamic \
        --with-threads \
        --with-stream \
        --with-stream_ssl_module \
        --with-http_slice_module \
        --with-mail=dynamic \
        --with-mail_ssl_module \
        --with-file-aio \
        --add-dynamic-module=./lua-nginx-module \
        --add-dynamic-module=./stream-lua-nginx-module \
        --add-dynamic-module=./headers-more-nginx-module \
        --add-dynamic-module=./nginx-sorted-querystring-module \
        --add-dynamic-module=./nginx-rtmp-module \
        --add-dynamic-module=./ngx_cache_purge \
        --add-dynamic-module=./ngx_http_secure_download \
        --add-dynamic-module=./redis2-nginx-module \
        --add-dynamic-module=./srcache-nginx-module \
        --add-dynamic-module=./memc-nginx-module \
        --add-dynamic-module=./lua-upstream-nginx-module \
        --add-dynamic-module=./echo-nginx-module \
        --add-dynamic-module=./ngx_http_enhanced_memcached_module \
        --add-dynamic-module=./nginx-dav-ext-module \
        --add-module=./ngx_devel_kit \
        --add-dynamic-module=./set-misc-nginx-module \
        --add-dynamic-module=./ngx_http_pipelog_module \
        --add-dynamic-module=./nginx-http-shibboleth \
        --add-dynamic-module=./ngx_http_geoip2_module \
        --add-dynamic-module=./ngx_upstream_jdomain \
        %{?with_http2:--with-http_v2_module} \
        --with-cc-opt="%{optflags} $(pcre-config --cflags) %{?tcp_fast_open: -DTCP_FASTOPEN=23} -Wno-uninitialized -Wno-unused-variable" \
        $*
make %{?_smp_mflags}
(cd lua-resty-jump-consistent-hash \
 && make libjchash.so)

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%{__mkdir} -p $RPM_BUILD_ROOT%{_datadir}/nginx
%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/nginx/html $RPM_BUILD_ROOT%{_datadir}/nginx/

%{__rm} -f $RPM_BUILD_ROOT%{_sysconfdir}/nginx/*.default
%{__rm} -f $RPM_BUILD_ROOT%{_sysconfdir}/nginx/fastcgi.conf

%{__mkdir} -p $RPM_BUILD_ROOT%{_localstatedir}/log/nginx
%{__mkdir} -p $RPM_BUILD_ROOT%{_localstatedir}/run/nginx
%{__mkdir} -p $RPM_BUILD_ROOT%{_localstatedir}/cache/nginx

%{__mkdir} -p $RPM_BUILD_ROOT%{_libdir}/nginx/modules
cd $RPM_BUILD_ROOT%{_sysconfdir}/nginx && \
    %{__ln_s} ../..%{_libdir}/nginx/modules modules && cd -
%{__mkdir} -p $RPM_BUILD_ROOT%{_libdir}/nginx/modules-debug
cd $RPM_BUILD_ROOT%{_sysconfdir}/nginx && \
    %{__ln_s} ../..%{_libdir}/nginx/modules-debug modules-debug && cd -

%{__mkdir} -p $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-core/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-cookie/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-http/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-string/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-lrucache/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-openidc/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-session/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-jwt/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-hmac/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-balancer/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-dns/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-lock/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-limit-traffic/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-memcached/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-memcached-shdict/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-mysql/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-redis/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-shdict-simple/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-shell/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-signal/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-upload/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-upstream-healthcheck/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-websocket/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/nginx-lua-saml-service-provider/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/nginx-lua-session/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-ffi-zlib/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/SLAXML/*.lua $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-woothee/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-jump-consistent-hash/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua

%{__mkdir} -p $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
%{__install} -m 644 -p %{SOURCE12} \
    $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/

%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/nginx/conf.d
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/nginx/nginx.conf
%{__install} -m 644 -p %{SOURCE4} \
    $RPM_BUILD_ROOT%{_sysconfdir}/nginx/nginx.conf
%{__install} -m 644 -p %{SOURCE5} \
    $RPM_BUILD_ROOT%{_sysconfdir}/nginx/conf.d/default.conf

%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
%{__install} -m 644 -p %{SOURCE3} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/nginx
%{__install} -m 644 -p %{SOURCE7} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/nginx-debug

%if %{use_systemd}
# install systemd-specific files
%{__mkdir} -p $RPM_BUILD_ROOT%{_unitdir}
%{__install} -m644 %SOURCE8 \
    $RPM_BUILD_ROOT%{_unitdir}/nginx.service
%{__install} -m644 %SOURCE11 \
    $RPM_BUILD_ROOT%{_unitdir}/nginx-debug.service
%{__mkdir} -p $RPM_BUILD_ROOT%{_libexecdir}/initscripts/legacy-actions/nginx
%{__install} -m755 %SOURCE9 \
    $RPM_BUILD_ROOT%{_libexecdir}/initscripts/legacy-actions/nginx/upgrade
%else
# install SYSV init stuff
%{__mkdir} -p $RPM_BUILD_ROOT%{_initrddir}
%{__install} -m755 nginx.init $RPM_BUILD_ROOT%{_initrddir}/nginx
%{__install} -m755 nginx-debug.init $RPM_BUILD_ROOT%{_initrddir}/nginx-debug
%endif

# install log rotation stuff
%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
%if 0%{?suse_version}
%{__install} -m 644 -p %{SOURCE10} \
    $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/nginx
%else
%{__install} -m 644 -p %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/nginx
%endif

%{__install} -m755 %{_builddir}/%{name}-%{version}/objs/nginx-debug \
    $RPM_BUILD_ROOT%{_sbindir}/nginx-debug
%{__install} -m755 %{_builddir}/%{name}-%{version}/objs-debug/*.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules-debug/

%{__install} -m644 \
    %{_builddir}/%{name}-%{version}/nginx-http-shibboleth/includes/shib_clear_headers \
    %{_builddir}/%{name}-%{version}/nginx-http-shibboleth/includes/shib_fastcgi_params \
    $RPM_BUILD_ROOT%{_sysconfdir}/nginx/

%{__install} -m755 -d $RPM_BUILD_ROOT%{_libdir}/lua/5.1
%{__install} -m644 \
    %{_builddir}/%{name}-%{version}/lua-resty-jump-consistent-hash/libjchash.so \
    $RPM_BUILD_ROOT%{_libdir}/lua/5.1/

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{_sbindir}/nginx
%{_sbindir}/nginx-debug

%dir %{_sysconfdir}/nginx
%dir %{_sysconfdir}/nginx/conf.d
%{_sysconfdir}/nginx/modules
%{_sysconfdir}/nginx/modules-debug

%config(noreplace) %{_sysconfdir}/nginx/nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/default.conf
%config(noreplace) %{_sysconfdir}/nginx/mime.types
%config(noreplace) %{_sysconfdir}/nginx/fastcgi_params
%config(noreplace) %{_sysconfdir}/nginx/scgi_params
%config(noreplace) %{_sysconfdir}/nginx/uwsgi_params
%config(noreplace) %{_sysconfdir}/nginx/shib_clear_headers
%config(noreplace) %{_sysconfdir}/nginx/shib_fastcgi_params
%config(noreplace) %{_sysconfdir}/nginx/koi-utf
%config(noreplace) %{_sysconfdir}/nginx/koi-win
%config(noreplace) %{_sysconfdir}/nginx/win-utf

%config(noreplace) %{_sysconfdir}/logrotate.d/nginx
%config(noreplace) %{_sysconfdir}/sysconfig/nginx
%config(noreplace) %{_sysconfdir}/sysconfig/nginx-debug
%if %{use_systemd}
%{_unitdir}/nginx.service
%{_unitdir}/nginx-debug.service
%dir %{_libexecdir}/initscripts/legacy-actions/nginx
%{_libexecdir}/initscripts/legacy-actions/nginx/*
%else
%{_initrddir}/nginx
%{_initrddir}/nginx-debug
%endif

%attr(0755,root,root) %dir %{_libdir}/nginx
%attr(0755,root,root) %dir %{_libdir}/nginx/modules
%attr(0755,root,root) %{_libdir}/nginx/modules/*.so
%attr(0644,root,root) %{_libdir}/lua/5.1/libjchash.so
%attr(0755,root,root) %dir %{_libdir}/nginx/modules-debug
%attr(0755,root,root) %{_libdir}/nginx/modules-debug/*.so
%attr(0755,root,root) %dir %{_prefix}/lib/nginx/lua
%{_prefix}/lib/nginx/lua/*
%dir %{_datadir}/nginx
%dir %{_datadir}/nginx/html
%{_datadir}/nginx/html/*

%attr(0755,root,root) %dir %{_localstatedir}/cache/nginx
%attr(0755,root,root) %dir %{_localstatedir}/log/nginx

%doc %{_datadir}/doc/%{name}-%{version}
%doc %{_datadir}/doc/%{name}-%{version}/COPYRIGHT

%pre
# Add the "nginx" user
getent group %{nginx_group} >/dev/null || groupadd -r %{nginx_group}
getent passwd %{nginx_user} >/dev/null || \
    useradd -r -g %{nginx_group} -s /sbin/nologin \
    -d %{nginx_home} -c "nginx user"  %{nginx_user}
exit 0

%post
# Register the nginx service
if [ $1 -eq 1 ]; then
%if %{use_systemd}
    /usr/bin/systemctl preset nginx.service >/dev/null 2>&1 ||:
    /usr/bin/systemctl preset nginx-debug.service >/dev/null 2>&1 ||:
%else
    /sbin/chkconfig --add nginx
    /sbin/chkconfig --add nginx-debug
%endif
    # print site info
    cat <<BANNER
----------------------------------------------------------------------

Thanks for using nginx!

Please find the official documentation for nginx here:
* http://nginx.org/en/docs/

Commercial subscriptions for nginx are available on:
* http://nginx.com/products/

----------------------------------------------------------------------
BANNER

    # Touch and set permisions on default log files on installation

    if [ -d %{_localstatedir}/log/nginx ]; then
        if [ ! -e %{_localstatedir}/log/nginx/access.log ]; then
            touch %{_localstatedir}/log/nginx/access.log
            %{__chmod} 640 %{_localstatedir}/log/nginx/access.log
            %{__chown} nginx:%{nginx_loggroup} %{_localstatedir}/log/nginx/access.log
        fi

        if [ ! -e %{_localstatedir}/log/nginx/error.log ]; then
            touch %{_localstatedir}/log/nginx/error.log
            %{__chmod} 640 %{_localstatedir}/log/nginx/error.log
            %{__chown} nginx:%{nginx_loggroup} %{_localstatedir}/log/nginx/error.log
        fi
    fi
fi

%preun
if [ $1 -eq 0 ]; then
%if %use_systemd
    /usr/bin/systemctl --no-reload disable nginx.service >/dev/null 2>&1 ||:
    /usr/bin/systemctl stop nginx.service >/dev/null 2>&1 ||:
%else
    /sbin/service nginx stop > /dev/null 2>&1
    /sbin/chkconfig --del nginx
    /sbin/chkconfig --del nginx-debug
%endif
fi

%postun
%if %use_systemd
/usr/bin/systemctl daemon-reload >/dev/null 2>&1 ||:
%endif
if [ $1 -ge 1 ]; then
    /sbin/service nginx status  >/dev/null 2>&1 || exit 0
    /sbin/service nginx upgrade >/dev/null 2>&1 || echo \
        "Binary upgrade failed, please check nginx's error.log"
fi

%changelog
* Wed Sep 08 2021 Hiroaki Nakamura <hnakamur@gmail.com> - 1.21.3-1
- 1.21.3
- echo_nginx_module 6f8a4abea9dcf366b7cb43f6ce7f1e56d0d409e5
- headers_more_nginx_module f85af9649b858e21b400a2150a4c7b8ebd36e921
- lua_nginx_module 3820d0e118f834916fff66c66f2a29196832dcf8
- lua_upstream_nginx_module 8aa93ead98ba2060d4efd594ae33a35d153589bf
- memc_nginx_module 5ae511de2285e74d4f4129f4a00890c6bef1928e
- redis2_nginx_module 154bc51b9fc118267f9c3d30f52779320956a807
- set_misc_nginx_module 31c4ad67bb9e392a734e4e58ea8048e24012311f
- srcache_nginx_module b61755d098568cd78febf69e6d7499b1d0b7250a
- stream_lua_nginx_module ef1188d0f4a96d77e02efeb96b4cf2c5e48f012b
- lua_resty_balancer 56fd8ad03d5718f507a5129edc43a25948364b9f
- lua_resty_core efce3705c01a348eb6551c57cd56c3f12abba096
- lua_resty_dns 869d2fbb009b6ada93a5a10cb93acd1cc12bd53f
- lua_resty_lock ad94745a4731ee6ddbffbc3b602df25ca7c6f7ba
- lua_resty_lrucache dacd022b4b8e3a73ed25886f2f9db043075ddb31
- lua_resty_limit_traffic 121a320a4e1167f611a9634a410a49e8c41c2c8e
- lua_resty_memcached 1517409a3f23116bb63f080629a6a515cf332d87
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql e40b9a11df87bd0bb2bab3116de9f94a96549fd4
- lua_resty_redis 91585affcd9a8da65cb664a5b1e926dde428095a
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 30ea64310c2c6aabc86774ac4f544a37dd458352
- lua_resty_signal 7b247bd3085007b4e9fa4c09bbb5f591aa19e0a1
- lua_resty_string b192878f6ed31b0af237935bbc5a8110a3c2256c
- lua_resty_upload 7baca92c7e741979ae5857989bbf6cc0402d6126
- lua_resty_upstream_healthcheck 27bf62336219cb4eb804f82e1263a00dff3be398
- lua_resty_websocket b341b7da72a7139cbe27b51c3b50511606e56636
- lua_resty_cookie 303e32e512defced053a6484bc0745cf9dc0d39e
- lua_resty_openidc 59d01573d7d8eeed4cd60666af1cdc90ff8be80b
- lua_resty_session 2cd1f8484fdd429505ac33abf7a44adda1f367bf
- lua_resty_jwt b8b1f6e00be74565111e0cbbc40bc7d26367a646
- lua_resty_hmac 193232acecb8bc15ee414651a53b11a1624e6a16
- lua_resty_http 0ce55d6d15da140ecc5966fa848204c6fd9074e8
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 23e1873aa62acb58b7881eed2a501f5bf35b82e9
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module f59558ebf71c810ceff15d475deb98f15a0a19c9
- nginx_http_shibboleth 605f1ebbfd3e9c7d1328b885d6dd6edcb663c937
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module a26c6beed77e81553686852dceb6c7fdacc5970d
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed Sep 01 2021 Hiroaki Nakamura <hnakamur@gmail.com> - 1.21.2-1
- 1.21.2
- echo_nginx_module 6f8a4abea9dcf366b7cb43f6ce7f1e56d0d409e5
- headers_more_nginx_module f85af9649b858e21b400a2150a4c7b8ebd36e921
- lua_nginx_module a9cd21e943f3a9dde9a0f86dbd692194552b7af4
- lua_upstream_nginx_module 8aa93ead98ba2060d4efd594ae33a35d153589bf
- memc_nginx_module 5ae511de2285e74d4f4129f4a00890c6bef1928e
- redis2_nginx_module 154bc51b9fc118267f9c3d30f52779320956a807
- set_misc_nginx_module fddc347134e97d22c34dc5189e76b0ec97bf84d7
- srcache_nginx_module b61755d098568cd78febf69e6d7499b1d0b7250a
- stream_lua_nginx_module ef1188d0f4a96d77e02efeb96b4cf2c5e48f012b
- lua_resty_balancer 56fd8ad03d5718f507a5129edc43a25948364b9f
- lua_resty_core efce3705c01a348eb6551c57cd56c3f12abba096
- lua_resty_dns 869d2fbb009b6ada93a5a10cb93acd1cc12bd53f
- lua_resty_lock ad94745a4731ee6ddbffbc3b602df25ca7c6f7ba
- lua_resty_lrucache dacd022b4b8e3a73ed25886f2f9db043075ddb31
- lua_resty_limit_traffic 121a320a4e1167f611a9634a410a49e8c41c2c8e
- lua_resty_memcached 1517409a3f23116bb63f080629a6a515cf332d87
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql e40b9a11df87bd0bb2bab3116de9f94a96549fd4
- lua_resty_redis 91585affcd9a8da65cb664a5b1e926dde428095a
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 30ea64310c2c6aabc86774ac4f544a37dd458352
- lua_resty_signal 7b247bd3085007b4e9fa4c09bbb5f591aa19e0a1
- lua_resty_string 67dc5483c59a3b79581f9e9c0a73b926c3659b0a
- lua_resty_upload 7baca92c7e741979ae5857989bbf6cc0402d6126
- lua_resty_upstream_healthcheck 27bf62336219cb4eb804f82e1263a00dff3be398
- lua_resty_websocket b341b7da72a7139cbe27b51c3b50511606e56636
- lua_resty_cookie 303e32e512defced053a6484bc0745cf9dc0d39e
- lua_resty_openidc 59d01573d7d8eeed4cd60666af1cdc90ff8be80b
- lua_resty_session 2cd1f8484fdd429505ac33abf7a44adda1f367bf
- lua_resty_jwt b8b1f6e00be74565111e0cbbc40bc7d26367a646
- lua_resty_hmac 193232acecb8bc15ee414651a53b11a1624e6a16
- lua_resty_http 0ce55d6d15da140ecc5966fa848204c6fd9074e8
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 23e1873aa62acb58b7881eed2a501f5bf35b82e9
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module f59558ebf71c810ceff15d475deb98f15a0a19c9
- nginx_http_shibboleth a5ad18a406451aa5064382ab077ca9258fc3f599
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module a26c6beed77e81553686852dceb6c7fdacc5970d
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Tue Aug 24 2021 Hiroaki Nakamura <hnakamur@gmail.com> - 1.21.1-2
- OpenSSL 1.1.1l

* Wed Jul 07 2021 Hiroaki Nakamura <hnakamur@gmail.com> - 1.21.1-1
- 1.21.1
- echo_nginx_module 5a402aa6c3e0b1fa690d517510ae2c6151497b4c
- headers_more_nginx_module d6d7ebab3c0c5b32ab421ba186783d3e5d2c6a17
- lua_nginx_module ccb0f8cc1087397278ea21ac094a8235658081ef
- lua_upstream_nginx_module b941321b67e7c4c908e84d94ec12991528482e2c
- memc_nginx_module ab68e851b88324b9bfbacfda90b0d5b5487962d2
- redis2_nginx_module 154bc51b9fc118267f9c3d30f52779320956a807
- set_misc_nginx_module 3937e7b575113fc158633a37a3b707dbd0d031cf
- srcache_nginx_module 4143dae84f5dbcc2e08af5113d50573eca84e21c
- stream_lua_nginx_module 429417c7d2aa05508fbe3cc2091d03e337e1b784
- lua_resty_balancer 2e1848e729eb8558d533ce97ffdf61edead39953
- lua_resty_core c08c4c6723754c3d57165bfa35d1e151199e3cdd
- lua_resty_dns 869d2fbb009b6ada93a5a10cb93acd1cc12bd53f
- lua_resty_lock facfe428604023e126140088732ac80313703c94
- lua_resty_lrucache f20bb8ac9489ba87d90d78f929552c2eab153caa
- lua_resty_limit_traffic 56b9a35a69117ed0e8a2e3b9a0866c426403e1b9
- lua_resty_memcached 3e64447c3223998d52be5718549fc87a710616ce
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 77805ebff1738513cb350d7927f2133561d7efe9
- lua_resty_redis 91585affcd9a8da65cb664a5b1e926dde428095a
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 86b56eefc35a1fea6ed5b5a0176cfb2f0a37d5d5
- lua_resty_signal 9a15eea470ab54fdda49890c76a1a3246637efc7
- lua_resty_string 3624678ca1c7c32e2fb16c18b7511863e074d542
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck 88bcedaadbc26bc6f7c9ac74776d67a4b413a512
- lua_resty_websocket d565794524cf9c42a41ed3f1a9848825d24b181f
- lua_resty_cookie 303e32e512defced053a6484bc0745cf9dc0d39e
- lua_resty_openidc 59d01573d7d8eeed4cd60666af1cdc90ff8be80b
- lua_resty_session 2cd1f8484fdd429505ac33abf7a44adda1f367bf
- lua_resty_jwt b8b1f6e00be74565111e0cbbc40bc7d26367a646
- lua_resty_hmac 193232acecb8bc15ee414651a53b11a1624e6a16
- lua_resty_http f754eb7ecc8c969657b357ae82f93a05a29dd395
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 23e1873aa62acb58b7881eed2a501f5bf35b82e9
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module f59558ebf71c810ceff15d475deb98f15a0a19c9
- nginx_http_shibboleth 3b02c89bb36be9d34b77094714f0e293373248c4
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module a26c6beed77e81553686852dceb6c7fdacc5970d
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed May 26 2021 Hiroaki Nakamura <hnakamur@gmail.com> - 1.21.0-1
- 1.21.0

* Wed Apr 14 2021 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.10-1
- 1.19.10
- echo_nginx_module 5a402aa6c3e0b1fa690d517510ae2c6151497b4c
- headers_more_nginx_module d6d7ebab3c0c5b32ab421ba186783d3e5d2c6a17
- lua_nginx_module 1c1bcfeb9276c6dfc9b038a6fa779e7e4b605bc9
- lua_upstream_nginx_module b941321b67e7c4c908e84d94ec12991528482e2c
- memc_nginx_module ab68e851b88324b9bfbacfda90b0d5b5487962d2
- redis2_nginx_module 154bc51b9fc118267f9c3d30f52779320956a807
- set_misc_nginx_module 3937e7b575113fc158633a37a3b707dbd0d031cf
- srcache_nginx_module 4143dae84f5dbcc2e08af5113d50573eca84e21c
- stream_lua_nginx_module 65567d19042ac809ed1f75708e2b2e47f718d1ef
- lua_resty_balancer 2e1848e729eb8558d533ce97ffdf61edead39953
- lua_resty_core 985eb5b323468effaa66deb5cbd4f800b99834cf
- lua_resty_dns ad4a51c8cae8c3fb8f712fa91fda660ab8a89669
- lua_resty_lock facfe428604023e126140088732ac80313703c94
- lua_resty_lrucache 0dea1d4504c3848d1ed3e330a4c3b2c81a15ae4b
- lua_resty_limit_traffic 56b9a35a69117ed0e8a2e3b9a0866c426403e1b9
- lua_resty_memcached 5e81abb7cdfa1756f578311053fd7a5dbca3a6c4
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql d73b4ed339a326d434a2708812c50cc440275470
- lua_resty_redis 12cdc0b8f10d495c647a0a8c1dc01014b082738a
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 86b56eefc35a1fea6ed5b5a0176cfb2f0a37d5d5
- lua_resty_signal fbb650cc918e8614e9d10da0e5231daa3cb37606
- lua_resty_string 435b86a8da73757eedc3b98f9fa7fe7edacdfdf8
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck f354e94395395a9113f43cc952283b3154ac6eb1
- lua_resty_websocket d565794524cf9c42a41ed3f1a9848825d24b181f
- lua_resty_cookie 303e32e512defced053a6484bc0745cf9dc0d39e
- lua_resty_openidc 59d01573d7d8eeed4cd60666af1cdc90ff8be80b
- lua_resty_session 2cd1f8484fdd429505ac33abf7a44adda1f367bf
- lua_resty_jwt b8b1f6e00be74565111e0cbbc40bc7d26367a646
- lua_resty_hmac 193232acecb8bc15ee414651a53b11a1624e6a16
- lua_resty_http 9bf951dfe162dd9710a0e1f4525738d4902e9d20
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module afd350e0d8b7820d7d2cfc3fa748217153265ce6
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module f59558ebf71c810ceff15d475deb98f15a0a19c9
- nginx_http_shibboleth 6cf9efcbb49aea803f140708f6978f08b9d6a233
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module a26c6beed77e81553686852dceb6c7fdacc5970d
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed Mar 31 2021 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.9-1
- 1.19.9
- echo_nginx_module 5a402aa6c3e0b1fa690d517510ae2c6151497b4c
- headers_more_nginx_module d6d7ebab3c0c5b32ab421ba186783d3e5d2c6a17
- lua_nginx_module eb944dedd28231a99d8a2a71cbc392ce2dad36c1
- lua_upstream_nginx_module b941321b67e7c4c908e84d94ec12991528482e2c
- memc_nginx_module ab68e851b88324b9bfbacfda90b0d5b5487962d2
- redis2_nginx_module 154bc51b9fc118267f9c3d30f52779320956a807
- set_misc_nginx_module 3937e7b575113fc158633a37a3b707dbd0d031cf
- srcache_nginx_module 4143dae84f5dbcc2e08af5113d50573eca84e21c
- stream_lua_nginx_module 149d82ea878cbbe4d54bed34870eed575228dc5e
- lua_resty_balancer 2e1848e729eb8558d533ce97ffdf61edead39953
- lua_resty_core 044ff52b5897a62a6bee204302a421d982037358
- lua_resty_dns ad4a51c8cae8c3fb8f712fa91fda660ab8a89669
- lua_resty_lock facfe428604023e126140088732ac80313703c94
- lua_resty_lrucache 0dea1d4504c3848d1ed3e330a4c3b2c81a15ae4b
- lua_resty_limit_traffic cf47c502091a45843d183831125c244d65592b85
- lua_resty_memcached 5e81abb7cdfa1756f578311053fd7a5dbca3a6c4
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql d73b4ed339a326d434a2708812c50cc440275470
- lua_resty_redis 12cdc0b8f10d495c647a0a8c1dc01014b082738a
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 86b56eefc35a1fea6ed5b5a0176cfb2f0a37d5d5
- lua_resty_signal fbb650cc918e8614e9d10da0e5231daa3cb37606
- lua_resty_string 435b86a8da73757eedc3b98f9fa7fe7edacdfdf8
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck f354e94395395a9113f43cc952283b3154ac6eb1
- lua_resty_websocket d565794524cf9c42a41ed3f1a9848825d24b181f
- lua_resty_cookie 303e32e512defced053a6484bc0745cf9dc0d39e
- lua_resty_openidc 59d01573d7d8eeed4cd60666af1cdc90ff8be80b
- lua_resty_session 2cd1f8484fdd429505ac33abf7a44adda1f367bf
- lua_resty_jwt b8b1f6e00be74565111e0cbbc40bc7d26367a646
- lua_resty_hmac 193232acecb8bc15ee414651a53b11a1624e6a16
- lua_resty_http d7f636c28c12cd5ec9a5c033f0c99f9ee943c450
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module afd350e0d8b7820d7d2cfc3fa748217153265ce6
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module f59558ebf71c810ceff15d475deb98f15a0a19c9
- nginx_http_shibboleth 6cf9efcbb49aea803f140708f6978f08b9d6a233
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module a26c6beed77e81553686852dceb6c7fdacc5970d
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Thu Mar 25 2021 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.8-2
- OpenSSL 1.1.1k

* Wed Mar 24 2021 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.8-1
- 1.19.8
- echo_nginx_module 5a402aa6c3e0b1fa690d517510ae2c6151497b4c
- headers_more_nginx_module d6d7ebab3c0c5b32ab421ba186783d3e5d2c6a17
- lua_nginx_module 88a52c44af56476f68c95c9200a380cd82f696dd
- lua_upstream_nginx_module b941321b67e7c4c908e84d94ec12991528482e2c
- memc_nginx_module ab68e851b88324b9bfbacfda90b0d5b5487962d2
- redis2_nginx_module 154bc51b9fc118267f9c3d30f52779320956a807
- set_misc_nginx_module 3937e7b575113fc158633a37a3b707dbd0d031cf
- srcache_nginx_module 4143dae84f5dbcc2e08af5113d50573eca84e21c
- stream_lua_nginx_module e9cfdc06513849bb61283bcc629695634cef3162
- lua_resty_balancer 2e1848e729eb8558d533ce97ffdf61edead39953
- lua_resty_core 044ff52b5897a62a6bee204302a421d982037358
- lua_resty_dns ad4a51c8cae8c3fb8f712fa91fda660ab8a89669
- lua_resty_lock facfe428604023e126140088732ac80313703c94
- lua_resty_lrucache 0dea1d4504c3848d1ed3e330a4c3b2c81a15ae4b
- lua_resty_limit_traffic cf47c502091a45843d183831125c244d65592b85
- lua_resty_memcached 5e81abb7cdfa1756f578311053fd7a5dbca3a6c4
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql d73b4ed339a326d434a2708812c50cc440275470
- lua_resty_redis 12cdc0b8f10d495c647a0a8c1dc01014b082738a
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 86b56eefc35a1fea6ed5b5a0176cfb2f0a37d5d5
- lua_resty_signal fbb650cc918e8614e9d10da0e5231daa3cb37606
- lua_resty_string 435b86a8da73757eedc3b98f9fa7fe7edacdfdf8
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck f354e94395395a9113f43cc952283b3154ac6eb1
- lua_resty_websocket d565794524cf9c42a41ed3f1a9848825d24b181f
- lua_resty_cookie 303e32e512defced053a6484bc0745cf9dc0d39e
- lua_resty_openidc 59d01573d7d8eeed4cd60666af1cdc90ff8be80b
- lua_resty_session 2cd1f8484fdd429505ac33abf7a44adda1f367bf
- lua_resty_jwt b8b1f6e00be74565111e0cbbc40bc7d26367a646
- lua_resty_hmac 193232acecb8bc15ee414651a53b11a1624e6a16
- lua_resty_http 1120af703db606045c36c6832033522f846820f6
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module afd350e0d8b7820d7d2cfc3fa748217153265ce6
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module f59558ebf71c810ceff15d475deb98f15a0a19c9
- nginx_http_shibboleth 38cf8e614aa8d94ecd01135af8dea3c311a198e2
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module a26c6beed77e81553686852dceb6c7fdacc5970d
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed Feb 17 2021 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.7-1
- OpenSSL 1.1.1j
- 1.19.7
- echo_nginx_module 5a402aa6c3e0b1fa690d517510ae2c6151497b4c
- headers_more_nginx_module d6d7ebab3c0c5b32ab421ba186783d3e5d2c6a17
- lua_nginx_module 88a52c44af56476f68c95c9200a380cd82f696dd
- lua_upstream_nginx_module b941321b67e7c4c908e84d94ec12991528482e2c
- memc_nginx_module ab68e851b88324b9bfbacfda90b0d5b5487962d2
- redis2_nginx_module 154bc51b9fc118267f9c3d30f52779320956a807
- set_misc_nginx_module 3937e7b575113fc158633a37a3b707dbd0d031cf
- srcache_nginx_module 4143dae84f5dbcc2e08af5113d50573eca84e21c
- stream_lua_nginx_module e9cfdc06513849bb61283bcc629695634cef3162
- lua_resty_balancer 2e1848e729eb8558d533ce97ffdf61edead39953
- lua_resty_core 42828f15d4a0e6ed83d29264f29fbfddac9573ef
- lua_resty_dns 6d96cfb5875a2d6267f1a4c66a91a01aa86702a0
- lua_resty_lock facfe428604023e126140088732ac80313703c94
- lua_resty_lrucache 0dea1d4504c3848d1ed3e330a4c3b2c81a15ae4b
- lua_resty_limit_traffic cf47c502091a45843d183831125c244d65592b85
- lua_resty_memcached 5e81abb7cdfa1756f578311053fd7a5dbca3a6c4
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 1067431d973a1c6a43d2c8b0a836f1d12a216bf8
- lua_resty_redis 12cdc0b8f10d495c647a0a8c1dc01014b082738a
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 86b56eefc35a1fea6ed5b5a0176cfb2f0a37d5d5
- lua_resty_signal fbb650cc918e8614e9d10da0e5231daa3cb37606
- lua_resty_string 435b86a8da73757eedc3b98f9fa7fe7edacdfdf8
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck f354e94395395a9113f43cc952283b3154ac6eb1
- lua_resty_websocket d565794524cf9c42a41ed3f1a9848825d24b181f
- lua_resty_cookie 303e32e512defced053a6484bc0745cf9dc0d39e
- lua_resty_openidc e35fa162176382846a1d11018aff46c63fa8e87c
- lua_resty_session 2cd1f8484fdd429505ac33abf7a44adda1f367bf
- lua_resty_jwt b8b1f6e00be74565111e0cbbc40bc7d26367a646
- lua_resty_hmac 193232acecb8bc15ee414651a53b11a1624e6a16
- lua_resty_http 902eecf9d44972e640377e1ec67d29ea15739389
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module afd350e0d8b7820d7d2cfc3fa748217153265ce6
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module f59558ebf71c810ceff15d475deb98f15a0a19c9
- nginx_http_shibboleth 2e99740bc3aeb2c9212ddaaa36185ea23d51c5fd
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module a26c6beed77e81553686852dceb6c7fdacc5970d
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed Dec 16 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.6-1
- 1.19.6
- echo_nginx_module 5a402aa6c3e0b1fa690d517510ae2c6151497b4c
- headers_more_nginx_module d6d7ebab3c0c5b32ab421ba186783d3e5d2c6a17
- lua_nginx_module 138c1b96423aa26defe00fe64dd5760ef17e5ad8
- lua_upstream_nginx_module b941321b67e7c4c908e84d94ec12991528482e2c
- memc_nginx_module ab68e851b88324b9bfbacfda90b0d5b5487962d2
- redis2_nginx_module 154bc51b9fc118267f9c3d30f52779320956a807
- set_misc_nginx_module 3937e7b575113fc158633a37a3b707dbd0d031cf
- srcache_nginx_module 4143dae84f5dbcc2e08af5113d50573eca84e21c
- stream_lua_nginx_module 9c53258faf425d85198413878154ea6bd58b2619
- lua_resty_balancer af4508f7aa5560c7d810922c2515b557f9e5d51a
- lua_resty_core 3b4ad750af4b9211d110340c354160f4fecc0c5d
- lua_resty_dns 6d96cfb5875a2d6267f1a4c66a91a01aa86702a0
- lua_resty_lock facfe428604023e126140088732ac80313703c94
- lua_resty_lrucache c40175034160f5a2eeae967326b3a804fc118c29
- lua_resty_limit_traffic cf47c502091a45843d183831125c244d65592b85
- lua_resty_memcached 020353154d644fdb957791b9aac36a19e5413816
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 7284ec351bdefd310e108ef4e6c42bd6881b32da
- lua_resty_redis 0244f0931b71b2cd9fba7dab2549792d1ae71ec6
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 86b56eefc35a1fea6ed5b5a0176cfb2f0a37d5d5
- lua_resty_signal 3c3e4f419e785e6464f6523a982e85901b833a0e
- lua_resty_string bf8cec1ca195f53bee1cd09c310a473927e62f79
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck f354e94395395a9113f43cc952283b3154ac6eb1
- lua_resty_websocket d565794524cf9c42a41ed3f1a9848825d24b181f
- lua_resty_cookie 303e32e512defced053a6484bc0745cf9dc0d39e
- lua_resty_openidc e35fa162176382846a1d11018aff46c63fa8e87c
- lua_resty_session b4e542c0e5bb01b62e89dcc904bdd94b42c826af
- lua_resty_jwt d1798eb236cac5cce7e273ee8d48747739a03754
- lua_resty_hmac 193232acecb8bc15ee414651a53b11a1624e6a16
- lua_resty_http 902eecf9d44972e640377e1ec67d29ea15739389
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module afd350e0d8b7820d7d2cfc3fa748217153265ce6
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module f59558ebf71c810ceff15d475deb98f15a0a19c9
- nginx_http_shibboleth a386c1844d9a3ed7dbe867fb5c937ccc6975a518
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module a26c6beed77e81553686852dceb6c7fdacc5970d
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed Dec 09 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.5-2
- OpenSSL 1.1.1i

* Wed Nov 25 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.5-1
- 1.19.5
- echo_nginx_module 5a402aa6c3e0b1fa690d517510ae2c6151497b4c
- headers_more_nginx_module d6d7ebab3c0c5b32ab421ba186783d3e5d2c6a17
- lua_nginx_module 7105adaa523adedec80f0aaa13388b88d08988f8
- lua_upstream_nginx_module b941321b67e7c4c908e84d94ec12991528482e2c
- memc_nginx_module ab68e851b88324b9bfbacfda90b0d5b5487962d2
- redis2_nginx_module 154bc51b9fc118267f9c3d30f52779320956a807
- set_misc_nginx_module 3937e7b575113fc158633a37a3b707dbd0d031cf
- srcache_nginx_module 4143dae84f5dbcc2e08af5113d50573eca84e21c
- stream_lua_nginx_module 1a1e49bd4be0f858818c4f133a06e2ac9a2ab306
- lua_resty_balancer af4508f7aa5560c7d810922c2515b557f9e5d51a
- lua_resty_core d5f6127e0c0c8b7c076c9843f2fdc422a63a3188
- lua_resty_dns 6d96cfb5875a2d6267f1a4c66a91a01aa86702a0
- lua_resty_lock facfe428604023e126140088732ac80313703c94
- lua_resty_lrucache c40175034160f5a2eeae967326b3a804fc118c29
- lua_resty_limit_traffic cf47c502091a45843d183831125c244d65592b85
- lua_resty_memcached 020353154d644fdb957791b9aac36a19e5413816
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 7284ec351bdefd310e108ef4e6c42bd6881b32da
- lua_resty_redis 0244f0931b71b2cd9fba7dab2549792d1ae71ec6
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 86b56eefc35a1fea6ed5b5a0176cfb2f0a37d5d5
- lua_resty_signal 3c3e4f419e785e6464f6523a982e85901b833a0e
- lua_resty_string bf8cec1ca195f53bee1cd09c310a473927e62f79
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck f354e94395395a9113f43cc952283b3154ac6eb1
- lua_resty_websocket d565794524cf9c42a41ed3f1a9848825d24b181f
- lua_resty_cookie 303e32e512defced053a6484bc0745cf9dc0d39e
- lua_resty_openidc 49be8033b7a3dc0557c133f8616645ca19485950
- lua_resty_session b4e542c0e5bb01b62e89dcc904bdd94b42c826af
- lua_resty_jwt d1798eb236cac5cce7e273ee8d48747739a03754
- lua_resty_hmac 193232acecb8bc15ee414651a53b11a1624e6a16
- lua_resty_http a6bd2e0eb1390e330e4fb10a48cced5a1f21fb66
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module f59558ebf71c810ceff15d475deb98f15a0a19c9
- nginx_http_shibboleth 184eea4be6b2b3bed5fce659449b108dc3417f91
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module 1cabd8a1f68ea3998f94e9f3504431970f848fbf
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed Oct 28 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.4-1
- 1.19.4
- Update line offsets in nginx-1.17.3-cache_manager.patch and
  rename to nginx-1.19.4-cache_manager.patch.
- echo_nginx_module 5a402aa6c3e0b1fa690d517510ae2c6151497b4c
- headers_more_nginx_module d6d7ebab3c0c5b32ab421ba186783d3e5d2c6a17
- lua_nginx_module 65d87507489b31b86419b0fcecc1c75ce46d0ece
- lua_upstream_nginx_module b941321b67e7c4c908e84d94ec12991528482e2c
- memc_nginx_module ab68e851b88324b9bfbacfda90b0d5b5487962d2
- redis2_nginx_module 154bc51b9fc118267f9c3d30f52779320956a807
- set_misc_nginx_module 3937e7b575113fc158633a37a3b707dbd0d031cf
- srcache_nginx_module 4143dae84f5dbcc2e08af5113d50573eca84e21c
- stream_lua_nginx_module f837686b47b29200cc0e16b58a4f58917d3d1a51
- lua_resty_balancer af4508f7aa5560c7d810922c2515b557f9e5d51a
- lua_resty_core 12abf47c9ba3eb1e85195ab751f028221996e1df
- lua_resty_dns 6d96cfb5875a2d6267f1a4c66a91a01aa86702a0
- lua_resty_lock facfe428604023e126140088732ac80313703c94
- lua_resty_lrucache c40175034160f5a2eeae967326b3a804fc118c29
- lua_resty_limit_traffic cf47c502091a45843d183831125c244d65592b85
- lua_resty_memcached 020353154d644fdb957791b9aac36a19e5413816
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 69c9f53d6bd7e0537e6824344e7c51b7e816358c
- lua_resty_redis 0244f0931b71b2cd9fba7dab2549792d1ae71ec6
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 86b56eefc35a1fea6ed5b5a0176cfb2f0a37d5d5
- lua_resty_signal 3c3e4f419e785e6464f6523a982e85901b833a0e
- lua_resty_string bf8cec1ca195f53bee1cd09c310a473927e62f79
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck f354e94395395a9113f43cc952283b3154ac6eb1
- lua_resty_websocket d565794524cf9c42a41ed3f1a9848825d24b181f
- lua_resty_cookie 303e32e512defced053a6484bc0745cf9dc0d39e
- lua_resty_openidc df75c6e26cb7dbc9d78927d989e98be04173f10b
- lua_resty_session b4e542c0e5bb01b62e89dcc904bdd94b42c826af
- lua_resty_jwt d1798eb236cac5cce7e273ee8d48747739a03754
- lua_resty_hmac 193232acecb8bc15ee414651a53b11a1624e6a16
- lua_resty_http a6bd2e0eb1390e330e4fb10a48cced5a1f21fb66
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module f59558ebf71c810ceff15d475deb98f15a0a19c9
- nginx_http_shibboleth e4ec2eeec6b72c3731dbed1c01d44ca297c2e080
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module 1cabd8a1f68ea3998f94e9f3504431970f848fbf
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed Sep 30 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.3-1
- 1.19.3
- echo_nginx_module 08ad67787d19235cb298f061e8950afbb6fd48b9
- headers_more_nginx_module af8160e0174c7187818a3396559486200af0f663
- lua_nginx_module 4d2a04a08147c2d0ba2ec9632b649264b7d006a9
- lua_upstream_nginx_module 2f012de74710da7750ed56ed3cb53ded2d62fc12
- memc_nginx_module dfbed06016b73e3e84cd961735a352e4f5477865
- redis2_nginx_module cc146f37440f798ffc41c3cb792eca3c60bc62d3
- set_misc_nginx_module 4667684cfed0f523596895d338f376ffd5f72879
- srcache_nginx_module ab46d947e2fda591de06dac3ba6c9c6f0e8f6b61
- stream_lua_nginx_module 77f82d60963d96488dfbdf9756d2a67bb7902191
- lua_resty_balancer af4508f7aa5560c7d810922c2515b557f9e5d51a
- lua_resty_core d130d96591cf72a958f02a9af39aa9ecb7c0f3fc
- lua_resty_dns cddf8cd81cda5ff94e5aab26bb622f0384d0324a
- lua_resty_lock 987b0e9c6748e2af0f4300309ab8c94df5be9692
- lua_resty_lrucache b2035269ac353444ac65af3969692bcae4fc1605
- lua_resty_limit_traffic bd1cc13b0a635fd057bc639dc56d26bd0cd3ee74
- lua_resty_memcached d4b0186d5e2f65e38c3c63408d462d98c8dc5977
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 472a4d7831fcc1e8d444e69bdde19872b49e4f5e
- lua_resty_redis e0efd8702b3bf97ad38dd1e412470e01fc7f9338
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell ea23b3d6d4a4b3c475a3e0b530469343694e775c
- lua_resty_signal 6b1bf606563c18eb4a25a7f36e9e2337af9217c0
- lua_resty_string 9a543f8531241745f8814e8e02475351042774ec
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck 26bad5df8131d93c6f06011cce82b80929ad8340
- lua_resty_websocket f5ed6c4ca6dbd85363e68cbd4a450e76c0ed3c1d
- lua_resty_cookie 303e32e512defced053a6484bc0745cf9dc0d39e
- lua_resty_openidc bfcfcce577185a95b019c34e446fe6b089124cbf
- lua_resty_session 3e4a3b9fbae76d9621b41db760989345f623f8f2
- lua_resty_jwt d1798eb236cac5cce7e273ee8d48747739a03754
- lua_resty_hmac 193232acecb8bc15ee414651a53b11a1624e6a16
- lua_resty_http a6bd2e0eb1390e330e4fb10a48cced5a1f21fb66
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module f59558ebf71c810ceff15d475deb98f15a0a19c9
- nginx_http_shibboleth 3f5ff4212fa12de23cb1acae8bf3a5a432b3f43b
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module 1cabd8a1f68ea3998f94e9f3504431970f848fbf
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed Sep 23 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.2-2
- OpenSSL 1.1.1h

* Wed Aug 12 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.2-1
- 1.19.2
- echo_nginx_module 08ad67787d19235cb298f061e8950afbb6fd48b9
- headers_more_nginx_module 743a4bb1a253325d17a4f4ce8ee61ea0d8e0cc19
- lua_nginx_module 21cfd8ab26b0aec0520f2d707770cb9e34680a5b
- lua_upstream_nginx_module 2f012de74710da7750ed56ed3cb53ded2d62fc12
- memc_nginx_module dfbed06016b73e3e84cd961735a352e4f5477865
- redis2_nginx_module cc146f37440f798ffc41c3cb792eca3c60bc62d3
- set_misc_nginx_module 4667684cfed0f523596895d338f376ffd5f72879
- srcache_nginx_module ab46d947e2fda591de06dac3ba6c9c6f0e8f6b61
- stream_lua_nginx_module 6eb31d265b1ba3707188709db0a141831dc7fd40
- lua_resty_balancer 5647c48c76bb7be6fa23bcf4b2d90b6133ed5b87
- lua_resty_core 464121e031bf4cbfb413b8c28ddc17113a9be103
- lua_resty_dns cddf8cd81cda5ff94e5aab26bb622f0384d0324a
- lua_resty_lock 987b0e9c6748e2af0f4300309ab8c94df5be9692
- lua_resty_lrucache b2035269ac353444ac65af3969692bcae4fc1605
- lua_resty_limit_traffic bd1cc13b0a635fd057bc639dc56d26bd0cd3ee74
- lua_resty_memcached d4b0186d5e2f65e38c3c63408d462d98c8dc5977
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 472a4d7831fcc1e8d444e69bdde19872b49e4f5e
- lua_resty_redis e0efd8702b3bf97ad38dd1e412470e01fc7f9338
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell ea23b3d6d4a4b3c475a3e0b530469343694e775c
- lua_resty_signal 6b1bf606563c18eb4a25a7f36e9e2337af9217c0
- lua_resty_string 9a543f8531241745f8814e8e02475351042774ec
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck 26bad5df8131d93c6f06011cce82b80929ad8340
- lua_resty_websocket cdb16f2434819c61ca0db6792db1c7069bcf5e06
- lua_resty_cookie c54865bdcfc3c42cbd6dbbceb654ba73871d07f6
- lua_resty_openidc 9155766ea354cb74c6fe496eaa7545e822f60297
- lua_resty_session 3e4a3b9fbae76d9621b41db760989345f623f8f2
- lua_resty_jwt d1798eb236cac5cce7e273ee8d48747739a03754
- lua_resty_hmac 696db6e747acf3dde995bed098837c9f608cc748
- lua_resty_http a6bd2e0eb1390e330e4fb10a48cced5a1f21fb66
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module f59558ebf71c810ceff15d475deb98f15a0a19c9
- nginx_http_shibboleth 5eadab80b2f5940d8873398bca000d93d3f0cf27
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module 1cabd8a1f68ea3998f94e9f3504431970f848fbf
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed Jul 08 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.1-1
- 1.19.1
- echo_nginx_module 08ad67787d19235cb298f061e8950afbb6fd48b9
- headers_more_nginx_module 743a4bb1a253325d17a4f4ce8ee61ea0d8e0cc19
- lua_nginx_module 635b6e864c385bc16125bd43a2ffe8b4560ca9fa
- lua_upstream_nginx_module 2f012de74710da7750ed56ed3cb53ded2d62fc12
- memc_nginx_module dfbed06016b73e3e84cd961735a352e4f5477865
- redis2_nginx_module cc146f37440f798ffc41c3cb792eca3c60bc62d3
- set_misc_nginx_module 4667684cfed0f523596895d338f376ffd5f72879
- srcache_nginx_module ab46d947e2fda591de06dac3ba6c9c6f0e8f6b61
- stream_lua_nginx_module 5a8bc299acf365f9511537895482cc29c161482a
- lua_resty_balancer 3807cd5501f3702f0d24bdba465d98e32d29c219
- lua_resty_core b7d0a681bb41e6e3f29e8ddc438ef26fd819bb19
- lua_resty_dns cddf8cd81cda5ff94e5aab26bb622f0384d0324a
- lua_resty_lock 987b0e9c6748e2af0f4300309ab8c94df5be9692
- lua_resty_lrucache b2035269ac353444ac65af3969692bcae4fc1605
- lua_resty_limit_traffic bd1cc13b0a635fd057bc639dc56d26bd0cd3ee74
- lua_resty_memcached d4b0186d5e2f65e38c3c63408d462d98c8dc5977
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql a46c69b40fc49ee16ad99935ff3858fee05798f7
- lua_resty_redis e2db038fccc48674a4b3956f3a9de5197b235505
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell ea23b3d6d4a4b3c475a3e0b530469343694e775c
- lua_resty_signal 6b1bf606563c18eb4a25a7f36e9e2337af9217c0
- lua_resty_string 9a543f8531241745f8814e8e02475351042774ec
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck 26bad5df8131d93c6f06011cce82b80929ad8340
- lua_resty_websocket cdb16f2434819c61ca0db6792db1c7069bcf5e06
- lua_resty_cookie c54865bdcfc3c42cbd6dbbceb654ba73871d07f6
- lua_resty_openidc 9155766ea354cb74c6fe496eaa7545e822f60297
- lua_resty_session 3e4a3b9fbae76d9621b41db760989345f623f8f2
- lua_resty_jwt d1798eb236cac5cce7e273ee8d48747739a03754
- lua_resty_hmac 696db6e747acf3dde995bed098837c9f608cc748
- lua_resty_http a6bd2e0eb1390e330e4fb10a48cced5a1f21fb66
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth 0c7987f54931b71ec9a50b1e541bf24f256520c7
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module 1cabd8a1f68ea3998f94e9f3504431970f848fbf
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed May 27 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.19.0-1
- 1.19.0
- echo_nginx_module a47a9817660db383a996f4683f2375a8735140a5
- headers_more_nginx_module 743a4bb1a253325d17a4f4ce8ee61ea0d8e0cc19
- lua_nginx_module febd730062a80593cadef29fff28f3b4a40c786a
- lua_upstream_nginx_module 2f012de74710da7750ed56ed3cb53ded2d62fc12
- memc_nginx_module dfbed06016b73e3e84cd961735a352e4f5477865
- redis2_nginx_module cc146f37440f798ffc41c3cb792eca3c60bc62d3
- set_misc_nginx_module 4667684cfed0f523596895d338f376ffd5f72879
- srcache_nginx_module 824f691819a587910b72c19c6374c79d61630594
- stream_lua_nginx_module 61cfab814418df78638c6d3c68dfd326e37bdf8c
- lua_resty_balancer 3807cd5501f3702f0d24bdba465d98e32d29c219
- lua_resty_core 266d19ca16a518956a27955a254369afcd14a4a4
- lua_resty_dns cddf8cd81cda5ff94e5aab26bb622f0384d0324a
- lua_resty_lock 987b0e9c6748e2af0f4300309ab8c94df5be9692
- lua_resty_lrucache b2035269ac353444ac65af3969692bcae4fc1605
- lua_resty_limit_traffic 2c5a23196360d533883cbfa03b3543fc7dfba4d5
- lua_resty_memcached d4b0186d5e2f65e38c3c63408d462d98c8dc5977
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 180db30817020356acfe810ea666d1db567cf65d
- lua_resty_redis 84dc8bc5c32db4c150d3fddeaf410277450b5cd6
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell ea23b3d6d4a4b3c475a3e0b530469343694e775c
- lua_resty_signal 6b1bf606563c18eb4a25a7f36e9e2337af9217c0
- lua_resty_string 9a543f8531241745f8814e8e02475351042774ec
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck 26bad5df8131d93c6f06011cce82b80929ad8340
- lua_resty_websocket cdb16f2434819c61ca0db6792db1c7069bcf5e06
- lua_resty_cookie c54865bdcfc3c42cbd6dbbceb654ba73871d07f6
- lua_resty_openidc 9155766ea354cb74c6fe496eaa7545e822f60297
- lua_resty_session ee6e6bab9ec4bd6b7ba6352eaefc531013ca05e7
- lua_resty_jwt d1798eb236cac5cce7e273ee8d48747739a03754
- lua_resty_hmac 696db6e747acf3dde995bed098837c9f608cc748
- lua_resty_http a6bd2e0eb1390e330e4fb10a48cced5a1f21fb66
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth fe5fcd27c0cc5a44d7099af18b1593e0ffbde7da
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module 1cabd8a1f68ea3998f94e9f3504431970f848fbf
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed Apr 22 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.10-2
- OpenSSL 1.1.1g
- echo_nginx_module a47a9817660db383a996f4683f2375a8735140a5
- headers_more_nginx_module 743a4bb1a253325d17a4f4ce8ee61ea0d8e0cc19
- lua_nginx_module 896638287afd83f060d3f8e9a51b53dbd26d0ae7
- lua_upstream_nginx_module 2f012de74710da7750ed56ed3cb53ded2d62fc12
- memc_nginx_module dfbed06016b73e3e84cd961735a352e4f5477865
- redis2_nginx_module cc146f37440f798ffc41c3cb792eca3c60bc62d3
- set_misc_nginx_module 5cc144d7b3387f4bf90ad92525985c835255debd
- srcache_nginx_module 824f691819a587910b72c19c6374c79d61630594
- stream_lua_nginx_module 61cfab814418df78638c6d3c68dfd326e37bdf8c
- lua_resty_balancer 3807cd5501f3702f0d24bdba465d98e32d29c219
- lua_resty_core 1bd74f8f502a9dc0a7099110d0ee184187698d01
- lua_resty_dns cddf8cd81cda5ff94e5aab26bb622f0384d0324a
- lua_resty_lock 987b0e9c6748e2af0f4300309ab8c94df5be9692
- lua_resty_lrucache b2035269ac353444ac65af3969692bcae4fc1605
- lua_resty_limit_traffic 2c5a23196360d533883cbfa03b3543fc7dfba4d5
- lua_resty_memcached fe57a4ad265deeaa3a7ce57cc77c2c074f2bd48c
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 180db30817020356acfe810ea666d1db567cf65d
- lua_resty_redis 3323079b1fccc449bebdfb286ef65892ae31f88b
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell ea23b3d6d4a4b3c475a3e0b530469343694e775c
- lua_resty_signal 6b1bf606563c18eb4a25a7f36e9e2337af9217c0
- lua_resty_string 9a543f8531241745f8814e8e02475351042774ec
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck 26bad5df8131d93c6f06011cce82b80929ad8340
- lua_resty_websocket 739183cd638eb069af2686682a3810c28d822e82
- lua_resty_cookie c54865bdcfc3c42cbd6dbbceb654ba73871d07f6
- lua_resty_openidc b9fd68e20da0429a9c5c3061a4d1fdce6c799423
- lua_resty_session c6e246d51def4926a803ee0ff35e46890f41b497
- lua_resty_jwt 381ccbaa6649f35ae57d6ffaa2d5120a1bafd8dd
- lua_resty_hmac 5f60e1a28b9fdd7939f0e1738171f0ca5fe22978
- lua_resty_http a6bd2e0eb1390e330e4fb10a48cced5a1f21fb66
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth dc7409d2f1d764ab87d85a03025799e89f99175b
- nginx_lua_saml_service_provider ae2c02dc4c56b11d7536d8f7b7d25ef152edf7c7
- nginx_lua_session 9c5053a7c9d2e8748f1153193d598dcea16417f4
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module 1cabd8a1f68ea3998f94e9f3504431970f848fbf
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed Apr 15 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.10-1
- 1.17.10
- OpenSSL 1.1.1f
- Add lua-resty-woothee and lua-resty-jump-consistent-hash
- echo_nginx_module a47a9817660db383a996f4683f2375a8735140a5
- headers_more_nginx_module 743a4bb1a253325d17a4f4ce8ee61ea0d8e0cc19
- lua_nginx_module 896638287afd83f060d3f8e9a51b53dbd26d0ae7
- lua_upstream_nginx_module 2f012de74710da7750ed56ed3cb53ded2d62fc12
- memc_nginx_module dfbed06016b73e3e84cd961735a352e4f5477865
- redis2_nginx_module cc146f37440f798ffc41c3cb792eca3c60bc62d3
- set_misc_nginx_module 5cc144d7b3387f4bf90ad92525985c835255debd
- srcache_nginx_module 824f691819a587910b72c19c6374c79d61630594
- stream_lua_nginx_module 61cfab814418df78638c6d3c68dfd326e37bdf8c
- lua_resty_balancer 3807cd5501f3702f0d24bdba465d98e32d29c219
- lua_resty_core 1bd74f8f502a9dc0a7099110d0ee184187698d01
- lua_resty_dns cddf8cd81cda5ff94e5aab26bb622f0384d0324a
- lua_resty_lock 987b0e9c6748e2af0f4300309ab8c94df5be9692
- lua_resty_lrucache b2035269ac353444ac65af3969692bcae4fc1605
- lua_resty_limit_traffic 2c5a23196360d533883cbfa03b3543fc7dfba4d5
- lua_resty_memcached fe57a4ad265deeaa3a7ce57cc77c2c074f2bd48c
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 180db30817020356acfe810ea666d1db567cf65d
- lua_resty_redis 057093e8f8c33974c3acdc941404158cb6a2c2a2
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell ea23b3d6d4a4b3c475a3e0b530469343694e775c
- lua_resty_signal 6b1bf606563c18eb4a25a7f36e9e2337af9217c0
- lua_resty_string 9a543f8531241745f8814e8e02475351042774ec
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck 26bad5df8131d93c6f06011cce82b80929ad8340
- lua_resty_websocket 739183cd638eb069af2686682a3810c28d822e82
- lua_resty_cookie c54865bdcfc3c42cbd6dbbceb654ba73871d07f6
- lua_resty_openidc b9fd68e20da0429a9c5c3061a4d1fdce6c799423
- lua_resty_session c6e246d51def4926a803ee0ff35e46890f41b497
- lua_resty_jwt 381ccbaa6649f35ae57d6ffaa2d5120a1bafd8dd
- lua_resty_hmac 5f60e1a28b9fdd7939f0e1738171f0ca5fe22978
- lua_resty_http a6bd2e0eb1390e330e4fb10a48cced5a1f21fb66
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth 473270289dcecced713025d5d77bae901389506b
- nginx_lua_saml_service_provider e5256d0008210318cacf6bbd9b29bfa693b78811
- nginx_lua_session db89c135fd920410cac31be60afb17d511851bfd
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module 1cabd8a1f68ea3998f94e9f3504431970f848fbf
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230
- lua_resty_woothee 0e594c4582f5e47a3eef1c755c59e5c8ae86d268
- lua_resty_jump_consistent_hash a01d2683bfe34cc4edaab7ecac7906d51dfbd125

* Wed Mar 04 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.9-1
- echo_nginx_module a47a9817660db383a996f4683f2375a8735140a5
- headers_more_nginx_module 743a4bb1a253325d17a4f4ce8ee61ea0d8e0cc19
- lua_nginx_module 4c4bb0fcbd12fc79e5adc5fad5d454dc03be875f
- lua_upstream_nginx_module 2f012de74710da7750ed56ed3cb53ded2d62fc12
- memc_nginx_module dfbed06016b73e3e84cd961735a352e4f5477865
- redis2_nginx_module cc146f37440f798ffc41c3cb792eca3c60bc62d3
- set_misc_nginx_module 5cc144d7b3387f4bf90ad92525985c835255debd
- srcache_nginx_module 824f691819a587910b72c19c6374c79d61630594
- stream_lua_nginx_module d987a0cb2f38eae7730be60bd2ddb7dcfd2335b4
- lua_resty_balancer 3807cd5501f3702f0d24bdba465d98e32d29c219
- lua_resty_core bdcc16bbd157dc70a0944f66f622899092f49a41
- lua_resty_dns cddf8cd81cda5ff94e5aab26bb622f0384d0324a
- lua_resty_lock 987b0e9c6748e2af0f4300309ab8c94df5be9692
- lua_resty_lrucache b2035269ac353444ac65af3969692bcae4fc1605
- lua_resty_limit_traffic 2c5a23196360d533883cbfa03b3543fc7dfba4d5
- lua_resty_memcached fe57a4ad265deeaa3a7ce57cc77c2c074f2bd48c
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 356da402ac76703aebb475eb2568f81960a8d2cd
- lua_resty_redis 057093e8f8c33974c3acdc941404158cb6a2c2a2
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell ea23b3d6d4a4b3c475a3e0b530469343694e775c
- lua_resty_signal 6b1bf606563c18eb4a25a7f36e9e2337af9217c0
- lua_resty_string 9a543f8531241745f8814e8e02475351042774ec
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck 26bad5df8131d93c6f06011cce82b80929ad8340
- lua_resty_websocket 739183cd638eb069af2686682a3810c28d822e82
- lua_resty_cookie c54865bdcfc3c42cbd6dbbceb654ba73871d07f6
- lua_resty_openidc 7d3cbe555f53a1a1378cdd9efdd4b7a6cda06d9f
- lua_resty_session 0a82227cf079f6c34688c33d542306c59f04c976
- lua_resty_jwt 425261aa15ea06a9dfbc6ebc57996348d71cbf14
- lua_resty_hmac 5f60e1a28b9fdd7939f0e1738171f0ca5fe22978
- lua_resty_http 41b2e822ce5c19f64e293b7dc2d5d244e511615d
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth cb0e0d7f7a587f3d1b4c2e5d99e9e561bee089e5
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib 1fb69ca505444097c82d2b72e87904f3ed923ae9
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module 1cabd8a1f68ea3998f94e9f3504431970f848fbf
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230

* Tue Jan 21 2020 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.8-1
- echo_nginx_module 996412d8156c1d1054128e7c52fae705d327de30
- headers_more_nginx_module 552e216a0da95c685d9db4f43e209c3f2a803e49
- lua_nginx_module c2390abb584e7aa69894e7d8a6acc7dd7879a753
- lua_upstream_nginx_module 6080f51f2a76b8ce5ee11e6e799442c0284fc442
- memc_nginx_module 32124a5454238ca5ae78a8df9298445293e8d73c
- redis2_nginx_module 15b0c454c987599689c369c2dd4ef07f3d2bcaca
- set_misc_nginx_module b28f23335a8c0020f3b189275af5f6ae11c4cd59
- srcache_nginx_module c196c2615ae4eca992d9f3439e215bbd493caa2e
- stream_lua_nginx_module c7ac2234ec7a26bdcd3b17cbb5314f17344f9f5c
- lua_resty_balancer 3807cd5501f3702f0d24bdba465d98e32d29c219
- lua_resty_core e0aba0b77e606cd1af43caeddf788999f842653d
- lua_resty_dns 6b20b9d28c5efd5164919c9377fbeece2e86ce21
- lua_resty_lock 89017540b06d6548de90dac4d1c377fcaa53d449
- lua_resty_lrucache 1861b4a856102c94222628d103e801f476861377
- lua_resty_limit_traffic cf31eb4a71792589d5f647d9dc0e0de79fea3bf6
- lua_resty_memcached afa425d9377645f04cf808941d42af643cf05ec2
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 2c3ce08dda74be3d4b576372107214478efa3fae
- lua_resty_redis 9536180768854d76c278825a7980c47dce888812
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 70fe0ee9fe86fce462369da486b42a3ba6fee21c
- lua_resty_signal 93d23c96123da25e5d5eef4cf5fe13dbe5e4aea9
- lua_resty_string 595c5fd519fafa3af30002fd1ea5226d520a34ac
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck 2522146c239ceea1de0c5bc7d76281d1235d688c
- lua_resty_websocket 423e41c1d54f4b2548740ab31afff62fca8f3bd7
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 6cd01e51ca695973a297b0cda8d365640132b843
- lua_resty_session 79e0427a53571ce18c3b4c7abb36ad9bb854053f
- lua_resty_jwt 425261aa15ea06a9dfbc6ebc57996348d71cbf14
- lua_resty_hmac 79a49299f9dc7907320a0f0d2dbb63dc16ce80fe
- lua_resty_http 41b2e822ce5c19f64e293b7dc2d5d244e511615d
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth da3910bb720bb8b01c86f8b37b66797752d1f20e
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib ae5f73508085e7ecce043f86342336400bf45a7c
- SLAXML 108970cbcb4370365e79c619b0f06099c9ec9754
- ngx_http_geoip2_module 5a83b6f958c67ea88d2899d0b3c2a5db8e36b211
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230

* Wed Dec 25 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.7-1
- 1.17.7
- echo_nginx_module 83e9fbbbcf7599fd81b4e1c3edd2d48df0430235
- headers_more_nginx_module 552e216a0da95c685d9db4f43e209c3f2a803e49
- lua_nginx_module 760f7073da87da23bb4f024943089edfad35c72e
- lua_upstream_nginx_module 6080f51f2a76b8ce5ee11e6e799442c0284fc442
- memc_nginx_module 32124a5454238ca5ae78a8df9298445293e8d73c
- redis2_nginx_module 15b0c454c987599689c369c2dd4ef07f3d2bcaca
- set_misc_nginx_module b28f23335a8c0020f3b189275af5f6ae11c4cd59
- srcache_nginx_module daaa062237821177cf666c198162558f7deaad6d
- stream_lua_nginx_module c7ac2234ec7a26bdcd3b17cbb5314f17344f9f5c
- lua_resty_balancer 3807cd5501f3702f0d24bdba465d98e32d29c219
- lua_resty_core 92d81d3d2520e2f3bc431044b4caae9f5993f86d
- lua_resty_dns 6b20b9d28c5efd5164919c9377fbeece2e86ce21
- lua_resty_lock 89017540b06d6548de90dac4d1c377fcaa53d449
- lua_resty_lrucache 1861b4a856102c94222628d103e801f476861377
- lua_resty_limit_traffic cf31eb4a71792589d5f647d9dc0e0de79fea3bf6
- lua_resty_memcached afa425d9377645f04cf808941d42af643cf05ec2
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 2c3ce08dda74be3d4b576372107214478efa3fae
- lua_resty_redis 9536180768854d76c278825a7980c47dce888812
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 70fe0ee9fe86fce462369da486b42a3ba6fee21c
- lua_resty_signal 93d23c96123da25e5d5eef4cf5fe13dbe5e4aea9
- lua_resty_string 595c5fd519fafa3af30002fd1ea5226d520a34ac
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck 2522146c239ceea1de0c5bc7d76281d1235d688c
- lua_resty_websocket 423e41c1d54f4b2548740ab31afff62fca8f3bd7
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 6cd01e51ca695973a297b0cda8d365640132b843
- lua_resty_session 79e0427a53571ce18c3b4c7abb36ad9bb854053f
- lua_resty_jwt 9b78d1c512ff8cd92bc402a1fac002b0c396a6d4
- lua_resty_hmac 79a49299f9dc7907320a0f0d2dbb63dc16ce80fe
- lua_resty_http 41b2e822ce5c19f64e293b7dc2d5d244e511615d
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth b7e2bc2a904c7d379cc83a31199f2877f7dd4c5e
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib ae5f73508085e7ecce043f86342336400bf45a7c
- SLAXML b7f376997e720d0deb7d0e1e4803c9f264c239de
- ngx_http_geoip2_module 5a83b6f958c67ea88d2899d0b3c2a5db8e36b211
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230

* Fri Dec 20 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.6-2
- OpenSSL 1.1.1d
- change to e98cuenc/ngx_upstream_jdomain
- ngx_upstream_jdomain a5a8e07f76cbe82b0792f8e3091e011c0c12f230

* Fri Nov 22 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.6-1
- 1.17.6
- echo_nginx_module 83e9fbbbcf7599fd81b4e1c3edd2d48df0430235
- headers_more_nginx_module 552e216a0da95c685d9db4f43e209c3f2a803e49
- lua_nginx_module a3ac3f557eed7efa3460d0870684f18d232adf5f
- lua_upstream_nginx_module 6080f51f2a76b8ce5ee11e6e799442c0284fc442
- memc_nginx_module 32124a5454238ca5ae78a8df9298445293e8d73c
- redis2_nginx_module 15b0c454c987599689c369c2dd4ef07f3d2bcaca
- set_misc_nginx_module b28f23335a8c0020f3b189275af5f6ae11c4cd59
- srcache_nginx_module daaa062237821177cf666c198162558f7deaad6d
- stream_lua_nginx_module c7ac2234ec7a26bdcd3b17cbb5314f17344f9f5c
- lua_resty_balancer 3807cd5501f3702f0d24bdba465d98e32d29c219
- lua_resty_core c0debd608f919b6df6a5976935c2891ac63d4aae
- lua_resty_dns 6b20b9d28c5efd5164919c9377fbeece2e86ce21
- lua_resty_lock 89017540b06d6548de90dac4d1c377fcaa53d449
- lua_resty_lrucache 1861b4a856102c94222628d103e801f476861377
- lua_resty_limit_traffic cf31eb4a71792589d5f647d9dc0e0de79fea3bf6
- lua_resty_memcached afa425d9377645f04cf808941d42af643cf05ec2
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 2c3ce08dda74be3d4b576372107214478efa3fae
- lua_resty_redis 9536180768854d76c278825a7980c47dce888812
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 70fe0ee9fe86fce462369da486b42a3ba6fee21c
- lua_resty_signal 93d23c96123da25e5d5eef4cf5fe13dbe5e4aea9
- lua_resty_string 595c5fd519fafa3af30002fd1ea5226d520a34ac
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck 2522146c239ceea1de0c5bc7d76281d1235d688c
- lua_resty_websocket 423e41c1d54f4b2548740ab31afff62fca8f3bd7
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 6cd01e51ca695973a297b0cda8d365640132b843
- lua_resty_session 6e5464668511d47d487e4de3e2788e2e92b43cde
- lua_resty_jwt 9b78d1c512ff8cd92bc402a1fac002b0c396a6d4
- lua_resty_hmac 79a49299f9dc7907320a0f0d2dbb63dc16ce80fe
- lua_resty_http 41b2e822ce5c19f64e293b7dc2d5d244e511615d
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth b7e2bc2a904c7d379cc83a31199f2877f7dd4c5e
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib ae5f73508085e7ecce043f86342336400bf45a7c
- SLAXML b7f376997e720d0deb7d0e1e4803c9f264c239de
- ngx_http_geoip2_module 5a83b6f958c67ea88d2899d0b3c2a5db8e36b211
- ngx_upstream_jdomain 1a92c677bd828fb41b88e0d87ca98995686a4e0a

* Wed Oct 23 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.5-1
- 1.17.5
- echo_nginx_module 83e9fbbbcf7599fd81b4e1c3edd2d48df0430235
- headers_more_nginx_module 552e216a0da95c685d9db4f43e209c3f2a803e49
- lua_nginx_module a3ac3f557eed7efa3460d0870684f18d232adf5f
- lua_upstream_nginx_module 6080f51f2a76b8ce5ee11e6e799442c0284fc442
- memc_nginx_module 32124a5454238ca5ae78a8df9298445293e8d73c
- redis2_nginx_module 15b0c454c987599689c369c2dd4ef07f3d2bcaca
- set_misc_nginx_module b28f23335a8c0020f3b189275af5f6ae11c4cd59
- srcache_nginx_module daaa062237821177cf666c198162558f7deaad6d
- stream_lua_nginx_module c7ac2234ec7a26bdcd3b17cbb5314f17344f9f5c
- lua_resty_balancer 3807cd5501f3702f0d24bdba465d98e32d29c219
- lua_resty_core c0debd608f919b6df6a5976935c2891ac63d4aae
- lua_resty_dns 6b20b9d28c5efd5164919c9377fbeece2e86ce21
- lua_resty_lock 89017540b06d6548de90dac4d1c377fcaa53d449
- lua_resty_lrucache 1861b4a856102c94222628d103e801f476861377
- lua_resty_limit_traffic cf31eb4a71792589d5f647d9dc0e0de79fea3bf6
- lua_resty_memcached afa425d9377645f04cf808941d42af643cf05ec2
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 2c3ce08dda74be3d4b576372107214478efa3fae
- lua_resty_redis 9536180768854d76c278825a7980c47dce888812
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 70fe0ee9fe86fce462369da486b42a3ba6fee21c
- lua_resty_signal 93d23c96123da25e5d5eef4cf5fe13dbe5e4aea9
- lua_resty_string 595c5fd519fafa3af30002fd1ea5226d520a34ac
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck 2522146c239ceea1de0c5bc7d76281d1235d688c
- lua_resty_websocket 423e41c1d54f4b2548740ab31afff62fca8f3bd7
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 6cd01e51ca695973a297b0cda8d365640132b843
- lua_resty_session 9302585bef154411d19362a484a605707670de8d
- lua_resty_jwt 9b78d1c512ff8cd92bc402a1fac002b0c396a6d4
- lua_resty_hmac 79a49299f9dc7907320a0f0d2dbb63dc16ce80fe
- lua_resty_http 41b2e822ce5c19f64e293b7dc2d5d244e511615d
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth 9aea2228947166039644e0841298045ff873d436
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib ae5f73508085e7ecce043f86342336400bf45a7c
- SLAXML b7f376997e720d0deb7d0e1e4803c9f264c239de
- ngx_http_geoip2_module a28ceffdeffb2b8ec2896bd1192a87f4f2c7a12a
- ngx_upstream_jdomain 1a92c677bd828fb41b88e0d87ca98995686a4e0a

* Wed Sep 25 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.4-1
- 1.17.4
- echo_nginx_module 2b3b256234d9966470d5441a0c743d9c5693607e
- headers_more_nginx_module 380e994d31284f6f450f9b00f464782467ee567c
- lua_nginx_module 69780f676900fb861cc4fa116e6dbe28d805da74
- lua_upstream_nginx_module 0ddfba570fbce0e9a1374dba9e8fa35c7c1741c3
- memc_nginx_module 9a2f32f6fd39acd860bef903ad8811d0fb5d89b4
- redis2_nginx_module 82ee1c2891d9455908219e8dd2d57f187f8878f2
- set_misc_nginx_module 048e9e05dbbc83ae4a0ea9c739397a8be2c4399a
- srcache_nginx_module f158163a065e21d7d3097d61a244208ac2850167
- stream_lua_nginx_module bfc9b27f2cef743b78d8fa6cf75f4d4e54b9f8d4
- lua_resty_balancer 3807cd5501f3702f0d24bdba465d98e32d29c219
- lua_resty_core e3f3fad22b086f5079e2ca2cea0fa21a2634a355
- lua_resty_dns 38f0c931e775f2a536c2d1150f7e942bd64d706d
- lua_resty_lock d14b2b0a2aeeca6f6a81f59020265933123aa635
- lua_resty_lrucache 2c1327a9d7e6c6b482552da443952c5a142c1178
- lua_resty_limit_traffic 31fb4b0277e45c4ddbab1c65bc4eae57b9f35983
- lua_resty_memcached 0f4052a649f66bb231e24989a7776d4adfeda28d
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 68f4841ab6e6ea197c1de002bed435f90ae7cab6
- lua_resty_redis 8a9147eba2842bd02f56f1ccdec156fda20049fa
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 683869f21540aac01bb84e164ab86090ba16e790
- lua_resty_signal 2495446a928aa0179923d08d1ab7eb736c822e66
- lua_resty_string 151cae6dc0619406c0a71921f23175db5f64e5a1
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck e36656b8604fcdcc7c0f3501428e751a1fa505df
- lua_resty_websocket 888000e7278025d6ac28050d48f7ae96062bbdc4
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 26ce9cc32212e4d1a4dbc16cb989687a15064b5a
- lua_resty_session a9a88648f4282104fc00bc8a067ab98cbfb16bf8
- lua_resty_jwt 9b78d1c512ff8cd92bc402a1fac002b0c396a6d4
- lua_resty_hmac 79a49299f9dc7907320a0f0d2dbb63dc16ce80fe
- lua_resty_http 41b2e822ce5c19f64e293b7dc2d5d244e511615d
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth 8384aaf427b985120251b142eccb8386bb78253f
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib ae5f73508085e7ecce043f86342336400bf45a7c
- SLAXML b7f376997e720d0deb7d0e1e4803c9f264c239de
- ngx_http_geoip2_module a28ceffdeffb2b8ec2896bd1192a87f4f2c7a12a
- ngx_upstream_jdomain 1a92c677bd828fb41b88e0d87ca98995686a4e0a

* Wed Sep 11 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.3-5
- OpenSSL 1.0.2t

* Wed Sep  4 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.3-4
- Fix nginx-1.17.3-cache_manager.patch

* Wed Sep  4 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.3-3
- Add nginx-1.17.3-cache_manager.patch

* Mon Sep  2 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.3-2
- Add ngx_http_geoip2_module and ngx_upstream_jdomain
- Update other modules
- echo_nginx_module 2b3b256234d9966470d5441a0c743d9c5693607e
- headers_more_nginx_module 380e994d31284f6f450f9b00f464782467ee567c
- lua_nginx_module fd1e0f89e495bcec9e930cb8c3525e953baa6f4a
- lua_upstream_nginx_module 0ddfba570fbce0e9a1374dba9e8fa35c7c1741c3
- memc_nginx_module 9a2f32f6fd39acd860bef903ad8811d0fb5d89b4
- redis2_nginx_module 82ee1c2891d9455908219e8dd2d57f187f8878f2
- set_misc_nginx_module 048e9e05dbbc83ae4a0ea9c739397a8be2c4399a
- srcache_nginx_module f158163a065e21d7d3097d61a244208ac2850167
- stream_lua_nginx_module 87a7ebae9f1f44b9431354566d357e0a38d48e8d
- lua_resty_balancer 3807cd5501f3702f0d24bdba465d98e32d29c219
- lua_resty_core 1985bf8a343339e6879fcadbc08481b25d8fc4ae
- lua_resty_dns 38f0c931e775f2a536c2d1150f7e942bd64d706d
- lua_resty_lock d14b2b0a2aeeca6f6a81f59020265933123aa635
- lua_resty_lrucache 2c1327a9d7e6c6b482552da443952c5a142c1178
- lua_resty_limit_traffic 31fb4b0277e45c4ddbab1c65bc4eae57b9f35983
- lua_resty_memcached 0f4052a649f66bb231e24989a7776d4adfeda28d
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 68f4841ab6e6ea197c1de002bed435f90ae7cab6
- lua_resty_redis 8a9147eba2842bd02f56f1ccdec156fda20049fa
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 683869f21540aac01bb84e164ab86090ba16e790
- lua_resty_signal 2495446a928aa0179923d08d1ab7eb736c822e66
- lua_resty_string 151cae6dc0619406c0a71921f23175db5f64e5a1
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck e36656b8604fcdcc7c0f3501428e751a1fa505df
- lua_resty_websocket 888000e7278025d6ac28050d48f7ae96062bbdc4
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 26ce9cc32212e4d1a4dbc16cb989687a15064b5a
- lua_resty_session a9a88648f4282104fc00bc8a067ab98cbfb16bf8
- lua_resty_jwt 42146446bbd2915850d4bb4636b2582b4ca71878
- lua_resty_hmac 79a49299f9dc7907320a0f0d2dbb63dc16ce80fe
- lua_resty_http 41b2e822ce5c19f64e293b7dc2d5d244e511615d
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth fb37ea03dca8a37882ca6a273db355f705103300
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib ae5f73508085e7ecce043f86342336400bf45a7c
- SLAXML b7f376997e720d0deb7d0e1e4803c9f264c239de
- ngx_http_geoip2_module a28ceffdeffb2b8ec2896bd1192a87f4f2c7a12a
- ngx_upstream_jdomain 1a92c677bd828fb41b88e0d87ca98995686a4e0a

* Wed Aug 14 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.3-1
- 1.17.3
- Add more lua-resty-* modules
- echo_nginx_module 2b3b256234d9966470d5441a0c743d9c5693607e
- headers_more_nginx_module 380e994d31284f6f450f9b00f464782467ee567c
- lua_nginx_module 2a190736a58674086c3a27bf71a7993383fffb55
- lua_upstream_nginx_module 0ddfba570fbce0e9a1374dba9e8fa35c7c1741c3
- memc_nginx_module 9a2f32f6fd39acd860bef903ad8811d0fb5d89b4
- redis2_nginx_module 82ee1c2891d9455908219e8dd2d57f187f8878f2
- set_misc_nginx_module 048e9e05dbbc83ae4a0ea9c739397a8be2c4399a
- srcache_nginx_module f158163a065e21d7d3097d61a244208ac2850167
- stream_lua_nginx_module 72e93064c7b124b159c63bdc88e5defc28813190
- lua_resty_balancer 3807cd5501f3702f0d24bdba465d98e32d29c219
- lua_resty_core 4b0dd534b7f8a271bd8757a38a418d3c7eb101f2
- lua_resty_dns 38f0c931e775f2a536c2d1150f7e942bd64d706d
- lua_resty_lock d14b2b0a2aeeca6f6a81f59020265933123aa635
- lua_resty_lrucache d8e0162c349e4ca7d10c8ca9ff7bf5b945cc41c9
- lua_resty_limit_traffic 31fb4b0277e45c4ddbab1c65bc4eae57b9f35983
- lua_resty_memcached 0f4052a649f66bb231e24989a7776d4adfeda28d
- lua_resty_memcached_shdict 32374a1a286506cf4cf9c18a8c1bf01bd1554c21
- lua_resty_mysql 68f4841ab6e6ea197c1de002bed435f90ae7cab6
- lua_resty_redis 12b10ccb38125e80b38c0b8ad56828bec41e9229
- lua_resty_shdict_simple 4d27246b16f86de49e6da8b8a6136cddfe7550b4
- lua_resty_shell 683869f21540aac01bb84e164ab86090ba16e790
- lua_resty_signal 2495446a928aa0179923d08d1ab7eb736c822e66
- lua_resty_string 151cae6dc0619406c0a71921f23175db5f64e5a1
- lua_resty_upload 8f4f0f8cb1edc97fb39c16d256968e5b1a18f9ea
- lua_resty_upstream_healthcheck e36656b8604fcdcc7c0f3501428e751a1fa505df
- lua_resty_websocket 888000e7278025d6ac28050d48f7ae96062bbdc4
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 26ce9cc32212e4d1a4dbc16cb989687a15064b5a
- lua_resty_session a9a88648f4282104fc00bc8a067ab98cbfb16bf8
- lua_resty_jwt 42146446bbd2915850d4bb4636b2582b4ca71878
- lua_resty_hmac 79a49299f9dc7907320a0f0d2dbb63dc16ce80fe
- lua_resty_http 41b2e822ce5c19f64e293b7dc2d5d244e511615d
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth d9fe8e54a43503953ad1cff26ce64c0752033a74
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib ae5f73508085e7ecce043f86342336400bf45a7c
- SLAXML b7f376997e720d0deb7d0e1e4803c9f264c239de

* Wed Jun 26 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.17.1-1
- 1.17.1
- echo_nginx_module 1574088dbf6c0a21c4e273bc69febcdd441528e5
- headers_more_nginx_module 085fbbc28fe5d7bd61bc7cd8d1355e73abc296ea
- lua_nginx_module 32dd6a34a17d6f1f094552a45c204ef614f5fbb5
- lua_upstream_nginx_module 6266791641050937c8fccdf25115c8e48a062870
- memc_nginx_module 133aac6cca0c9228062924cd1770a2408af515a2
- redis2_nginx_module a0b4cf012b27ba0d9a55fe17af18f154e49b7dae
- set_misc_nginx_module bcfa7a6d0d0fca4dac57d5b45e6064c6fa7f1cae
- srcache_nginx_module b6a7aeb1653d2846da7d139fd6e717ca49b3a9a6
- lua_resty_core 6d99c245229dc2692f78db4f89760e927a16157a
- stream_lua_nginx_module b56659832f54558b985c0ff53c2c0f4316fea576
- lua_resty_string fbf93a478754dafcc2d86dcd79d5e3e18bcc41e0
- lua_resty_lrucache 22c6c6e8eb17438157abed327bc8b76f3fcbb890
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 88e5447d66351da5815131cf7e71aa325e3626f7
- lua_resty_session 0b18efa72deb3798c7f05d4669e11ad23646d17a
- lua_resty_jwt f17d7c6ed45d59beb9fbf3bd5f50e89ead395b98
- lua_resty_hmac 989f601acbe74dee71c1a48f3e140a427f2d03ae
- lua_resty_http 23053ba93117116de2e50749c7a448e6e840914b
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth 14d92fdde64fa1ad746fa0bf6db68a8dbe761a75
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib ae5f73508085e7ecce043f86342336400bf45a7c
- SLAXML b7f376997e720d0deb7d0e1e4803c9f264c239de

* Thu Apr 18 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.12-1
- 1.15.12
- echo_nginx_module 866bab2da7ef2f7296ccf5640f119cb062f9a3ab
- headers_more_nginx_module 085fbbc28fe5d7bd61bc7cd8d1355e73abc296ea
- lua_nginx_module 61e4d0aac8974b8fad1b5b93d0d3d694d257d328
- lua_upstream_nginx_module 6e31bed3220b3083c6029f9f7043ab3651b23f78
- memc_nginx_module 133aac6cca0c9228062924cd1770a2408af515a2
- redis2_nginx_module a0b4cf012b27ba0d9a55fe17af18f154e49b7dae
- set_misc_nginx_module bcfa7a6d0d0fca4dac57d5b45e6064c6fa7f1cae
- srcache_nginx_module b6a7aeb1653d2846da7d139fd6e717ca49b3a9a6
- lua_resty_core 7a735eaf34ae1dddf853fdf10a9616af07da3517
- stream_lua_nginx_module 84507348cc01590542d0a3b7c1181600427776f4
- lua_resty_string f9d23cf95861815b1125472c7415297e8226c9f2
- lua_resty_lrucache 22c6c6e8eb17438157abed327bc8b76f3fcbb890
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc b8277e232099c1aeef439da31886222bca0db28b
- lua_resty_session 0b18efa72deb3798c7f05d4669e11ad23646d17a
- lua_resty_jwt f17d7c6ed45d59beb9fbf3bd5f50e89ead395b98
- lua_resty_hmac 989f601acbe74dee71c1a48f3e140a427f2d03ae
- lua_resty_http f71e9708a3fd0ff4179d4b0d770c91fcf98d0042
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth 284935267e1ed53968c0beef8201723770d46456
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib 3d6dbee710b4712b8d0e0235425abee04a22b1bd
- SLAXML b7f376997e720d0deb7d0e1e4803c9f264c239de

* Wed Mar 27 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.10-1
- 1.15.10
- echo_nginx_module 32859fce2a36b2f6b8c13569f6d21e05a55674cd
- headers_more_nginx_module 085fbbc28fe5d7bd61bc7cd8d1355e73abc296ea
- lua_nginx_module 12d991e182ec0e742b200405b65150cba8659e3d
- lua_upstream_nginx_module 6e31bed3220b3083c6029f9f7043ab3651b23f78
- memc_nginx_module 133aac6cca0c9228062924cd1770a2408af515a2
- redis2_nginx_module a0b4cf012b27ba0d9a55fe17af18f154e49b7dae
- set_misc_nginx_module bcfa7a6d0d0fca4dac57d5b45e6064c6fa7f1cae
- srcache_nginx_module b6a7aeb1653d2846da7d139fd6e717ca49b3a9a6
- lua_resty_core 678a65ba1426e15d0edfefe18359af377930f37a
- stream_lua_nginx_module ef7731eb2f2abcdd82693cd5eadd5459c8c793fe
- lua_resty_string f9d23cf95861815b1125472c7415297e8226c9f2
- lua_resty_lrucache a120a0ca46bf05962efaef99f83aff125cf4a77b
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc b8277e232099c1aeef439da31886222bca0db28b
- lua_resty_session 0b18efa72deb3798c7f05d4669e11ad23646d17a
- lua_resty_jwt f17d7c6ed45d59beb9fbf3bd5f50e89ead395b98
- lua_resty_hmac 989f601acbe74dee71c1a48f3e140a427f2d03ae
- lua_resty_http f71e9708a3fd0ff4179d4b0d770c91fcf98d0042
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth 92930a4091fbb0b261814cba4a0853dc75603f0f
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib 3d6dbee710b4712b8d0e0235425abee04a22b1bd
- SLAXML b7f376997e720d0deb7d0e1e4803c9f264c239de

* Wed Feb 27 2019 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.9-1
- 1.15.9
- OpenSSL 1.0.2r
- echo_nginx_module 32859fce2a36b2f6b8c13569f6d21e05a55674cd
- headers_more_nginx_module 085fbbc28fe5d7bd61bc7cd8d1355e73abc296ea
- lua_nginx_module 83ca6b57ae5ede2b9ff987babff323e5814cebaf
- lua_upstream_nginx_module 6e31bed3220b3083c6029f9f7043ab3651b23f78
- memc_nginx_module 133aac6cca0c9228062924cd1770a2408af515a2
- redis2_nginx_module a0b4cf012b27ba0d9a55fe17af18f154e49b7dae
- set_misc_nginx_module bcfa7a6d0d0fca4dac57d5b45e6064c6fa7f1cae
- srcache_nginx_module b6a7aeb1653d2846da7d139fd6e717ca49b3a9a6
- lua_resty_core d36c977ac72ca2af75c48bca197d2268b49c1611
- stream_lua_nginx_module ef7731eb2f2abcdd82693cd5eadd5459c8c793fe
- lua_resty_string f9d23cf95861815b1125472c7415297e8226c9f2
- lua_resty_lrucache a120a0ca46bf05962efaef99f83aff125cf4a77b
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 4fbfd9b4c4bbd94900ded89839b8afa636ff8af8
- lua_resty_session 0b18efa72deb3798c7f05d4669e11ad23646d17a
- lua_resty_jwt f17d7c6ed45d59beb9fbf3bd5f50e89ead395b98
- lua_resty_hmac 989f601acbe74dee71c1a48f3e140a427f2d03ae
- lua_resty_http f71e9708a3fd0ff4179d4b0d770c91fcf98d0042
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module f5e30888a256136d9c550bf1ada77d6ea78a48af
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth 92930a4091fbb0b261814cba4a0853dc75603f0f
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib 3d6dbee710b4712b8d0e0235425abee04a22b1bd
- SLAXML b7f376997e720d0deb7d0e1e4803c9f264c239de

* Fri Nov 30 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.7-1
- 1.15.7
- OpenSSL 1.0.2q
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module ec0d5768b25044cda99e35ce3413f82c21d4aac1
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module bcfa7a6d0d0fca4dac57d5b45e6064c6fa7f1cae
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core c193534071f4f2e8335839961728e51c7c248d6a
- stream_lua_nginx_module 88bec0b375b88224f438f2435648a6c5f44bc6b9
- lua_resty_string 945b7d67422e8ceb6013cf84d8603c47713a8a02
- lua_resty_lrucache d02dddc97953864eed537246f57aa8f537782ef9
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 7e0cebd13def44cc39e433c5a86db8e9cf70fa3c
- lua_resty_session 4429a06ffac1724a056fafa954c0394d437b261f
- lua_resty_jwt f17d7c6ed45d59beb9fbf3bd5f50e89ead395b98
- lua_resty_hmac 989f601acbe74dee71c1a48f3e140a427f2d03ae
- lua_resty_http e5deba5bde1db31adc7aad574bae5e89f83fd973
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth 9fddcf9e5a71ffb65376af18ad4435194b473487
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib 3d6dbee710b4712b8d0e0235425abee04a22b1bd
- SLAXML b7f376997e720d0deb7d0e1e4803c9f264c239de

* Wed Nov  7 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.6-1
- 1.15.6
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module 08a9baa92b64ac06d2c82d1af25298fc36f46264
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module bcfa7a6d0d0fca4dac57d5b45e6064c6fa7f1cae
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core d2c6e28b4d4021602b800a835dc6bbaad4cc3d89
- stream_lua_nginx_module eacdfa39184a5a5ea28bd15b3baf49b2c3fed23b
- lua_resty_string bfc33982f37cb57748e94e204a6187d41263ac0e
- lua_resty_lrucache d02dddc97953864eed537246f57aa8f537782ef9
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 2879b4395bbfebb7390038a044f59fdf817d969a
- lua_resty_session 4429a06ffac1724a056fafa954c0394d437b261f
- lua_resty_jwt f17d7c6ed45d59beb9fbf3bd5f50e89ead395b98
- lua_resty_hmac 989f601acbe74dee71c1a48f3e140a427f2d03ae
- lua_resty_http e5deba5bde1db31adc7aad574bae5e89f83fd973
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 68b5f4b6553e1588c42d2cf021aa8b5f7bf268fb
- nginx_http_shibboleth d954cab13859f186862a38c32b7748760b947aa8
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib 3d6dbee710b4712b8d0e0235425abee04a22b1bd
- SLAXML b7f376997e720d0deb7d0e1e4803c9f264c239de

* Thu Oct  4 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.5-1
- 1.15.5
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module f64ec8c9056437bb1b822fc4e99f05f784d36e32
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module aac9afe4c42d96e35d496994c552839799010255
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core bdbac701eb017370775f7333979922041021aeee
- stream_lua_nginx_module e3eb228c08e5bab30404d5d715bd9b5a545f68a8
- lua_resty_string 2ac7c3bdba55e06bbfd8d76aa981611ffb2cb321
- lua_resty_lrucache edaafeb0c2be6b2835911a3e38a5e4152d6a0d98
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 06bfae9f1e55aa7328f33d5230e807e2498315e8
- lua_resty_session 4429a06ffac1724a056fafa954c0394d437b261f
- lua_resty_jwt f17d7c6ed45d59beb9fbf3bd5f50e89ead395b98
- lua_resty_hmac 989f601acbe74dee71c1a48f3e140a427f2d03ae
- lua_resty_http e5deba5bde1db31adc7aad574bae5e89f83fd973
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5
- nginx_http_shibboleth d954cab13859f186862a38c32b7748760b947aa8
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib 3d6dbee710b4712b8d0e0235425abee04a22b1bd
- SLAXML 8bfc922c6ed14f89548d7bbc2401ce35d7d92749

* Wed Sep 12 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.3-3
- Add jkeys089/lua-resty-hmac
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module e94f2e5d64daa45ff396e262d8dab8e56f5f10e0
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module aac9afe4c42d96e35d496994c552839799010255
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core bdbac701eb017370775f7333979922041021aeee
- stream_lua_nginx_module e3eb228c08e5bab30404d5d715bd9b5a545f68a8
- lua_resty_string 2ac7c3bdba55e06bbfd8d76aa981611ffb2cb321
- lua_resty_lrucache edaafeb0c2be6b2835911a3e38a5e4152d6a0d98
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 40ed435505b307b4d7046766b1f3ad7e0127c498
- lua_resty_session 4429a06ffac1724a056fafa954c0394d437b261f
- lua_resty_jwt f17d7c6ed45d59beb9fbf3bd5f50e89ead395b98
- lua_resty_hmac 989f601acbe74dee71c1a48f3e140a427f2d03ae
- lua_resty_http e5deba5bde1db31adc7aad574bae5e89f83fd973
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5
- nginx_http_shibboleth d954cab13859f186862a38c32b7748760b947aa8
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib 3d6dbee710b4712b8d0e0235425abee04a22b1bd
- SLAXML 8bfc922c6ed14f89548d7bbc2401ce35d7d92749

* Fri Sep  7 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.3-2
- Add zmartzone/lua-resty-openidc and dependencies
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module e94f2e5d64daa45ff396e262d8dab8e56f5f10e0
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module aac9afe4c42d96e35d496994c552839799010255
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core bdbac701eb017370775f7333979922041021aeee
- stream_lua_nginx_module e3eb228c08e5bab30404d5d715bd9b5a545f68a8
- lua_resty_string 2ac7c3bdba55e06bbfd8d76aa981611ffb2cb321
- lua_resty_lrucache edaafeb0c2be6b2835911a3e38a5e4152d6a0d98
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_openidc 40ed435505b307b4d7046766b1f3ad7e0127c498
- lua_resty_session 4429a06ffac1724a056fafa954c0394d437b261f
- lua_resty_jwt f17d7c6ed45d59beb9fbf3bd5f50e89ead395b98
- lua_resty_http e5deba5bde1db31adc7aad574bae5e89f83fd973
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5
- nginx_http_shibboleth d954cab13859f186862a38c32b7748760b947aa8
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib 3d6dbee710b4712b8d0e0235425abee04a22b1bd
- SLAXML 8bfc922c6ed14f89548d7bbc2401ce35d7d92749

* Wed Aug 29 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.3-1
- 1.15.2
- OpenSSL 1.0.2p
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module e94f2e5d64daa45ff396e262d8dab8e56f5f10e0
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module aac9afe4c42d96e35d496994c552839799010255
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core bdbac701eb017370775f7333979922041021aeee
- stream_lua_nginx_module e3eb228c08e5bab30404d5d715bd9b5a545f68a8
- lua_resty_string 2ac7c3bdba55e06bbfd8d76aa981611ffb2cb321
- lua_resty_lrucache edaafeb0c2be6b2835911a3e38a5e4152d6a0d98
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_http fe5c10a47cf40440845c140a5d29cd0e0cd0208f
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5
- nginx_http_shibboleth d954cab13859f186862a38c32b7748760b947aa8
- nginx_lua_saml_service_provider 90b79233bfc28dd48ad8f2d38a8d547d182f1a62
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib 3d6dbee710b4712b8d0e0235425abee04a22b1bd
- SLAXML 8bfc922c6ed14f89548d7bbc2401ce35d7d92749

* Mon Jul 30 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.2-2
- Add my SAML service provider and dependencies
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module e94f2e5d64daa45ff396e262d8dab8e56f5f10e0
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module aac9afe4c42d96e35d496994c552839799010255
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core bdbac701eb017370775f7333979922041021aeee
- stream_lua_nginx_module e3eb228c08e5bab30404d5d715bd9b5a545f68a8
- lua_resty_string 2ac7c3bdba55e06bbfd8d76aa981611ffb2cb321
- lua_resty_lrucache edaafeb0c2be6b2835911a3e38a5e4152d6a0d98
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_http 75e30060863d41df47c95a5b54e1458954e98792
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5
- nginx_http_shibboleth b441df08887fc10e44cc047da2a188014a0dadf5
- nginx_lua_saml_service_provider 391490b399187e3648f6d796ba6141a00be2f8fc
- nginx_lua_session 00cfbbf018c6b8b74614e6fe3dc350b29a5c6ae8
- lua_ffi_zlib 3d6dbee710b4712b8d0e0235425abee04a22b1bd
- SLAXML 8bfc922c6ed14f89548d7bbc2401ce35d7d92749

* Wed Jul 11 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.2-1
- 1.15.2
- Install debug build modules to %{_libdir}/nginx/modules-debug
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module e94f2e5d64daa45ff396e262d8dab8e56f5f10e0
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module aac9afe4c42d96e35d496994c552839799010255
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core bdbac701eb017370775f7333979922041021aeee
- stream_lua_nginx_module e3eb228c08e5bab30404d5d715bd9b5a545f68a8
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_http 75e30060863d41df47c95a5b54e1458954e98792
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5
- nginx_http_shibboleth b441df08887fc10e44cc047da2a188014a0dadf5

* Wed Jul 11 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.1-2
- Add pintsized/lua-resty-http
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module 576a10d246daf81c0ce1b959c50ee807769c01a8
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module aac9afe4c42d96e35d496994c552839799010255
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core 1d5c898e3574d7c38ef2d8d905e8481f9cfd5aaa
- stream_lua_nginx_module e3eb228c08e5bab30404d5d715bd9b5a545f68a8
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- lua_resty_http 0e8ac2dc767447f48ec964ba3901caa8dfb3ec06
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5
- nginx_http_shibboleth b441df08887fc10e44cc047da2a188014a0dadf5

* Wed Jul  4 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.1-1
- 1.15.1
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module 576a10d246daf81c0ce1b959c50ee807769c01a8
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module aac9afe4c42d96e35d496994c552839799010255
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core 1d5c898e3574d7c38ef2d8d905e8481f9cfd5aaa
- stream_lua_nginx_module e3eb228c08e5bab30404d5d715bd9b5a545f68a8
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5
- nginx_http_shibboleth b441df08887fc10e44cc047da2a188014a0dadf5

* Fri Jun 29 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.0-3
- Include shib_fastcgi_params and shib_clear_headers
  from nginx_http_shibboleth module.
- Add lua-resty-cookie lua file.
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module 576a10d246daf81c0ce1b959c50ee807769c01a8
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module aac9afe4c42d96e35d496994c552839799010255
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core 1d5c898e3574d7c38ef2d8d905e8481f9cfd5aaa
- stream_lua_nginx_module e3eb228c08e5bab30404d5d715bd9b5a545f68a8
- lua_resty_cookie 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5
- nginx_http_shibboleth b441df08887fc10e44cc047da2a188014a0dadf5

* Wed Jun 27 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.0-2
- Add github.com/nginx-shib/nginx-http-shibboleth module
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module 576a10d246daf81c0ce1b959c50ee807769c01a8
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module aac9afe4c42d96e35d496994c552839799010255
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core 1d5c898e3574d7c38ef2d8d905e8481f9cfd5aaa
- stream_lua_nginx_module e3eb228c08e5bab30404d5d715bd9b5a545f68a8
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5
- nginx_http_shibboleth b441df08887fc10e44cc047da2a188014a0dadf5

* Wed Jun  6 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.0-1
- 1.15.0
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module 55743aeba3075b34a250380b32bad6366eae6c30
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
- redis2_nginx_module c989c829a2877132cb100f901e320921250e068d
- set_misc_nginx_module aac9afe4c42d96e35d496994c552839799010255
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core 2e8b0450775ef1d066ef14eda495817614a4427d
- stream_lua_nginx_module 87863ca2bfb35219ecea43c2c14a15e6c882a036
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module b58a4500db3c4ee274be54a18abc767219dcfd36
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5

* Thu Apr  5 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.11-1
- 1.13.11
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module 91a0ad236c9661f38b78cdc99e05025f7ce5cccb
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 66de925b7da5931badf24c7e675e2ee62c697069
- redis2_nginx_module 4b7ff9bdf669d487efd32ac3d06d3ee981f5a2f6
- set_misc_nginx_module 77ae35bfb00e81196d8dbae48c359e1d591a8d01
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core 6ea0dea70647a54c68ca02be47c3deb83b15a6ad
- stream_lua_nginx_module a9e856564ccae54a43f27d909ce9af80064f5688
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5

* Mon Apr  2 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.10-1
- 1.13.10
- OpenSSL Update to 1.0.2o
- echo_nginx_module c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
- lua_nginx_module 91a0ad236c9661f38b78cdc99e05025f7ce5cccb
- lua_upstream_nginx_module 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
- memc_nginx_module 66de925b7da5931badf24c7e675e2ee62c697069
- redis2_nginx_module 4b7ff9bdf669d487efd32ac3d06d3ee981f5a2f6
- set_misc_nginx_module 77ae35bfb00e81196d8dbae48c359e1d591a8d01
- srcache_nginx_module 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core 6ea0dea70647a54c68ca02be47c3deb83b15a6ad
- stream_lua_nginx_module a9e856564ccae54a43f27d909ce9af80064f5688
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module 2503d5ef853ff2542ee7e08d898a85a7747812e5

* Wed Feb 21 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.9-1
- 1.13.9
- echo_nginx_module_commit c65f5c638d0501b482fbc3ebbda9a49648022d40
- headers_more_nginx_module_commit 55fbdaba96be3d4e534201232f6b555f3415fbb9
- lua_nginx_module_commit 3cde1d8aa1887e8b76356013a24a7602440d283e
- lua_upstream_nginx_module_commit 9610123819cf324fcdad7b907187d5a4f70bb07a
- memc_nginx_module_commit 66de925b7da5931badf24c7e675e2ee62c697069
- redis2_nginx_module_commit 4b7ff9bdf669d487efd32ac3d06d3ee981f5a2f6
- set_misc_nginx_module_commit cda7e5086b56047f3f9d65b6339976f453e8f8f8
- srcache_nginx_module_commit 53a98806b0a24cc736d11003662e8b769c3e7eb3
- lua_resty_core_commit a0a404f6f14d615789012598c5a7f161f46cf40c
- stream_lua_nginx_module_commit d4757341ef2e5ec7faa4224c7830386f32bddd6a
- ngx_cache_purge_commit 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module_commit 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module_commit 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module_commit a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download_commit f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit_commit a22dade76c838e5f377d58d007f65d35b5ce1df3
- nginx_sorted_querystring_module_commit e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module_commit 2503d5ef853ff2542ee7e08d898a85a7747812e5

* Mon Jan 15 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.8-1
- 1.13.8
- echo_nginx_module_commit 7365fb01fd7c5630eeb298d43959a84fc629791a
- headers_more_nginx_module_commit 55fbdaba96be3d4e534201232f6b555f3415fbb9
- lua_nginx_module_commit d125123f8be3db55ab57bf0206ad086c9ff43934
- lua_upstream_nginx_module_commit 9610123819cf324fcdad7b907187d5a4f70bb07a
- memc_nginx_module_commit 1d8ef84616e13b64d6021b3ab0c24f40ea09f750
- redis2_nginx_module_commit 0402a28467b8532e7a892bbdb8213a7654f872b4
- set_misc_nginx_module_commit cda7e5086b56047f3f9d65b6339976f453e8f8f8
- srcache_nginx_module_commit b741f55e32b66120fbe380f203e4ed7e96235d1f
- stream_lua_nginx_module_commit 73bbadce5c32069d2d8fa690299dff85663fa5b2
- ngx_cache_purge_commit 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module_commit 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module_commit 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module_commit a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download_commit f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit_commit 3358655ea454bbbedda5ae65d77d95cad0e26772
- nginx_sorted_querystring_module_commit e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module_commit 2503d5ef853ff2542ee7e08d898a85a7747812e5

* Fri Dec  8 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.7-2
- OpenSSL 1.0.2n
- echo_nginx_module_commit 7365fb01fd7c5630eeb298d43959a84fc629791a
- headers_more_nginx_module_commit 55fbdaba96be3d4e534201232f6b555f3415fbb9
- lua_nginx_module_commit 18b5de576c13ed19f88ad3844c36776f23fbb61f
- lua_upstream_nginx_module_commit 9610123819cf324fcdad7b907187d5a4f70bb07a
- memc_nginx_module_commit 1d8ef84616e13b64d6021b3ab0c24f40ea09f750
- redis2_nginx_module_commit 0402a28467b8532e7a892bbdb8213a7654f872b4
- set_misc_nginx_module_commit 0112cf0bca7f2ce1c608ac692515204a254f942c
- srcache_nginx_module_commit b741f55e32b66120fbe380f203e4ed7e96235d1f
- stream_lua_nginx_module_commit 4557314ed4b2b2a993afb78c46504efbd9688b41
- ngx_cache_purge_commit 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module_commit 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module_commit 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module_commit a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download_commit f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit_commit 440cdb0cefc8132c99674eac9dc531ee5ba7ddb2
- nginx_sorted_querystring_module_commit e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module_commit 2503d5ef853ff2542ee7e08d898a85a7747812e5

* Mon Dec  4 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.7-1
- 1.13.7
- echo_nginx_module_commit 7365fb01fd7c5630eeb298d43959a84fc629791a
- headers_more_nginx_module_commit 55fbdaba96be3d4e534201232f6b555f3415fbb9
- lua_nginx_module_commit 18b5de576c13ed19f88ad3844c36776f23fbb61f
- lua_upstream_nginx_module_commit 9610123819cf324fcdad7b907187d5a4f70bb07a
- memc_nginx_module_commit 1d8ef84616e13b64d6021b3ab0c24f40ea09f750
- redis2_nginx_module_commit 0402a28467b8532e7a892bbdb8213a7654f872b4
- set_misc_nginx_module_commit 0112cf0bca7f2ce1c608ac692515204a254f942c
- srcache_nginx_module_commit b741f55e32b66120fbe380f203e4ed7e96235d1f
- stream_lua_nginx_module_commit 4557314ed4b2b2a993afb78c46504efbd9688b41
- ngx_cache_purge_commit 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module_commit 791b6136f02bc9613daf178723ac09f4df5a3bbf
- nginx_dav_ext_module_commit 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module_commit a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download_commit f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit_commit 440cdb0cefc8132c99674eac9dc531ee5ba7ddb2
- nginx_sorted_querystring_module_commit e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module_commit 2503d5ef853ff2542ee7e08d898a85a7747812e5

* Wed Nov  8 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.6-3
- 1.13.6
- OpenSSL 1.0.2m
- Add openresty/stream-lua-nginx-module since it is now neede by lua-nginx-module.
  https://github.com/openresty/lua-nginx-module/commit/7730490c1e98a5867da77dc72814fc896000a769
- Build stream as static module to pass build of stream-lua-nginx-module.
- echo_nginx_module_commit 7365fb01fd7c5630eeb298d43959a84fc629791a
- headers_more_nginx_module_commit 55fbdaba96be3d4e534201232f6b555f3415fbb9
- lua_nginx_module_commit b2aae31a85be4b51469ae8f7a128743e6e633b05
- lua_upstream_nginx_module_commit 9610123819cf324fcdad7b907187d5a4f70bb07a
- memc_nginx_module_commit 1d8ef84616e13b64d6021b3ab0c24f40ea09f750
- redis2_nginx_module_commit 0402a28467b8532e7a892bbdb8213a7654f872b4
- set_misc_nginx_module_commit 0112cf0bca7f2ce1c608ac692515204a254f942c
- srcache_nginx_module_commit b741f55e32b66120fbe380f203e4ed7e96235d1f
- stream_lua_nginx_module_commit 3c89e16cc8a29ef26bafc9a60a7c2c8f5ea5e30a
- ngx_cache_purge_commit 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module_commit 43f1e4209b7ee7b795595912943a8fdc37f2ea4a
- nginx_dav_ext_module_commit 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module_commit a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download_commit f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit_commit 440cdb0cefc8132c99674eac9dc531ee5ba7ddb2
- nginx_sorted_querystring_module_commit e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module_commit 2503d5ef853ff2542ee7e08d898a85a7747812e5

* Wed Oct 11 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.6-1
- 1.13.6
- Remove ngx_http_v2 patches
- echo_nginx_module_commit d95da3500ae992b703f90dea926877b728818104
- headers_more_nginx_module_commit d63cf91edcfa65a92eb0474d0d6fea7280abb0c6
- lua_nginx_module_commit 8dd4bdef6f78495bdc1a7cce92eed494a70cc0af
- lua_upstream_nginx_module_commit a84fbbb3d3b07684c232f642eccbc5334bafcbfe
- memc_nginx_module_commit 31ba7ff6d53201f1afa0b6fff5d6233336168c83
- redis2_nginx_module_commit 5ae5a74b0ac205638805a2f6f48bb1d70b1c7038
- set_misc_nginx_module_commit 48908343c00a45a40365158282f61d5369d17194
- srcache_nginx_module_commit af82f755b8a92765fff0b3e70b26bedf4bbacadc
- ngx_cache_purge_commit 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module_commit 43f1e4209b7ee7b795595912943a8fdc37f2ea4a
- nginx_dav_ext_module_commit 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module_commit a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download_commit f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit_commit 440cdb0cefc8132c99674eac9dc531ee5ba7ddb2
- nginx_sorted_querystring_module_commit e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module_commit 2503d5ef853ff2542ee7e08d898a85a7747812e5

* Sun Oct  8 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.5-4
- Add lua-resty-core
- echo_nginx_module_commit d95da3500ae992b703f90dea926877b728818104
- headers_more_nginx_module_commit d63cf91edcfa65a92eb0474d0d6fea7280abb0c6
- lua_nginx_module_commit f829065b794025c856c9f86d469395e464e782ed
- lua_upstream_nginx_module_commit a84fbbb3d3b07684c232f642eccbc5334bafcbfe
- memc_nginx_module_commit 31ba7ff6d53201f1afa0b6fff5d6233336168c83
- redis2_nginx_module_commit 5ae5a74b0ac205638805a2f6f48bb1d70b1c7038
- set_misc_nginx_module_commit 48908343c00a45a40365158282f61d5369d17194
- srcache_nginx_module_commit af82f755b8a92765fff0b3e70b26bedf4bbacadc
- lua_resty_core_commit 3343ea159201da764e9a0f78f0857e5e7be11cf2
- ngx_cache_purge_commit 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module_commit 43f1e4209b7ee7b795595912943a8fdc37f2ea4a
- nginx_dav_ext_module_commit 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module_commit a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download_commit f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit_commit 440cdb0cefc8132c99674eac9dc531ee5ba7ddb2
- nginx_sorted_querystring_module_commit e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module_commit 2503d5ef853ff2542ee7e08d898a85a7747812e5

* Sun Oct  8 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.5-3
- echo_nginx_module_commit d95da3500ae992b703f90dea926877b728818104
- headers_more_nginx_module_commit d63cf91edcfa65a92eb0474d0d6fea7280abb0c6
- lua_nginx_module_commit f829065b794025c856c9f86d469395e464e782ed
- lua_upstream_nginx_module_commit a84fbbb3d3b07684c232f642eccbc5334bafcbfe
- memc_nginx_module_commit 31ba7ff6d53201f1afa0b6fff5d6233336168c83
- redis2_nginx_module_commit 5ae5a74b0ac205638805a2f6f48bb1d70b1c7038
- set_misc_nginx_module_commit 48908343c00a45a40365158282f61d5369d17194
- srcache_nginx_module_commit af82f755b8a92765fff0b3e70b26bedf4bbacadc
- ngx_cache_purge_commit 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module_commit 43f1e4209b7ee7b795595912943a8fdc37f2ea4a
- nginx_dav_ext_module_commit 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module_commit a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download_commit f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit_commit 440cdb0cefc8132c99674eac9dc531ee5ba7ddb2
- nginx_sorted_querystring_module_commit e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module_commit 2503d5ef853ff2542ee7e08d898a85a7747812e5

* Mon Sep 11 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.5-2
- Add ngx_http_pipelog_module_commit
- echo_nginx_module_commit d95da3500ae992b703f90dea926877b728818104
- headers_more_nginx_module_commit 7b0762aba64495e289c3f9cd7f0bd74d0051a980
- lua_nginx_module_commit 36d6ef406b98c63f2f47d1deb790fc8f32615e0f
- lua_upstream_nginx_module_commit a84fbbb3d3b07684c232f642eccbc5334bafcbfe
- memc_nginx_module_commit 31ba7ff6d53201f1afa0b6fff5d6233336168c83
- redis2_nginx_module_commit 5ae5a74b0ac205638805a2f6f48bb1d70b1c7038
- set_misc_nginx_module_commit 48908343c00a45a40365158282f61d5369d17194
- srcache_nginx_module_commit af82f755b8a92765fff0b3e70b26bedf4bbacadc
- ngx_cache_purge_commit 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module_commit 43f1e4209b7ee7b795595912943a8fdc37f2ea4a
- nginx_dav_ext_module_commit 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module_commit a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download_commit f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit_commit 440cdb0cefc8132c99674eac9dc531ee5ba7ddb2
- nginx_sorted_querystring_module_commit e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- ngx_http_pipelog_module_commit 2503d5ef853ff2542ee7e08d898a85a7747812e5

* Sun Sep 10 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.5-1
- 1.13.5
- echo_nginx_module_commit d95da3500ae992b703f90dea926877b728818104
- headers_more_nginx_module_commit 7b0762aba64495e289c3f9cd7f0bd74d0051a980
- lua_nginx_module_commit 36d6ef406b98c63f2f47d1deb790fc8f32615e0f
- lua_upstream_nginx_module_commit a84fbbb3d3b07684c232f642eccbc5334bafcbfe
- memc_nginx_module_commit 31ba7ff6d53201f1afa0b6fff5d6233336168c83
- redis2_nginx_module_commit 5ae5a74b0ac205638805a2f6f48bb1d70b1c7038
- set_misc_nginx_module_commit 48908343c00a45a40365158282f61d5369d17194
- srcache_nginx_module_commit af82f755b8a92765fff0b3e70b26bedf4bbacadc
- ngx_cache_purge_commit 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module_commit 43f1e4209b7ee7b795595912943a8fdc37f2ea4a
- nginx_dav_ext_module_commit 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module_commit a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download_commit f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit_commit 440cdb0cefc8132c99674eac9dc531ee5ba7ddb2
- nginx_sorted_querystring_module_commit e5bbded07fd67e2977edc2bc145c45a7b3fc4d26

* Wed Aug  9 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.4-1
- 1.13.4
- echo_nginx_module d95da3500ae992b703f90dea926877b728818104
- headers_more_nginx_module 7b0762aba64495e289c3f9cd7f0bd74d0051a980
- lua_nginx_module cdd2ae921f67bf396c743406493127be496e57ce
- lua_upstream_nginx_module a84fbbb3d3b07684c232f642eccbc5334bafcbfe
- memc_nginx_module 31ba7ff6d53201f1afa0b6fff5d6233336168c83
- redis2_nginx_module 5ae5a74b0ac205638805a2f6f48bb1d70b1c7038
- set_misc_nginx_module 48908343c00a45a40365158282f61d5369d17194
- srcache_nginx_module af82f755b8a92765fff0b3e70b26bedf4bbacadc
- ngx_cache_purge 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
- nginx_rtmp_module 43f1e4209b7ee7b795595912943a8fdc37f2ea4a
- nginx_dav_ext_module 430fd774fe838a04f1a5defbf1dd571d42300cf9
- ngx_http_enhanced_memcached_module a9b76b6c9e0623e3ee84fecb04284dc8c91dfdb4
- ngx_http_secure_download f379a1acf2a76f63431a12fa483d9e22e718400b
- ngx_devel_kit e443262071e759c047492be60ec7e2d73c5b57ec
- nginx_sorted_querystring_module e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
- Delete lua-nginx-cache-module
- Delete replay/ngx_http_consistent_hash

* Wed Jul 12 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.3-1
- 1.13.3
- Update ngx_lua_version commit hash cc0a793a27af48a364b951a374716b8cd5221487

* Wed Jun 28 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.2-1
- 1.13.2
- Update ngx_lua_version commit hash 031e0000429e18d3220c0d530fa03b9ba20d9489

* Mon Jun 12 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.13.1-1
- 1.13.1
- Update OpenSSL to 1.0.2l
- Update ngx_lua_version commit hash 69d995513b17df9ebb09dd4ea6656e1f78b28a34

* Mon Apr 24 2017 Masafumi Yamamoto <masa23@gmail.com> - 1.11.13-1
- 1.11.13
- Update ngx_lua_version commit hash ca8ed0e8cd746c41450b14abff5e40d8f713ccc9
- delete configure option --with-ipv6
 
* Mon Apr 10 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.10-1
- 1.11.10
- Update ngx_lua_version to 0.10.8

* Mon Apr 10 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.9-9
- Build ngx_devel_kit as a static module.

* Tue Mar 21 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.9-8
- Add ngx_devel_kit v0.3.0.
- Add set-misc-nginx-module v0.31.

* Thu Feb  9 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.9-7
- Revert %post, %preun and %postun to the original.

* Tue Jan 31 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.9-6
- Revert %post, %preun and %postun but keep running process during upgrade.

* Tue Jan 31 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.9-5
- Do nothing for %post, %preun and %postun

* Tue Jan 31 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.9-4
- Do not run systemctl preset or chkconfig add in %post.

* Mon Jan 30 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.9-3
- Do not run graceful restart after yum update nginx.

* Sat Jan 28 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.9-2
- Update OpenSSL to 1.0.2k

* Wed Jan 25 2017 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.9-1
- 1.11.9

* Wed Dec 28 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.8-1
- 1.11.8

* Tue Dec 20 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.7-1
- 1.11.7

* Thu Nov 17 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.6-2
- Use master branch of redis2-nginx-module and memc-nginx-module
- https://github.com/openresty/redis2-nginx-module/pull/42
- https://github.com/openresty/memc-nginx-module/pull/27

* Wed Nov 16 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.6-1
- 1.11.6

* Thu Nov 10 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.5-4
- Switch to the OpenResty's fork of LuaJIT 2
- Update https://github.com/openresty/lua-nginx-module to 0.10.7

* Thu Nov 10 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.5-3
- Apply OpenResty's SSL patches

* Fri Oct 21 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.5-2
- Fix PIDFile path in nginx.service and nginx-debug.source

* Thu Oct 20 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.5-1
- 1.11.5

* Tue Sep 27 2016 Masafumi Yamamoto <masa23@gmail.com> - 1.11.4-2
- OpenSSL Update to 1.0.2j

* Mon Sep 26 2016 Masafumi Yamamoto <masa23@gmail.com> - 1.11.4-1
- 1.11.4
- OpenSSL Update to 1.0.2i

* Fri Aug 26 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.3-5
- Add openresty srcache-nginx-module as a dynamic module.
  https://github.com/openresty/srcache-nginx-module/pull/43#issuecomment-213152217

* Fri Aug 26 2016 Masafumi Yamamoto <masa23@gmail.com> - 1.11.3-4
- Update https://github.com/openresty/lua-nginx-module to 0.10.6

* Mon Aug  1 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.3-2
- Update https://github.com/openresty/lua-nginx-module to 0.3.0

* Sat Jul 30 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.3-1
- 1.11.3

* Sat Jul 30 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.2-3
- Remove nginx_upstream_check_module

* Wed Jul 06 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.11.2-2
- Remove nginx-rtmp-module.sockaddr_pointer.patch

* Wed Jul 06 2016 Masafumi Yamamoto <masa23@gmail.com> - 1.11.2-1
- 1.11.2

* Wed Jul 06 2016 Masafumi Yamamoto <masa23@gmail.com> - 1.11.1-4
- support CentOS7 TCP Fast Open

* Tue Jun 28 2016 Masafumi Yamamoto <masa23@gmail.com> - 1.11.1-3
- nginx lua module update v0.10.5

* Tue Jun 28 2016 Masafumi Yamamoto <masa23@gmail.com> - 1.11.1-2
- openssl 1.0.2h library static link

* Tue Jun 28 2016 Masafumi Yamamoto <masa23@gmail.com> - 1.11.1-1
- 1.11.1

* Thu Apr 21 2016 Masafumi Yamamoto <masa23@gmail.com> - 1.9.15-1
- 1.9.15

* Sat Apr  9 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.14-1
- 1.9.14

* Wed Mar 30 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.13-1
- 1.9.13
- Delete patch to add dynamic module support for nginx-rtmp-module

* Thu Feb 25 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.12-1
- 1.9.12
- Remove openresty srcache-nginx-module since it has severe compatiblity
  issues with nginx 1.9.11.
  https://github.com/openresty/srcache-nginx-module/pull/43#issuecomment-187873777

* Mon Feb 22 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.11-6
- Add nginx-dav-ext-module

* Wed Feb 17 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.11-5
- Add ngx_http_enhanced_memcached_module

* Wed Feb 17 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.11-4
- Add openresty srcache-nginx-module, redis2-nginx-module,
  memc-nginx-module lua-upstream-nginx-module and echo-nginx-module
  modules

* Mon Feb 15 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.11-3
- Fix ngx_addon_name of http_consistent_hash and http_secure_download

* Sat Feb 13 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.11-2
- Update ngx_lua_version to 4f2954302ce642a6f17255cff294663aa6552d8d and build it as a dynamic module
- Build http_geoip, http_image_filter, and http_xslt as dynamic modules.
- Build cache_purge, headers-more, http_consistent_hash, http_secure_download, rtmp,
  lua-upstream-cache and sorted-querystring as dynamic modules

* Thu Feb 11 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.11-1
- 1.9.11
- Update ngx_lua_version to 0.10.1rc0
- dynamic modules path and symlink in %{_sysconfdir}/nginx added

* Fri Jan 29 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.10-4
- Add ngx_http_secure_download, nginx-rtmp-module, headers-more-nginx-module,
  lua-nginx-cache-module and ngx_cache_purge modules

* Thu Jan 28 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.10-3
- Add ngx_http_consistent_hash again

* Thu Jan 28 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.10-2
- Add nginx-sorted-querystring-module

* Wed Jan 27 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.10-1
- 1.9.10

* Tue Jan 19 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.9-4
- Add nginx_upstream_check_module again

* Mon Jan 18 2016 Hiroaki Nakamura <hnakamur@gmail.com> - 1.9.9-3
- Remove nginx_upstream_check_module and ngx_http_consistent_hash
- Update ngx_lua_version to 0.10.0

* Sun Dec 13 2015 Hiroaki Nakamura <hnakamur@gmail.com>
- Add lua-nginx-module, nginx_upstream_check_module and ngx_http_consistent_hash

* Wed Dec  9 2015 Konstantin Pavlov <thresh@nginx.com>
- 1.9.9

* Tue Dec  8 2015 Konstantin Pavlov <thresh@nginx.com>
- 1.9.8
- http_slice module enabled

* Tue Nov 17 2015 Konstantin Pavlov <thresh@nginx.com>
- 1.9.7

* Tue Oct 27 2015 Sergey Budnevitch <sb@nginx.com>
- 1.9.6

* Tue Sep 22 2015 Andrei Belov <defan@nginx.com>
- 1.9.5
- http_spdy module replaced with http_v2 module

* Tue Aug 18 2015 Konstantin Pavlov <thresh@nginx.com>
- 1.9.4

* Tue Jul 14 2015 Sergey Budnevitch <sb@nginx.com>
- 1.9.3

* Tue May 26 2015 Sergey Budnevitch <sb@nginx.com>
- 1.9.1

* Tue Apr 28 2015 Sergey Budnevitch <sb@nginx.com>
- 1.9.0
- thread pool support added
- stream module added
- example_ssl.conf removed

* Tue Apr  7 2015 Sergey Budnevitch <sb@nginx.com>
- 1.7.12

* Tue Mar 24 2015 Sergey Budnevitch <sb@nginx.com>
- 1.7.11

* Tue Feb 10 2015 Sergey Budnevitch <sb@nginx.com>
- 1.7.10

* Tue Dec 23 2014 Sergey Budnevitch <sb@nginx.com>
- 1.7.9

* Tue Dec  2 2014 Sergey Budnevitch <sb@nginx.com>
- 1.7.8

* Tue Sep 30 2014 Sergey Budnevitch <sb@nginx.com>
- 1.7.6

* Tue Sep 16 2014 Sergey Budnevitch <sb@nginx.com>
- epoch added to the EPEL7/CentOS7 spec to override EPEL one
- 1.7.5

* Tue Aug  5 2014 Sergey Budnevitch <sb@nginx.com>
- 1.7.4

* Tue Jul  8 2014 Sergey Budnevitch <sb@nginx.com>
- 1.7.3

* Tue Jun 17 2014 Sergey Budnevitch <sb@nginx.com>
- 1.7.2

* Tue May 27 2014 Sergey Budnevitch <sb@nginx.com>
- 1.7.1
- incorrect sysconfig filename finding in the initscript fixed

* Thu Apr 24 2014 Konstantin Pavlov <thresh@nginx.com>
- 1.7.0

* Tue Apr  8 2014 Sergey Budnevitch <sb@nginx.com>
- 1.5.13
- built spdy module on rhel/centos 6

* Tue Mar 18 2014 Sergey Budnevitch <sb@nginx.com>
- 1.5.12
- spec cleanup
- openssl version dependence added
- upgrade() function in the init script improved
- warning added when binary upgrade returns non-zero exit code

* Tue Mar  4 2014 Sergey Budnevitch <sb@nginx.com>
- 1.5.11

* Tue Feb  4 2014 Sergey Budnevitch <sb@nginx.com>
- 1.5.10

* Wed Jan 22 2014 Sergey Budnevitch <sb@nginx.com>
- 1.5.9

* Tue Dec 17 2013 Sergey Budnevitch <sb@nginx.com>
- 1.5.8
- fixed invalid week days in the changelog

* Tue Nov 19 2013 Sergey Budnevitch <sb@nginx.com>
- 1.5.7

* Tue Oct  1 2013 Sergey Budnevitch <sb@nginx.com>
- 1.5.6

* Tue Sep 17 2013 Andrei Belov <defan@nginx.com>
- 1.5.5

* Tue Aug 27 2013 Sergey Budnevitch <sb@nginx.com>
- 1.5.4
- auth request module added

* Tue Jul 30 2013 Sergey Budnevitch <sb@nginx.com>
- 1.5.3

* Tue Jul  2 2013 Sergey Budnevitch <sb@nginx.com>
- 1.5.2

* Tue Jun  4 2013 Sergey Budnevitch <sb@nginx.com>
- 1.5.1

* Mon May  6 2013 Sergey Budnevitch <sb@nginx.com>
- 1.5.0

* Tue Apr 16 2013 Sergey Budnevitch <sb@nginx.com>
- 1.3.16

* Tue Mar 26 2013 Sergey Budnevitch <sb@nginx.com>
- 1.3.15
- gunzip module added
- set permissions on default log files at installation

* Tue Feb 12 2013 Sergey Budnevitch <sb@nginx.com>
- excess slash removed from --prefix
- 1.2.7

* Tue Dec 11 2012 Sergey Budnevitch <sb@nginx.com>
- 1.2.6

* Tue Nov 13 2012 Sergey Budnevitch <sb@nginx.com>
- 1.2.5

* Tue Sep 25 2012 Sergey Budnevitch <sb@nginx.com>
- 1.2.4

* Tue Aug  7 2012 Sergey Budnevitch <sb@nginx.com>
- 1.2.3
- nginx-debug package now actually contains non stripped binary

* Tue Jul  3 2012 Sergey Budnevitch <sb@nginx.com>
- 1.2.2

* Tue Jun  5 2012 Sergey Budnevitch <sb@nginx.com>
- 1.2.1

* Mon Apr 23 2012 Sergey Budnevitch <sb@nginx.com>
- 1.2.0

* Thu Apr 12 2012 Sergey Budnevitch <sb@nginx.com>
- 1.0.15

* Thu Mar 15 2012 Sergey Budnevitch <sb@nginx.com>
- 1.0.14
- OpenSUSE init script and SuSE specific changes to spec file added

* Mon Mar  5 2012 Sergey Budnevitch <sb@nginx.com>
- 1.0.13

* Mon Feb  6 2012 Sergey Budnevitch <sb@nginx.com>
- 1.0.12
- banner added to install script

* Thu Dec 15 2011 Sergey Budnevitch <sb@nginx.com>
- 1.0.11
- init script enhancements (thanks to Gena Makhomed)
- one second sleep during upgrade replaced with 0.1 sec usleep

* Tue Nov 15 2011 Sergey Budnevitch <sb@nginx.com>
- 1.0.10

* Tue Nov  1 2011 Sergey Budnevitch <sb@nginx.com>
- 1.0.9
- nginx-debug package added

* Tue Oct 11 2011 Sergey Budnevitch <sb@nginx.com>
- spec file cleanup (thanks to Yury V. Zaytsev)
- log dir permitions fixed
- logrotate creates new logfiles with nginx owner
- "upgrade" argument to init-script added (based on fedora one)

* Sat Oct  1 2011 Sergey Budnevitch <sb@nginx.com>
- 1.0.8
- built with mp4 module

* Fri Sep 30 2011 Sergey Budnevitch <sb@nginx.com>
- 1.0.7

* Tue Aug 30 2011 Sergey Budnevitch <sb@nginx.com>
- 1.0.6
- replace "conf.d/*" config include with "conf.d/*.conf" in default nginx.conf

* Wed Aug 10 2011 Sergey Budnevitch
- Initial release
