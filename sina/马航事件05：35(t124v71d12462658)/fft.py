import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def CountSecond(time):
    start_time = [5, 35, 0]
    times = time.split(':')
    h = int(times[0]) - start_time[0]
    m = int(times[1]) - start_time[1]
    s = int(times[2]) - start_time[2]
    return h * 3600 + m * 60 + s

def rawData():
    countDict = {item: 0 for item in range(221)}

    fp = open('sina_02_1.csv', 'r')
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
    y_fft = fft(value, 576)
    plt.plot(abs(y_fft))
    plt.xlim(0, 288)
    plt.xticks([0,6,144,288],[0,'4h','10min','5min'])
    plt.show()