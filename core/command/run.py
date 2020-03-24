# -*- coding: utf-8 -*-

import sys
import os
import re
import traceback

from core.loggers import log

def completer(shell, items, text, state):
    return None

def run(shell, **kwargs):
    options = kwargs['options']
    module  = kwargs['module']

    # 检查是否选择了模块
    if not module:
        shell.print_info('No module selected')
        return

    # 校验参数
    for option in module.__meta__['options']:
        if not option.get('required', False):
            continue

        value = shell.variables.get(option['name'], '').strip()
        if len(value) == 0:
            shell.print_info('The following options failed to validate: {}'.format(option['name']))
            return

    module.run(shell, options = shell.variables)


