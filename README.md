nginx-rpm
=========

A Dockerfile to build [nginx](http://nginx.org/) rpm for CentOS7 using [Travis CI](https://travis-ci.org/) and [fedora copr](https://copr.fedoraproject.org/).

This build includes the following modules:

* [openresty/lua-nginx-module](https://github.com/openresty/lua-nginx-module)
* [yaoweibin/nginx_upstream_check_module](https://github.com/yaoweibin/nginx_upstream_check_module)
* [replay/ngx_http_consistent_hash](https://github.com/replay/ngx_http_consistent_hash)

## License
MIT
