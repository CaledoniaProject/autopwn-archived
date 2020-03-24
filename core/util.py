# -*- coding: utf-8 -*-

import sys
import os
import re
import imp
import shlex
import traceback

from pathlib import Path

def parse_command(line):
    return shlex.split(line)

def load_modules(base_dir):
    result = {}
    
    for filename in Path(base_dir).glob('**/*.py'):
        filename = str(filename)
        modname  = filename[len(base_dir):-3]

        result[modname] = imp.load_source(modname, filename)

    return result

def default_args():
    return [
        {
            'name':        'URL',
            'required':    True,
            'description': 'Target URL'
        },
        {
            'name':        'RHOST',
            'required':    False,
            'description': 'Specify target IP address'
        },
        {
            'name':        'Cookie',
            'required':    False,
            'description': 'Specify cookie header'
        },
    ]


