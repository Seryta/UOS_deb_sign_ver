#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Saryta
# @last-modified 2021-02-25T10:13:07.875Z+08:00

import sys, getopt, os
from pathlib import Path

class Verify(object):
    def __init__(self, opts, args) -> None:
        self.opts = opts
        self.args = args

    def errors():
        pass

def main():
    try:
        print(f"Will parse argv: {sys.argv[1:]}")
        opts, args = getopt.getopt(sys.argv[1:], 'hs', ['help','sign'])
        Verify(opts, args)
    except getopt.GetoptError:
        print("Parameter format error!")
        usage()
        sys.exit(2)

def usage():
    print("Sign_deb_ver version 1.0")
    print("""
    usage:  sign-deb-ver    [-h help] [-s sign]
    """)

if __name__ == "__main__":
    cwd = Path.cwd().joinpath('main.py')
    command = "grep 'alias sign-deb-ver=' ~/.bashrc"
    result = os.popen(command).read()
    if result == '':
        print("第一次执行脚本，必须在脚本所在目录中进行！")
        command = '''echo "alias sign-deb-ver='python3 {}'" >> ~/.bashrc'''.format(cwd)
        os.popen(command)
    else:
        main()