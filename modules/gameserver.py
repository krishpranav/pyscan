#!/usr/bin/env python3

# imports
import socket
import datetime
import sys
import ipaddress
import threading
import os 

# colors
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'


class ThreadManager(object):
    i = 0

    def __init__(self, ipList):
        self.allIps = ipList
        self.size = len(ipList)
        