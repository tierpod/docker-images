#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import requests
import textwrap

DEFAULT_SRV = 'localhost:5000'

def parse_args():
    parser = argparse.ArgumentParser(description='Get images list from docker registry')
    parser.add_argument('-s', '--server', type=str, default=DEFAULT_SRV,
                        help='Registry server [default: {0}]'.format(DEFAULT_SRV))
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    URL = 'https://{0}/v2'.format(args.server)
    # Disable InsecureRequestWarning: Unverified HTTPS request...
    requests.packages.urllib3.disable_warnings()

    catalog = requests.get("{0}/_catalog".format(URL), verify=False).json()['repositories']

    wrapper = textwrap.TextWrapper(initial_indent='  ', subsequent_indent='  ',
                                   break_on_hyphens=False)

    print "Found images for registry: {0} (total: {1})".format(URL, len(catalog))
    print wrapper.fill(' '.join(catalog))
    print ""

    for c in catalog:
        tags = requests.get("{0}/{1}/tags/list".format(URL, c), verify=False).json()['tags']
        print "Tags for image: {0} (total: {1})".format(c, len(tags))
        print wrapper.fill(' '.join(tags))
        print ""
