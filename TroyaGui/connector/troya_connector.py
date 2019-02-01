#!/usr/bin/env python2

import sys

from connector import troyadconnector

global LSYSTEM
LSYSTEM = ""


def get_troya_response(data):
    return troyadconnector.get_troya_response(data)

