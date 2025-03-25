import pandas as pd


def getData(filepath: str) -> any:
    df = pd.read_csv(filepath)
    return df

def getHouseMembers(data, house_name):
    df = pd.DataFrame(columns=["Index", "Hogwarts House", "First Name", "Last Name", "Birthday", "Best Hand", "Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts", "Divination", "Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration", "Potions", "Care of Magical Creatures", "Charms", "Flying"])
    for idx, row in data.iterrows():
        if row["Hogwarts House"] == house_name:
            df.loc[idx] = row
    return df