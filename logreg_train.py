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
    ages = data["Age"]
    genders = data["Gender"]
    smoke_status = data["Smoker status"]
 
    iterations = 10000
    learning_rate = 0.0001
    epsilon = 1e-15
    for _ in range(iterations):
        sums = [0, 0, 0, 0]
        log_loss = 0


        for i, status in enumerate(data["Disease"]):
            y = status
            ŷ = estimate(ts, ages[i], genders[i], smoke_status[i])
            ŷ = max(epsilon, min(1 - epsilon, ŷ))
            log_loss += y * math.log(ŷ) + (1 - y) * math.log(1 - ŷ)
            
            sums[0] += (ŷ - y)
            sums[1] += (ŷ - y) * ages[i]
            sums[2] += (ŷ - y) * genders[i]
            sums[3] += (ŷ - y) * smoke_status[i]

        ts[0] = ts[0] - learning_rate * sums[0]
        ts[1] = ts[1] - learning_rate * sums[1]
        ts[2] = ts[2] - learning_rate * sums[2]
        ts[3] = ts[3] - learning_rate * sums[3]
        log_loss = -log_loss
        print(log_loss)
    return ts


def writeThetas(ts):
    with open("thetas.txt" , 'w') as file:
        file.write(f"{ts[0]}\n{ts[1]}\n{ts[2]}\n{ts[3]}")


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
        writeThetas(thetas)
        print(estimate(thetas, 40, 0, 0))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
