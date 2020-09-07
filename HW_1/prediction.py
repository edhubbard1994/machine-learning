"""
This script attempts to predict survival of a titanic passenger based on the
average fare paid by passengers.

"""

import csv
import numpy
from passenger import Passenger
from statistics import mean, median, stdev


PASSENGERS = dict()


def make_predictions():
    fares = list()
    for p_id, passenger in PASSENGERS.items():
        fares.append(passenger.fare)
    alpha = mean(fares)
    accurate_predictions = 0
    
    for p_id, passenger in PASSENGERS.items():
        accurate_predictions = accurate_predictions + int(passenger.predict(alpha))
    print("There were {} accurately predicted survivors of {}".format(
        accurate_predictions,
        len(PASSENGERS)))
    percent = (accurate_predictions/len(PASSENGERS)) * 100
    print("\n this is a {} % accuracy \n\n".format(percent))


def load_data():
    with open("titanic/test.csv") as file:
        data = csv.reader(file)
        count = 0
        for row in data:
            if count > 0:
                try:
                    PASSENGERS[int(row[0])] = Passenger(
                        int(row[0]),
                        int(row[1]),
                        float(row[8])
                    )
                except:
                    pass
            count = count + 1
    file.close()


def load_survivers():
    with open("titanic/gender_submission.csv") as file:
        data = csv.reader(file)
        count = 0
        for row in data:
            if count > 0:
                try:
                    passenger = PASSENGERS[int(row[0])]
                    passenger.set_actual_survival(row[1])
                except Exception as e:
                    pass # passenger does not have fare
            count = count + 1
    file.close()



if __name__ == "__main__":
    load_data()
    load_survivers()
    make_predictions()