import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from get_data import getData



def getHouseMembers(data, house_name):
    df = pd.DataFrame(columns=["Index", "Hogwarts House", "First Name", "Last Name", "Birthday", "Best Hand", "Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts", "Divination", "Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration", "Potions", "Care of Magical Creatures", "Charms", "Flying"])
    for idx, row in data.iterrows():
        if row["Hogwarts House"] == house_name:
            df.loc[idx] = row
    return df


def main():
    try:
        houses = [ "Hufflepuff", "Gryffindor", "Slytherin", "Ravenclaw"]
        data = getData('datasets/dataset_train.csv')
        huf = getHouseMembers(data, "Hufflepuff")
        print(huf)
        gryf = getHouseMembers(data, "Gryffindor")
        print(gryf)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
