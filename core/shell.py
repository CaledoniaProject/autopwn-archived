# -*- coding: utf-8 -*-

import sys
import os
import re
import json
import traceback
import readline
import atexit

from core.util import parse_command, load_modules

class Shell:
    def __init__(self):
        self.version        = 'v17.12.31'
        self.prompt         = 'autopwn'
        self.commands       = load_modules('core/command/')
        self.modules        = load_modules('modules/')
        self.histfile       = os.path.join(os.path.expanduser("~"), ".autopwn_hist")

        self.current_module = None
        self.variables      = {}
        self.advanced       = [
            { 'name': 'RHOST',  'descr': 'Connect to this IP address instead' },
            { 'name': 'COOKIE', 'descr': 'Specify Cookie header' }            
        ]

        self.load_history()
        self.banner()

    def banner(self):
        keys_all  = self.modules.keys()
        auxiliary = filter(lambda x: x.startswith('auxiliary'), keys_all)
        exploits  = filter(lambda x: x.startswith('exploits'),  keys_all)

        print ""
        print '           =[   autopwn %1s ]'       % (self.version)
        print '    + -- --=[   %-3d exploits      ]' % (len(exploits))
        print '    + -- --=[   %-3d auxiliary     ]' % (len(auxiliary))
        print ""

    def load_history(self):
        try:
            open(self.histfile, 'a').close()

            readline.read_history_file(self.histfile)
            readline.set_history_length(1000)

            atexit.register(readline.write_history_file, self.histfile)
        except IOError:
            pass

    def completer(self, text, state):
        line  = readline.get_line_buffer()
        items = parse_command(line)

        if readline.get_begidx() > len(items[0]):
            if items[0] not in self.commands:
                return None
            else:
                return self.commands[items[0]].completer(self, items, text, state)

        options  = [i for i in self.commands.keys() if i.startswith(text)]
        if state < len(options):
            return options[state] + ' '
        else:
            return None

    def run(self):
        readline.set_completer_delims(' \t\n;')
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.completer)

        while True:
            try:
                cmd = raw_input("%s > " % (self.prompt)).strip()
                if len(cmd) == 0:
                    continue

                items   = parse_command(cmd)
                options = items[1:]

                if items[0] not in self.commands:
                    self.print_info('Unknown command: {}'.format(items[0]))
                else:
                    self.commands[items[0]].run(
                        self,
                        options = options,
                        module  = self.current_module)

            except KeyboardInterrupt:
                print 'UserInterrupt'
                break
            except EOFError:
                print 'exit'
                break
            except Exception:
                print traceback.format_exc()
                pass

    def print_info(self, text, **kwargs):
        print '[-]', text

    def print_warning(self, text, **kwargs):
        print '[-]', text



