def getThetas():
    with open("thetas.txt", 'r') as file:
        data = file.read()
        thets = data.split('\n')
        return thets

def estimate(tts, age, gender, smoke_status):
    y = tts[0] + tts[1] * age + tts[2] * gender + tts[3] * smoke_status
    return y




def main():
    try:
        thetas = getThetas()
        estimate(tts, )
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
