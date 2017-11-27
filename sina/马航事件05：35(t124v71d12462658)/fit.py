import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def func1(x, a, b):
    return a * x * np.exp(-b * np.sqrt(x))

def func2(x, a, b):
    return a * x * np.exp(-b * np.power(x, 1 / 3.0))

def func3(x, a, b, c, d):
    return a * abs(np.sin(b * x + c)) * np.exp(-d * np.sqrt(x))


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
    xdata = np.array(left, dtype=np.float32)[:185]
    ydata = np.array(value, dtype=np.float32)[36:]
    popt1, pcov1 = curve_fit(func1, xdata, ydata, [1.0, 0.01])
    popt2, pcov2 = curve_fit(func2, xdata, ydata, [1.0, 2.0])
    popt3, pcov3 = curve_fit(func3, xdata, ydata, [1.0, 0.1, 1, 1])
    # print(popt1, pcov1, popt2, pcov2, popt3, pcov3)
    plt.figure(1)
    # plt.subplot(211)
    plt.bar(xdata, ydata)

    x = np.linspace(1, 221, 221)
    y1 = func1(x, popt1[0], popt1[1])
    y2 = func2(x, popt2[0], popt2[1])
    y3 = func3(x, popt3[0], popt3[1], popt3[2], popt3[3])
    # plt.subplot(212)
    plt.plot(x, y1, color='r')
    plt.plot(x, y2, color='g')
    plt.plot(x, y3, color='y')

    # plt.ylim(0, 250)
    plt.ylabel('Visited Amount')
    plt.xlabel('Time')
    print(value.index(max(value[77:96])))
    plt.show()
