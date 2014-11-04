import numpy as np
import matplotlib.pyplot as plt

#positions = np.array([1,10,100,1000])
num_trials = 10000
position_value = [1000,100,10,1]
cumu_ret = []
position = 1000

for trial in range(num_trials):
	temp = 0
	for i in range(position): 
		if np.random.rand() <= 0.51: 
			temp += (2*1000/position)
	cumu_ret.append(temp)

cumu_ret = np.array(cumu_ret)
daily_ret = (cumu_ret/1000.) - 1
print "the mean value of the daily return",np.mean(daily_ret)
print "the standard deviation of the daily return",np.std(daily_ret)
plt.hist(daily_ret,100,range=[-1,1])
plt.show()

