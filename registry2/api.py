#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import requests

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

    print "Found images for registry: {0}".format(URL)
    print "{0}\n".format(' '.join(catalog))

    for c in catalog:
        tags = requests.get("{0}/{1}/tags/list".format(URL, c), verify=False).json()['tags']
        print "Tags for image: {0}".format(c)
        print "{0}\n".format(' '.join(tags))
