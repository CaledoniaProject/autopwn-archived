# -*- coding: utf-8 -*-

import sys
import os
import re
import traceback

from texttable import Texttable

def completer(shell, items, text, state):
    return None

def run(shell, **kwargs):
    module = kwargs['module']

    if not module:
        shell.print_info('No module selected')
        return

    info = module.__meta__

    print ""

    print        "Name:\n  {}\n".format(info['name'])
    print "Description:\n  {}\n".format(info['description'])
    print      "Author:\n  {}\n".format(info['author'])
    print  "References:\n  {}\n".format("\n".join(info['references']))

