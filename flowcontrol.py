rangeList = range(17)
# print rangeList
for number in rangeList:
	if number in (1, 4, 10, 20):
		print number, "is here"
	else:
		print number, "not here"

print
if rangeList[1] == 2:
	print "The second item (lists are 0-based) is 2"
elif rangeList[1] == 3:
	print "The second item (lists are 0-based) is 3"
else:
	print "Dunno"

