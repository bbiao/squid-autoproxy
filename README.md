squid-autoproxy
===============

## usage

    python conv_gfwlist.py
    python conv_chnroutes.py -p squid

add following lines to your squid.conf

    include squid-autoproxy/proxyroute.squid
    include squid-autoproxy/gfwlist.blocked.squid
    include squid-autoproxy/gfwlist.cn.squid

    always_direct allow proxyroute

    never_direct allow gfwlist.blocked.dstdom_regex
    never_direct allow gfwlist.blocked.url_regex
    never_direct deny gfwlist.cn.dstdom_regex
    never_direct deny gfwlist.cn.url_regex
