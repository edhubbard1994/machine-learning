import csv
import numpy
from passenger import Passenger
from statistics import mean, median, stdev

#MATRIX = numpy.array()
PASSENGERS = dict()


def make_predictions():
    fares = list()
    for p_id, passenger in PASSENGERS.items():
        pass


def load_data():
    with open("titanic/test.csv") as file:
        data = csv.reader(file)
        for row in data:
            PASSENGERS[int(row[0])] = Passenger(
                int(row[0]),
                int(row[1]),
                int(row[4]),
                float(row[8])
            )
    file.close()




def load_survivers():
    with open("titanic/gender_submission.csv") as file:
        data = csv.reader(file)
        for row in data:
            try:
                passenger = PASSENGERS[int(row[0])]
                passenger.set_actual_survival(row[1])
            except Exception as e:
                print("no passenger with id" + row[0])

    file.close()








if __name__ == "__main__":
    load_data()
    load_survivers()