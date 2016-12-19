#!/usr/bin/env python

from socket import *
import cPickle

def send(cmd):
	cs = socket(AF_INET, SOCK_DGRAM)
	cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

	cs.sendto(cPickle.dumps(cmd), ('255.255.255.255', 54545))


