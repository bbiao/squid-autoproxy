#!/usr/bin/env python
#encoding: utf-8

ADSERVERS_URL = 'http://pgl.yoyo.org/adservers/serverlist.php?hostformat=squid-dstdom-regex&showintro=1&startdate%5Bday%5D=&startdate%5Bmonth%5D=&startdate%5Byear%5D=&mimetype=plaintext'

import urllib2
import textwrap

class AdServersFetcher:
    def __init__(self, output_file):
        self.output_file = output_file

    def run(self):
        adservers = urllib2.urlopen(ADSERVERS_URL).read()
        output = open(self.output_file, 'w')
        for line in adservers.split('\n'):
            if len(line) == 0:
                continue
            output.write('acl ads dstdom_regex -i %s\n' % (line, ))

        end = textwrap.dedent('''
        #http_access deny ads
        #deny_info TCP_RESET ads
        ''')
        output.write(end)
        output.close()


def main():
    asf = AdServersFetcher('./ad_servers.squid')
    asf.run()

if __name__ == '__main__':
    main()
