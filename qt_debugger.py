#!/usr/bin/env python

import pydevd


def debug_this_thread():
    try:
        pydevd.settrace(suspend=False)
    except:
        pass

