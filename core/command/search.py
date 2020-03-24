# -*- coding: utf-8 -*-

import sys
import os
import re
import traceback

def completer(shell, items, text, state):
    return None

def run(shell, **kwargs):
    items = kwargs['items']

    if len(items) != 2:
        shell.print_info('Usage: search keyword_to_use')
        return

    try:
        keyword = items[1].lower()
        result  = filter(lambda x: x.lower().index(keyword) != 0, shell.modules.keys())

        print ""

        for row in result:
            print "{}\n{}\n".format(row, shell.modules[row].meta['name'])
    except ValueError:
        print 'No matched modules'
        pass
    


