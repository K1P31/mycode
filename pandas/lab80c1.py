#!/usr/bin/python3

"""" Write a few scripts that can transform data between JSON, CSV, and Excel. You are welcome to try other formats if you'd like. """


import pandas

def main():

    # create a dataframe from json
    df = pandas.read_json("5movies.json")

    # writeout dataframe to CSV
    df.to_csv("5movies-translated-from-json.csv")

if __name__ == "__main__":
    main()

