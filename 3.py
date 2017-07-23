import numpy
data = numpy.random.random(102)
print data
bins = numpy.linspace(0, 1, 10)
print "Bins:"
print bins
digitized = numpy.digitize(data, bins)
bin_means = [data[digitized == i].mean() for i in range(1, len(bins))]
print "Bin Means:"
print bin_means
