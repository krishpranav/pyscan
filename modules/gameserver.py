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

    def getNextIp(self):
        if not (self.i >= self.size -1):
            ip = self.allIps[self.i]
            self.i += 1 
            return ip
        return 0
    
    def getID(self):
        return self.i + 1

def coreOptions():
    options = [["network", "IP range to scan", ""], ["port-timeout", "Timeout (in sec) for port 80.", "0.3"],
               ["threads", "Number of threads to run.", "100"], ["verbose", "Show verbose output.", "true"]]
    return options

def createIPList(network):
    net4 = ipaddress.ip_network(network)
    ipList = []
    for x in net4.hosts():
        ipList.append(x)
    return ipList

def print1(data):
    if verbose:
        print("\033[K" + data)