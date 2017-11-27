#coding = utf-8
import time
import matplotlib.pyplot as plt

count = {item : 0 for item in range(9) }

fp = open('sina_01_1.csv' , 'r')
for line in fp:
	rets = line.strip().split(',')
	start_time = time.strptime('1970-01-01 23:14:00' , "%Y-%m-%d %H:%M:%S")
	visit_time = time.strptime('1970-01-01 '+rets[3] , "%Y-%m-%d %H:%M:%S")
	timeSpan = int((time.mktime(visit_time) - time.mktime(start_time))/300)
	for i in count:
		if timeSpan in count:
			count[timeSpan] += 1
print count
left = count.keys()
value = count.values()

plt.bar(left , value)
plt.ylabel('Visited Amount')
plt.xlabel('Time')
plt.show()