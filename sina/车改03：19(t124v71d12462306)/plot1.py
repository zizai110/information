# coding = utf-8
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math

def func(x, a, b, c, d):
    return a * (np.sin(b * x) + c) * np.exp(-d * np.sqrt(x))

def CountSecond(time):
    start_time = [03, 19, 0]
    times = time.split(':')
    h = int(times[0]) - start_time[0]
    m = int(times[1]) - start_time[1]
    s = int(times[2]) - start_time[2]
    return h * 3600 + m * 60 + s

countDict = {item: 0 for item in range(262)}

def rawData():
    fp = open('car_reform.csv', 'r')
    for line in fp:
        rets = line.strip().split(',')
        fmin = int(CountSecond(rets[3]) / 300)

        if fmin in countDict:
            countDict[fmin] += 1

    countList = sorted(countDict.items(), key=lambda x: x[0])
    left, value = [], []
    for item in countList:
        left.append(item[0])
        value.append(item[1])
    return left, value

if __name__ == '__main__':
    left, value = rawData()
    xdata = np.array(left, dtype=np.float32)
    ydata = np.array(value, dtype=np.float32)
    plt.figure(1)
    plt.bar(xdata, ydata)
    plt.show()