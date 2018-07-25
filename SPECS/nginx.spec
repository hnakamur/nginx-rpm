#
%define nginx_home %{_localstatedir}/cache/nginx
%define nginx_user nginx
%define nginx_group nginx
%define nginx_loggroup adm

%define ngx_openssl_version 1.0.2o

%define echo_nginx_module_commit c65f5c638d0501b482fbc3ebbda9a49648022d40
%define headers_more_nginx_module_commit a9f7c7e86cc7441d04e2f11f01c2e3a9c4b0301d
%define lua_nginx_module_commit e94f2e5d64daa45ff396e262d8dab8e56f5f10e0
%define lua_upstream_nginx_module_commit 6ebcda3c1ee56a73ba73f3a36f5faa7821657115
%define memc_nginx_module_commit 858fcdcf145ce2cad51cf5c8aa3d5e41a0facac3
%define redis2_nginx_module_commit c989c829a2877132cb100f901e320921250e068d
%define set_misc_nginx_module_commit aac9afe4c42d96e35d496994c552839799010255
%define srcache_nginx_module_commit 53a98806b0a24cc736d11003662e8b769c3e7eb3
%define lua_resty_core_commit bdbac701eb017370775f7333979922041021aeee
%define stream_lua_nginx_module_commit e3eb228c08e5bab30404d5d715bd9b5a545f68a8
%define lua_resty_cookie_commit 3edcd960ba9e3b2154cd3a24bf3e12f3a2a598a6
%define lua_resty_http_commit 75e30060863d41df47c95a5b54e1458954e98792
%define ngx_cache_purge_commit 331fe43e8d9a3d1fa5e0c9fec7d3201d431a9177
%define nginx_rtmp_module_commit 791b6136f02bc9613daf178723ac09f4df5a3bbf
%define nginx_dav_ext_module_commit 430fd774fe838a04f1a5defbf1dd571d42300cf9
%define ngx_http_enhanced_memcached_module_commit b58a4500db3c4ee274be54a18abc767219dcfd36
%define ngx_http_secure_download_commit f379a1acf2a76f63431a12fa483d9e22e718400b
%define ngx_devel_kit_commit a22dade76c838e5f377d58d007f65d35b5ce1df3
%define nginx_sorted_querystring_module_commit e5bbded07fd67e2977edc2bc145c45a7b3fc4d26
%define ngx_http_pipelog_module_commit 2503d5ef853ff2542ee7e08d898a85a7747812e5
%define nginx_http_shibboleth_commit b441df08887fc10e44cc047da2a188014a0dadf5

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
Version: 1.15.2
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

Patch14: ngx_http_secure_download-dynamic_module.patch
Patch15: ngx_cache_purge-dynamic_module.patch
Patch16: ngx_cache_purge-fix_compatibility_with_nginx_1.11.6.patch
Patch17: ngx_cache_purge-feat_purge_all.patch
Patch18: ngx_cache_purge-feat_purge_partial_keys.patch
Patch19: ngx_cache_purge-select_response_type.patch
Patch20: nginx-1.11.2-ssl_cert_cb_yield.patch

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

Provides: webserver

%description
nginx [engine x] is an HTTP and reverse proxy server, as well as
a mail proxy server.

%if 0%{?suse_version} == 1315
%debug_package
%endif

%prep
%setup -q -a 100 -a 101 -a 102 -a 103 -a 104 -a 105 -a 106 -a 107 -a 108 -a 109 -a 110 -a 111 -a 112 -a 113 -a 114 -a 115 -a 116 -a 117 -a 118 -a 119 -a 120 -a 121
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
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
        --with-debug \
        %{?with_http2:--with-http_v2_module} \
        --with-cc-opt="%{optflags} $(pcre-config --cflags)%{?tcp_fast_open: -DTCP_FASTOPEN=23}" \
        $*
make %{?_smp_mflags}
%{__mv} %{_builddir}/%{name}-%{version}/objs/nginx \
        %{_builddir}/%{name}-%{version}/objs/nginx-debug
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
        %{?with_http2:--with-http_v2_module} \
        --with-cc-opt="%{optflags} $(pcre-config --cflags) %{?tcp_fast_open: -DTCP_FASTOPEN=23}" \
        $*
make %{?_smp_mflags}

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

%{__mkdir} -p $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-core/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-cookie/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua
%{__cp} -pr %{_builddir}/%{name}-%{version}/lua-resty-http/lib/* $RPM_BUILD_ROOT%{_prefix}/lib/nginx/lua

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

%{__install} -m644 \
    %{_builddir}/%{name}-%{version}/nginx-http-shibboleth/includes/shib_clear_headers \
    %{_builddir}/%{name}-%{version}/nginx-http-shibboleth/includes/shib_fastcgi_params \
    $RPM_BUILD_ROOT%{_sysconfdir}/nginx/

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{_sbindir}/nginx
%{_sbindir}/nginx-debug

%dir %{_sysconfdir}/nginx
%dir %{_sysconfdir}/nginx/conf.d
%{_sysconfdir}/nginx/modules

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
* Wed Jul 11 2018 Hiroaki Nakamura <hnakamur@gmail.com> - 1.15.2-1
- 1.15.2
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
