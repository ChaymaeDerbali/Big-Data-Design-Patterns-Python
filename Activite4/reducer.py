#!/usr/bin/python
import sys

Sum =0    #sum of costs
oldKey = None
trouve = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisDay,thisCost = data
	if oldKey and oldKey != thisDay:
		if oldKey == "6":
			trouve= "{0}\t{1}".format(oldKey,Sum/Total)
		else:
			print "{0}\t{1}".format(oldKey,Sum)
			Sum   = 0
		
	oldKey = thisDay
	Sum   += float(thisCost)
	
if oldKey != None:
	print oldKey,"\t", Sum
if trouve != None:
	print trouve

	
