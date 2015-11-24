#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Send 2 test message to remote syslog server (localhost:514/udp)

1. rfc3164 protocol: https://tools.ietf.org/html/rfc3164
2. rfc5242 protocol: https://tools.ietf.org/html/rfc5424
'''

import logging
import logging.handlers

HOSTNAME = 'localhost'
PORT = 514

rootLogger = logging.getLogger('')
rootLogger.setLevel(logging.DEBUG)
socketHandler = logging.handlers.SysLogHandler(address=(HOSTNAME, PORT))
rootLogger.addHandler(socketHandler)

###
config_rfc3164 = {
    'DATE': 'Oct 11 22:14:15',
    'HOSTNAME': 'mymachine',
    'TAG': 'programname[321]:',
    'MSG': 'rfc3164 test logger message',
    }
template_rfc3164 = '{DATE} {HOSTNAME} {TAG} {MSG}'
message_rfc3154 = template_rfc3164.format(**config_rfc3164)

print('rfc3164:')
for k, v in config_rfc3164.items():
    print('  {0:10} {1}'.format(k, v))
print('  {0:10} {1}'.format('Template', template_rfc3164))
print('  {0:10} {1}'.format('Message', message_rfc3154))
logging.info(message_rfc3154)


###
config_rfc5424 = {
    'VERSION': '1',
    'DATE': '1985-04-12T23:20:50.52Z',
    'HOSTNAME': 'mymachine',
    'APP-NAME': 'appname',
    'PROCID': '321',
    'MSGID': 'MSGID',
    'MSG': 'rfc5424 test logger message в юникоде'
    }

template_rfc5242 = '{VERSION} {DATE} {HOSTNAME} {APP-NAME} {PROCID} {MSGID} {MSG}'
message_rfc5242 = template_rfc5242.format(**config_rfc5424)

print('\nrfc5242:')
for k, v in config_rfc5424.items():
    print('  {0:10} {1}'.format(k, v))
print('  {0:10} {1}'.format('Template', template_rfc5242))
print('  {0:10} {1}'.format('Message', message_rfc5242))
logging.info(message_rfc5242)
