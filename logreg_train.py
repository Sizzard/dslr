import argparse
from get_data import getData
from logreg_predict import estimate
import math

def algorithm(data):
    ts = [0, 0, 0, 0]
    
    map_gender = {'Male': 1, "Female": 0}
    map_smoker = {"Smoker": 1, "Non-smoker": 0}
    map_diseased = {"diseased": 1, "not diseased": 0}
    data = data.replace(({"Gender" : map_gender}))
    data = data.replace(({"Smoker status" : map_smoker}))
    data = data.replace({"Disease" : map_diseased})
    ages = (data["Age"] - data["Age"].mean()) / data["Age"].std()
 
    m = len(data)
    iterations = 10000
    learning_rate = 0.001
    res = 0
    for _ in range(iterations):
        sums = [0, 0, 0, 0]

        for i in range(m):
            error = sigmoid(estimate(ts, ages[i], data.iloc[i]["Gender"], data.iloc[i]["Smoker status"])) - data.iloc[i]["Disease"]
            sums[0] += error
            sums[1] += error * ages[i]
            sums[2] += error *  data["Gender"][i]
            sums[3] += error * data["Smoker status"][i]

        d0 = (1 / m) * sums[0]
        d1 = (1 / m) * sums[1]
        d2 = (1 / m) * sums[2]
        d3 = (1 / m) * sums[3]

        ts[0] = ts[0] - (learning_rate * d0)
        ts[1] = ts[1] - (learning_rate * d1)
        ts[2] = ts[2] - (learning_rate * d2)
        ts[3] = ts[3] - (learning_rate * d3)

    return ts


def sigmoid(z):
    res = 1 / (1 + math.exp( - z))
    return res

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('dataset', help='Required dataset to analyse')
        args = parser.parse_args()
        if args.dataset != "dataset_train.csv":
            raise AssertionError("Not entered the good file as parameter")
        data = getData('datatab.csv')
        thetas = algorithm(data)
        print(thetas)
        print(sigmoid(estimate(thetas, 50, 0, 1)))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
