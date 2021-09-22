import pandas as pd
import os


def convert_to_csv(source):
    # Retrieving the current working directory
    cwd = os.getcwd()
    print(cwd)

    # File reading section
    try:
        print("\nReading file : "+source)
        data = pd.read_json(source)
        print("Read successful".center(50, "="))

    except:
        print("Error while reading the input file")

    # File converting section
    try:
        path = cwd+"python-project\json2csv\jsonAndcsv\data.csv"

        print("\nConverting file...")
        data.to_csv(path)
        print("File succesfully converting in : "+path+"\n")

    except:
        print("Error while converting the data to .csv")


if __name__ == "__main__":
    cwd = os.getcwd()
    print(cwd)
    json_file = cwd+"python-project\json2csv\jsonAndcsv\data.json"
    convert_to_csv(json_file)
