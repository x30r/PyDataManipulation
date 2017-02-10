#!/usr/bin/env python
import csv,pandas,math,statistics;
#def mean(number):
#	return float((sum(number)) / len(number))

#column = "Values"
#data = "\n10\n20\n30\n40\n50\n60\n70\n80\n90\n100"
#r = open("read-write.csv","w")
#r.write(column+data)
#r.close()
print 'There are 2 number of columns'
print 'Choose the column:'
x = int(raw_input())
#print('The data is:')
try:
	row = []
	l = []
	f = open("read-write.csv","rb")
	read = csv.reader(f)
	for column in read:
		row.append(column[x])
	print row[0]
	print '--------'
	l = map(int, row[1:len(row)])
	print l
	means = statistics.mean(l)
	medians = statistics.median(l)
	print "Mean:",means
	print "Median:",medians
	l.sort()
	print "Sorted List:",l
	print "Enter the number of Bins to be created:"
	num = float(raw_input())
	bin = math.ceil(len(l)/num)
	bin = int(bin)
	num = int(num)	
	print "Total elements in a bin:",bin
	print "Bins Created:"
	for loop in range(0,num):
		print l[loop*bin:bin*(loop+1)]
finally:
	f.close()


#Do 2 Binning operation
