import numpy
a = 0.5273
b = a*0.5
d = numpy.cos(numpy.pi*(3/4))
c = numpy.sqrt(a**2 + b**2 +2*a*b*numpy.cos(numpy.pi*3/4))
print(c)