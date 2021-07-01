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

allModules = [["http", "Scan for open HTTP ports, and get the titles."],
              ["mongodb", "Scan for open MongoDB instances, and check if they are password protected."],
              ["mysql", "Scan for open MySQL servers, and try to log in with the default credentials."],
              ["ssh", "Scan for open SSH ports."], ["printer", "Scan for open printer ports and websites."],
              ["gameserver", "Scan for open game server ports."],
              ["manual", "Scan custom ports."], ["template", "Template module for developers."]]

textToModule = [["http", http], ["template", template], ["printer", printer], ["gameserver", gameserver], ["ssh", ssh], ["manual", manual], ["mongodb", mongodb], ["mysql", mysql]]

inModule = False
currentModule = ""
moduleOptions = []


def commandHandler(command):
    command = str(command)
    command = command.lower()

    global inModule
    global currentModule
    global moduleOptions
    global currentModuleFile

    