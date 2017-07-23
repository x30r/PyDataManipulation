#usr/bin/python python
import random
print "[+]Generating CSV"
fi = open("p1.csv","w")
print "[+]Generating 10k Numbers"
for i in range(0,10000):
	rand = random.randint(1,50)
	rand = str(rand)
	fi.write(rand+"\n")
print "[+]File Generated as p1.csv"
