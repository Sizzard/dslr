import math

def getThetas():
    with open("thetas.txt", 'r') as file:
        data = file.read()
        thets = data.split('\n')
        return thets


def sigmoid(z):
    res = 1 / (1 + math.exp( - z))
    return res


def estimate(ts, age, gender, smoke_status):
    z = ts[0] + ts[1] * age + ts[2] * gender + ts[3] * smoke_status
    return sigmoid(z)


def main():
    try:
        thetas = getThetas()
        for i in range(4):
            thetas[i] = float(thetas[i])
        print(estimate(thetas, 90, 1, 1))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
