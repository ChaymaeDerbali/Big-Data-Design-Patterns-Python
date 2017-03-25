#!/usr/bin/python
import sys
Total = 0
oldKey = None
posts= []
trouve = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisWord,thisPost = data
	if oldKey and oldKey != thisWord:
		if oldKey == "difficult":
			trouve= "{0}\t{1}\t{2}".format(oldKey,Total,posts)
		else:
			print "{0}\t{1}\t{2}".format(oldKey,Total,posts)
			Total = 0
			posts = []
		
	oldKey = thisWord
	posts.append(thisPost)
	Total += 1
	
if oldKey != None:
	print oldKey,"\t", Total,"\t",posts
if trouve != None:
	print trouve

	
