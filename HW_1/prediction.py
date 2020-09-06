import csv
import numpy

#MATRIX = numpy.array()
FARE_INDEX = 8
PID_INDEX = 0

def load_data():
    with open("titanic/test.csv") as file:
        data = csv.reader(file)
        for row in data:
            print(row)







if __name__ == "__main__":
    load_data()