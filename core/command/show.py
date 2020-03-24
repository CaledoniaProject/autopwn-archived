# -*- coding: utf-8 -*-

import sys
import os
import re

def _show_options(shell):
    if not shell.current_module:
        shell.print_info('No module selected')
        return

    formats = '\t{0:<12}{1:<16}{2:<16}{3:<16}'
    options = shell.current_module.__meta__['options']

    print ""
    print formats.format("Name", "Value", "Required", "Description")
    print formats.format("----", "-----", "--------", "-----------")

    for option in options:
        print formats.format(
            option['name'], 
            shell.variables.get(option['name'], ''), 
            'Yes' if option.get('required', False) else 'No',
            option['descr'])

    print ""

def _show_advanced(shell):
    formats   = '\t{0:<12}{1:<16}{2:<16}'

    print ""
    print formats.format("Name", "Value", "Description")
    print formats.format("----", "-----", "-----------")

    for option in shell.advanced:
        print formats.format(
            option['name'], 
            option.get('value', ''), 
            option['descr'])

    print ""

known_options = {
    'options':  _show_options,
    'advanced': _show_advanced
}

def completer(shell, items, text, state):
    if len(items) > 2:
        return None

    options  = [i for i in known_options.keys() if i.startswith(text)]
    if state < len(options):
        return options[state] + ' '
    else:
        return None

def run(shell, **kwargs):
    options = kwargs['options']

    if len(options) != 1:
        shell.print_info('Usage: show [field]')
        return
    elif options[0] in known_options:
        return known_options[options[0]](shell)
    else:
        shell.print_info('Unknown field %s', options[0])

