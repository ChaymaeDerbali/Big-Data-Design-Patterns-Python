#! /usr/bin/python

import sys

nb=0

for line in sys.stdin:
	data=line.strip().split("\t")
	if len(data) != 2: 
		continue
	nb=nb+1
print nb
