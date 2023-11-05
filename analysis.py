from timeit import Timer, timeit
import time
import random
from matplotlib import pyplot as plt

def bubbleSort(data):

    for i in range(len(data) - 1, 0, -1):  # generate a range for the next step
        for j in range(i):  # note that the range i is decrementing
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j] # swap items


def mergeSort(data):
    print("Splitting ", data)
    #start = time.time()
    if len(data) > 1:
        mid = len(data) // 2
        l = data[:mid]
        r = data[mid:]

        mergeSort(l)

        mergeSort(r)


        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                print(data)
                data[k] = l[i]
                i += 1
            else:
                data[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            data[k] = l[i]
            i, k = i + 1, k + 1
        while j < len(r):
            data[k] = r[j]
            j, k = j + 1, k + 1


def analyze (fxn, data):
    times = []
    for i in data:
        t = Timer(f"{fxn}({i})", f"from __main__ import {fxn}")
        time_taken = t.timeit(number=len(i))
        times.append(time_taken)
    return times


if __name__ == '__main__':
    # generate lists of random numbers from 0 to 500
    d1 = random.sample(range(0, 500), 10)
    d2 = random.sample(range(0, 500), 20)
    d3 = random.sample(range(0, 500), 50)
    d4 = random.sample(range(0, 500), 100)
    d5 = random.sample(range(0, 500), 200)

    # use random lists as input
    data = [d1, d2, d3, d4, d5]
    time = analyze('bubbleSort', data)
    plt.plot([len(i) for i in data], time, 'r')

    time = analyze('mergeSort', data)
    plt.plot([len(i) for i in data], time, 'b')
    plt.show()