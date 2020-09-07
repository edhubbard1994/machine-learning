import csv
import numpy
from statistics import mean, median, stdev

#MATRIX = numpy.array()
SURVIVERS = dict()
FARE_INDEX = 8
PID_INDEX = 0
FARES = list()
FARE_METRICS = dict()

def compare_data():
    pass

def load_data():
    with open("titanic/test.csv") as file:
        data = csv.reader(file)
        for row in data:
            FARES.append(row[FARE_INDEX])
    file.close()




def load_survivers():
    with open("titanic/gender_submission.csv") as file:
        data = csv.reader(file)
        for row in data:
            SURVIVERS[row[0]] = row[1]
    file.close()
    print(SURVIVERS)








if __name__ == "__main__":
    load_survivers()