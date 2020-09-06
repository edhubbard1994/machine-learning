import csv
import numpy

#MATRIX = numpy.array()
SURVIVERS = dict()
FARE_INDEX = 8
PID_INDEX = 0
FARES = list()

def load_data():
    with open("titanic/test.csv") as file:
        data = csv.reader(file)
        for row in data:
            print(row)




def load_survivers():
    with open("titanic/gender_submission.csv") as file:
        data = csv.reader(file)
        for row in data:
            SURVIVERS[row[0]] = row[1]
        print(SURVIVERS)








if __name__ == "__main__":
    load_survivers()