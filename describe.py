import argparse
import math
from get_data import getData


def truncateFloat(float_number, decimal_places):
    multiplier = 10 ** decimal_places
    return int(float_number * multiplier) / multiplier


def getMean(data, data_name):
    return sum(data[data_name]) / len(data[data_name])


def getStd(data, data_name):
    mean = getMean(data, data_name)
    deviation = []
    squared_deviation = []
    for i, nb in enumerate(data[data_name]):
        deviation.insert(i, nb - mean)
        squared_deviation.insert(i, deviation[i] ** 2)
    pre_res = sum(squared_deviation) / len(data[data_name])
    return math.sqrt(pre_res)


def getMin(data, data_name):
    min = float('inf')
    for elem in data[data_name]:
        if elem < min:
            min = elem
    return min


def getMax(data, data_name):
    max = float('-inf')
    for elem in data[data_name]:
        if elem > max:
            max = elem
    return max


def printCount(data):
    print("\nCount        ", end="")
    for i, name in enumerate(data):
        if i >= 5:
            break
        print(f"{len(data[name]): >15}", end=" | ")


def printMean(data):
    print("\nMean         ", end="")
    for i, name in enumerate(data):
        if i >= 5:
            break
        mean = truncateFloat(getMean(data, name), 2)
        print(f"{mean: >15}", end=" | ")
    

def printStd(data):
    print("\nStd          ", end="")
    for i, name in enumerate(data):
        if i >= 5:
            break
        std = truncateFloat(getStd(data, name), 2)
        print(f"{std: >15}", end=" | ")
    

def printMin(data):
    print("\nMin          ", end="")
    for i, name in enumerate(data):
        if i >= 5:
            break
        min = truncateFloat(getMin(data, name), 2)
        print(f"{min: >15}", end=" | ")


def printMax(data):
    print("\nMax          ", end="")
    for i, name in enumerate(data):
        if i >= 5:
            break
        max = truncateFloat(getMax(data, name), 2)
        print(f"{max: >15}", end=" | ")


def getPercent(data, data_name, percent):
    sorted_data = data.sort_values(by=data_name, ignore_index=True)
    index = int(len(sorted_data) * percent / 100)
    return sorted_data.iloc[index][data_name] 


def print25(data):
    print("\n25%          ", end="")
    for i, name in enumerate(data):
        if i >= 5:
            break
        percent25 = truncateFloat(getPercent(data, name, 25), 2)
        print(f"{percent25: >15}", end=" | ")


def print50(data):
    print("\n50%          ", end="")
    for i, name in enumerate(data):
        if i >= 5:
            break
        percent50 = truncateFloat(getPercent(data, name, 50), 2)
        print(f"{percent50: >15}", end=" | ")


def print75(data):
    print("\n75%          ", end="")
    for i, name in enumerate(data):
        if i >= 5:
            break
        percent75 = truncateFloat(getPercent(data, name, 75), 2)
        print(f"{percent75: >15}", end=" | ")


def display(data):
    data = data.fillna(0)
    print("             ", end="")
    for i, name in enumerate(data):
        if i >= 5:
            break
        print(f"{name: >15}", end=" | ")
    printCount(data)
    printMean(data)
    printStd(data)
    printMin(data)
    print25(data)
    print50(data)
    print75(data)
    printMax(data)
    print()


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('dataset', help='Required dataset to analyse')
        args = parser.parse_args()
        data = getData(args.dataset)
        display(data.select_dtypes(include=['int64', 'float64']))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
