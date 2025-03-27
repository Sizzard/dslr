import matplotlib.pyplot as plt
from get_data import getData



def main():
    try:
        getData('datasets/dataset_train.csv')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
