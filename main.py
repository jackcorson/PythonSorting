import matplotlib.pyplot as plt
import random
import time

def defineGraphAxes(data):
    x = []
    i = 1
    for val in data:
        x.append(i)
        i += 1
    return x

def bogoSort(data):
    x = defineGraphAxes(data)
    start = time.time()
    while data != sorted(data):
        random.shuffle(data)
        plt.clf()
        plt.bar(x, data)
        plt.pause(.001)
    end = time.time()
    elapsed = end - start
    plt.show()
    return elapsed
    
def bubbleSort(data):
    n = len(data)
    x = defineGraphAxes(data)
    start = time.time()
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            plt.clf()
            plt.bar(x, data)
            plt.pause(.1)
    
    end = time.time()
    elapsed = end - start

    plt.show()

    return elapsed

def selectionSort(data):
    x = defineGraphAxes(data)
    start = time.time()
    for index, value in enumerate(data):
        minimum = value
        where = index
        for ind, val in enumerate(data):
            plt.clf()
            plt.bar(x, data)
            plt.pause(.01)
            if val < minimum and ind > index:
                minimum = val
                where = ind

            temp = data[index]
            data[index] = minimum
            data[where] = temp
    end = time.time()
    elapsed = end - start

    plt.show()
    return elapsed 

def insertionSort(data): 
    x = defineGraphAxes(data)
    start = time.time()
    for index, value in enumerate(data):
        if index != 0:
            i = index - 1
            while i != -1:
                if value < data[i]:
                    temp = data[i]
                    data[i] = data[i + 1]
                    data[i + 1] = temp
                plt.clf()
                plt.bar(x, data)
                plt.pause(.1)
                i -= 1
    end = time.time()
    elapsed = end - start
    
    plt.show()
    return elapsed

def exchangeSort(data):
    x = defineGraphAxes(data)
    start = time.time()
    for index, value in enumerate(data):
        for ind, val in enumerate(data):
            if data[ind] < data[index] and ind > index:
                temp = data[index]
                data[index] = data[ind]
                data[ind] = temp
            plt.clf()
            plt.bar(x, data)
            plt.pause(.1)

    end = time.time()
    elapsed = end - start
    
    plt.show()
    return elapsed
            

x = [5, 1, 2, 4, 3] #Test array of random numbers, can be changed

elapsedTimeSelectionSort = selectionSort(x)
print("{time:.2f} seconds".format(time = elapsedTimeSelectionSort))

# elapsedTimeExchangeSort = exchangeSort(x)
# print("{time:.2f} seconds".format(time = elapsedTimeExchangeSort))

# elapsedTimeBogoSort = bogoSort(x)
# print("{time:.2f} seconds".format(time = elapsedTimeBogoSort))

# elapsedTimeInsertionSort = insertionSort(x)
# print("{time:.2f} seconds".format(time = elapsedTimeInsertionSort))

# elapsedTimeBubbleSort = bubbleSort(x)
# print("{time:.2f} seconds".format(time = elapsedTimeBubbleSort))



    
