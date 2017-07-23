import numpy
data = numpy.random.random(10)
print "--Sorted Data--"
data.sort()
print data
normalized = (data-min(data))/(max(data)-min(data))
print "--Normalized min-max data--" 
print normalized
