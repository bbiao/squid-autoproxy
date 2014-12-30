squid-autoproxy
===============

*squid-autoproxy* converts chnroutes and gfwlist rules to autoproxy configurations.

It works for me. #fuckgfw #fuckfbx

## Usage

    python conv_gfwlist.py
    python conv_chnroutes.py -p squid

## add following lines to your squid.conf

    prefer_direct on

    include squid-autoproxy/proxyroute.squid
    always_direct allow proxyroute

    include squid-autoproxy/gfwlist.blocked.squid
    never_direct allow gfwlist.blocked.dstdom_regex
    never_direct allow gfwlist.blocked.url_regex

    include squid-autoproxy/gfwlist.cn.squid
    never_direct deny gfwlist.cn.dstdom_regex
    never_direct deny gfwlist.cn.url_regex

    never_direct allow all

### Optional: Deny advertisement servers
    python conv_adservers.py

#### With configure
    include squid-autoproxy/ad_servers.squid
    http_access deny ads
    deny_info TCP_RESET ads

