# coding = utf-8
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math
import seaborn as sns

def func(x, a, b, c, d):
    return a * (np.sin(b * x) + c) * np.exp(-d * np.sqrt(x))

def CountSecond(time):
    start_time = [23, 14, 0]
    times = time.split(':')
    h = int(times[0]) - start_time[0]
    m = int(times[1]) - start_time[1]
    s = int(times[2]) - start_time[2]
    return h * 3600 + m * 60 + s


def CountSecond2(time):
    times = time.split(':')
    h = int(times[0])
    m = int(times[1])
    s = int(times[2])
    return h * 3600 + m * 60 + s + 2760


countDict = {item: 0 for item in range(300)}

def rawData():
    fp = open('sina_01_1.csv', 'r')
    for line in fp:
        rets = line.strip().split(',')
        fmin = int(CountSecond(rets[3]) / 300)

        if fmin in countDict:
            countDict[fmin] += 1

    fp = open('sina_01_2.csv', 'r')
    for line in fp:
        rets = line.strip().split(',')
        fmin = int(CountSecond2(rets[3]) / 300)

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
    popt, pcov = curve_fit(func, xdata, ydata, [1.0, 0.005, 0.1,1])
    # popt1, pcov1 = curve_fit(func1, xdata, ydata, [1.0, 1])
    print(popt,pcov)
    print(max(ydata))
    x = np.linspace(1, 300, 300)
    y = func(x, popt[0], popt[1], popt[2], popt[3])
    # y1 = func(x, popt1[0], popt1[1])

    plt.bar(xdata, ydata)
    plt.plot(x, y, color='r')
    # plt.plot(x, y1, color='g')
    plt.xticks([0,50,100,150,200,250,300],['23:14','03:24','07:34','11:44','15:54','20:04','00:14'])
    plt.ylabel('Vistied amount')
    plt.xlabel('time')
    plt.title('Visited amount with time')
    
    plt.show()