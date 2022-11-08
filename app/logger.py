import logging, sys, time
from logging import config
from random import randint

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        "syslog": {
            "format": "%(asctime)s:%(levelname)s:%(process)d:%(filename)s:%(funcName)s:L%(lineno)d:%(message)s"
        }
    },
    'handlers': {
        'logfile': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'syslog',
            },
        'stdout': {
            'class': 'logging.StreamHandler',
            'stream': open('/var/log/app/mylog.log','a+'),
            'formatter': 'syslog',
            },
        },
    'loggers': {
        'my-logger': {
            'handlers': ['logfile', 'stdout'],
            'level': logging.DEBUG,
            'propagate': True,
            },
        }
    }

config.dictConfig(LOGGING)

logger = logging.getLogger("my-logger")
counter = 0
sleep = 0

while True:
    msg_type = randint(0, 4)
    if(msg_type == 0):
        logger.debug("This is a debug msg number {0} after {1}s".format(counter, sleep))
    if(msg_type == 1):
        logger.info("This is a info msg number {0} after {1}s".format(counter, sleep))
    if(msg_type == 2):
        logger.warning("This is a warn msg number {0} after {1}s".format(counter, sleep))
    if(msg_type == 3):
        logger.error("This is a error msg number {0} after {1}s".format(counter, sleep))
    if(msg_type == 4):
        logger.critical("This is a error msg number {0} after {1}s".format(counter, sleep))

    counter = counter + 1
    sleep = randint(0, 30)
    time.sleep(sleep)