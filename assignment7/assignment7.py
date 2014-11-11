import numpy as np
from matplotlib import pyplot as plt

#question 1
a = np.arange(1,16).reshape(3,5)
a = a.transpose()

b = a[[1,3],:]
print b
c = a[:,1]
print c
d = a[1:4,:]
print d
e = np.array([i for i in a.ravel() if i >= 3 and i <= 11])
print e

#question 2

a = np.arange(25).reshape(5,5)
print a

b = np.array([1., 5, 10, 15, 20] * 5).reshape(5,5)

print a/b.T

#question 3
result = []
a = np.random.rand(10,3)
for row in a:
	mindistance = 1
	for element in row:
		if abs(element-0.5) < mindistance:
			mindistance = abs(element-0.5)
			i = row.tolist().index(element)
	result.append(i)
#print a
print result


#question 4


N_max = 50
some_threshold = 50

mask = np.array([False]*300*300).reshape(300,300)

#print mask
X = np.linspace(-2, 1, 300)
Y = np.linspace(-1.5, 1.5, 300)

for x in X:
	for y in Y:
		c = x + 1j*y
		z = c
		for v in range(N_max):
			if abs(z) > some_threshold:
				break
			else:
				z = z**2 + c
		if abs(z) < some_threshold:
			mask[X.tolist().index(x)][Y.tolist().index(y)] = True

plt.imshow(mask.T, extent = [-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('a.png')
