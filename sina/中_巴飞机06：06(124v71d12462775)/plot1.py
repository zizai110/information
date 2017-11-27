# coding = utf-8
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn.neighbors.kde import KernelDensity
import seaborn as sns

def func(x, a, b, c, d):
    return a * (np.sin(b * x) + c) * np.exp(-d * np.sqrt(x))

def CountSecond(time):
    start_time = [6, 6, 0]
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
    return h * 3600 + m * 60 + s + 64440

countDict = {item: 0 for item in range(506)}

def rawData():
    fp = open('brazil_airport.csv', 'r')
    for line in fp:
        rets = line.strip().split(',')
        fmin = int(CountSecond(rets[3]) / 300)

        if fmin in countDict:
            countDict[fmin] += 1

    fp = open('brazil_airport2.csv', 'r')
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
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.bar(xdata, ydata)
    plt.subplot(2,1,2)
    sns.kdeplot(ydata, kernel='gau')
    plt.show()