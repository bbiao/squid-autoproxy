#!/usr/bin/env python
#encoding: utf-8

# thanks to https://sorz.org/p/squid-blacklist

import urllib2
from base64 import b64decode

GFWLIST_URL = 'https://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt'
BLACK_FILE = 'gfwlist.blocked.squid'
WHITE_FILE = 'gfwlist.cn.squid'

def convert_line(line, aclname):
    # in the original gfwlist, the line is a regexp
    if line[0] == '/' and line[-1] == '/':
        return 'acl %s.url_regex url_regex %s' % (aclname, line[1:-1])

    # replace the wildcard to regexp
    line = line.replace('*', '.*')

    # some rules' url contains . ()
    line = line.replace('/', '\/').replace('-', '\-').replace('.', '\.').replace('(', '\(').replace(')', '\)')

    if line.startswith('||'): # ||12bet.com
        #return 'acl %{2}s url_regex ^[\w\-]+:\/+(?!\/)(?:[^\/]+\.)?%{1}s' % (line[2:], aclname)
        return 'acl %s.dstdom_regex dstdom_regex %s' % (aclname, line[2:])
    elif line.startswith('|'):
        return 'acl %s.url_regex url_regex %s' % (aclname, line[1:])
    else:
        return 'acl %s.url_regex url_regex %s' % (aclname, line)

def convert_list(gfwlist):
    black = open(BLACK_FILE, 'w')
    white = open(WHITE_FILE, 'w')

    for l in gfwlist.split('\n'):
        if not l or l[0] == '!' or l[0] == '[':
            continue

        if l.startswith('@@'):
            white.write(convert_line(l[2:], 'gfwlist.cn') + '\n')
        else:
            black.write(convert_line(l, 'gfwlist.blocked') + '\n')

    black.close()
    white.close()

def main():
    src = urllib2.urlopen(GFWLIST_URL).read()
    #src_file = open('gfwlist.txt', 'r')
    #lines = src_file.readlines()
    #src = ''.join(lines)
    #src_file.close()
    src = b64decode(src)
    convert_list(src)

if __name__ == '__main__':
    main()
