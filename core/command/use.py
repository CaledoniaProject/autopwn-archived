# -*- coding: utf-8 -*-

import sys
import os
import traceback

from core import colors

def completer(shell, items, text, state):
    # print items
    
    if len(items) > 2:
        return None

    options  = [i for i in shell.modules.keys() if i.startswith(text)]
    if state < len(options):
        return options[state] + ' '
    else:
        return None

def run(shell, **kwargs):
    options = kwargs['options']

    if len(options) != 1:
        shell.print_info('Usage: use module_name')
        return

    if options[0] not in shell.modules:
        shell.print_info('Unknown module: ' + items[1])
        return

    (category, subname)  = options[0].split('/', 1)
    shell.current_module = shell.modules[options[0]]
    shell.prompt         = 'autopwn {}({})'.format(category, subname)
    
    shell.prompt         = '{}autopwn{} {}({}{}{})'.format(
        '\1' + colors.style.UNDERLINE + '\2',
        '\1' + colors.style.RESET_ALL + '\2',

        category,

        '\1' + colors.style.BRIGHT + colors.fg.RED + '\2',
        subname,
        '\1' + colors.style.RESET_ALL + '\2')

