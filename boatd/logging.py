from __future__ import print_function

import time

from .color import color

VERBOSE, NORMAL, WARN, ERROR = range(4)


def log(message, level=NORMAL):
    messages = []
    if level == WARN:
        messages.append('[{}]'.format(color('WARNING', 31)))

    messages.append(message)
    print(time.strftime('[%H:%M:%S]'), *messages)
