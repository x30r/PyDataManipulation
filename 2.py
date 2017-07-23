import csv
column = "Values"
data = "\n40\n50\n90\n10\n90\n60\n70\n80\n30\n100"
r = open("2.csv","w")
r.write(column+data)
r.close()
row = []
l = []
f = open("2.csv","rb")
read = csv.reader(f)
for column in read:
	row.append(column[0])
print row[0]
print "--------"
l = map(int, row[1:len(row)])
l.sort()
print type(l)
print l
