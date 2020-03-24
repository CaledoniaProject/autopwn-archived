# -*- coding: utf-8 -*-

import sys
import os
import re
import traceback

from core.loggers import log

def completer(shell, items, text, state):
    if len(items) > 2:
        return None

    keys    = []
    options = shell.current_module.__meta__['options']

    for option in options:
        keys.append(option['name'])
    for option in shell.advanced:
        keys.append(option['name'])

    options  = [i for i in keys if i.startswith(text)]
    if state < len(options):
        return options[state] + ' '
    else:
        return None

def run(shell, **kwargs):
    options = kwargs['options']

    if len(options) != 2:
        shell.print_info('Usage: set NAME VALUE')
        return

    key   = options[0]
    value = options[1]

    shell.variables[key] = value
    shell.print_info("{} => {}".format(key, value))




    