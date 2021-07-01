#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# colors
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'

try:
    import os
    import traceback
    import argparse
    from modules import *
except KeyboardInterrupt:
    print(GREEN + "\n[+] You Pressed Ctrl+C..." + END)
    print(GREEN + "\nExiting" + END)
except:
    print(RED + "\n[!] Some Modules Not Found Please Install It And Try Again. [!]" + END)
    raise SystemExit
