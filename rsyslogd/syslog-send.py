#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Send 2 test message to remote syslog server (localhost:514/udp)

1. rfc3164 protocol: https://tools.ietf.org/html/rfc3164
2. rfc5242 protocol: https://tools.ietf.org/html/rfc5424
'''

import logging
import logging.handlers

rootLogger = logging.getLogger('')
rootLogger.setLevel(logging.DEBUG)
socketHandler = logging.handlers.SysLogHandler(address=('localhost', 514))
rootLogger.addHandler(socketHandler)

config_rfc3164 = {
    'DATE': 'Oct 11 22:14:15',
    'HOSTNAME': 'mymachine',
    'TAG': 'programname[321]:',
    'MSG': 'rfc3164 test logger message',
    }

logging.info('{DATE} {HOSTNAME} {TAG} {MSG}'.format(**config_rfc3164))

config_rfc5424 = {
    'VERSION': '1',
    'DATE': '1985-04-12T23:20:50.52Z',
    'HOSTNAME': 'mymachine',
    'APP-NAME': 'appname',
    'PROCID': '321',
    'MSGID': 'MSGID',
    'MSG': 'rfc5424 test logger message в юникоде'
    }

logging.info('{VERSION} {DATE} {HOSTNAME} {APP-NAME} {PROCID} {MSGID} {MSG}'.format(**config_rfc5424))
