import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def CountSecond(time):
    start_time = [5, 35, 0]
    times = time.split(':')
    h = int(times[0]) - start_time[0]
    m = int(times[1]) - start_time[1]
    s = int(times[2]) - start_time[2]
    return h * 3600 + m * 60 + s

def rawData(filename):
    countDict = {item: 0 for item in range(221)}

    fp = open(filename, 'r')
    for line in fp:
        rets = line.strip().split(',')
        fmin = int(CountSecond(rets[3]) / 300)

        if fmin in countDict:
            countDict[fmin] += 1
    countList = sorted(countDict.items(), key=lambda x: x[0])
    value = []
    for item in countList:
        value.append(item[1])
    return value


if __name__ == '__main__':
    value1 = rawData('mahang_01.csv')
    value2 = rawData('mahang_11.csv')#--> 8
    scale = sum(value2) / float(sum(value1))
    value1 = [item*scale for item in value1]
    plt.figure()
    # plt.plot(value1, color='r')
    # plt.plot(value2[9:], color='b')
    sns.boxplot(value2)
    plt.show()