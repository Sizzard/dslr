from get_data import getData, getHouseMembers
from describe import getMin, getMax, getMean, getPercent, getStd
import matplotlib.pyplot as plt
import pandas as pd


# def getDescribedData(data):
#     lst = []
#     df = pd.DataFrame(columns=["Index", "Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts", "Divination", "Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration", "Potions", "Care of Magical Creatures", "Charms", "Flying"])
#     for idx, study in enumerate(df):
#         lst.insert(idx, getPercent(data, study, 50))
#     return lst

def main():
    try:
        data = getData('datasets/dataset_train.csv')
        huf = getHouseMembers(data, "Hufflepuff")
        gryf = getHouseMembers(data, "Gryffindor")
        sly = getHouseMembers(data, "Slytherin")
        rav = getHouseMembers(data, "Ravenclaw")
        plt.hist( [huf["Transfiguration"], gryf["Transfiguration"], sly["Transfiguration"], rav["Transfiguration"]] , label=["Hufflepuff", "Gryffindor", "Slytherin", "Ravenclaw"])
        plt.xlabel("Sum of grades")
        plt.ylabel("Frequency")
        plt.legend(loc="upper right")
        plt.show()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
