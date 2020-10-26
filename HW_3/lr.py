from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
import numpy as np
import pandas as pd
from math import sqrt

def load_dataset():
    dataset = pd.read_csv("Grocery_Stores_-_2013.csv", delimiter=",")

    X = dataset.loc[:,"SQUARE FEET"].to_numpy()
    y = dataset.loc[:,"LATITUDE"].to_numpy()
    return [X,y]
    

def get_training_data(X_y):
    X = np.nan_to_num(X_y[0],nan=0)
    y = np.nan_to_num(X_y[1],nan=0)
    X_size = len(X)/3
    y_size = len(y)/3
    X_train = X[0:int(X_size)]
    y_train = y[0:int(y_size)]
    return (X_train, y_train)

def train_model(LR,data):
    classifier = []
    final_data = []
    count = 0
    for i in data[1]:
        final_data.append([data[0][count],i])
        if i < 41.8781 and data[0][count] > 11000 :
            classifier.append(1)
        else:
            classifier.append(0)
        count = count + 1 
    LR.fit(np.array(final_data), np.array(classifier))

def predict(LR, data):
    classifier = []
    final_data = []
    data[0] = np.nan_to_num(data[0],nan=0)
    data[1] = np.nan_to_num(data[1],nan=0)
    count = 0
    for i in data[1]:
        final_data.append([data[0][count],i])
        if i < 41.8781 and data[0][count] > 11000 :
            classifier.append(1)
        else:
            classifier.append(0)
        count = count + 1
    return compare(classifier, LR.predict(np.array(final_data)))

def predict_altered(LR, data):
    classifier = []
    final_data = []
    data[0] = np.nan_to_num(data[0],nan=0)
    data[1] = np.nan_to_num(data[1],nan=0)
    count = 0
    for i in data[1]:
        final_data.append([data[0][count],i])
        if i < 41.8307 and data[0][count] > 11000 :
            classifier.append(1)
        else:
            classifier.append(0)
        count = count + 1
    return compare(classifier, LR.predict(np.array(final_data)))

def compare(real, predicted):
    count = 0
    acc = 0
    for i in real:
        if i == predicted[count]:
            acc = acc + 1
        count = count + 1
    return acc / count

def euclidean_distance(x, y):
    distance = 0.0
    for i in range(len(y)-1):
	    distance += (x[i] - y[i])**2
    return sqrt(distance)

def neighbors(train, test_row, num_neighbors):
    final_train_data = []
    final_test_data = []
    count = 0
    for i in train[1]:
        final_train_data.append([train[0][count],i])
        count = count + 1 
    count = 0
    for i in test_row[1]:
        final_test_data.append([test_row[0][count],i])
        count = count + 1 

    distances = list()
    for train_row in final_train_data:
        dist = euclidean_distance(final_test_data[0], final_train_data[1])
        distances.append((train_row, dist))
        distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors



if __name__ == "__main__":
    data_tuple = load_dataset()
    training_data = get_training_data(data_tuple)
    LR = LogisticRegression()
    DC_mf = DummyClassifier(strategy="most_frequent")
    DC_sf = DummyClassifier(strategy="stratified")

    train_model(LR,training_data)
    train_model(DC_mf,training_data)
    train_model(DC_sf,training_data)

    print("the accuracy of the prediction using most frequent Dummy Classifier:")
    print(predict(DC_mf, data_tuple))

    print("the accuracy of the prediction using stratified Dummy Classifier:")
    print(predict(DC_sf, data_tuple))


    print("the accuracy of the prediction using Logistic Regression is:")
    print(predict(LR, data_tuple))

    print("the accuracy of the altered prediction using Logistic Regression is:")
    print(predict_altered(LR, data_tuple))
    
    print("k nearest neighbors prediction is:")
    neighbors_found = neighbors(training_data, data_tuple,5)
    output_values = [row[-1] for row in neighbors_found]
    print( max(set(output_values), key=output_values.count))


