import argparse



def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('dataset', help='Required dataset to analyse')
        args = parser.parse_args()
        if args.dataset != "dataset_train.csv":
            raise AssertionError("Not entered the good file as parameter")
        
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
