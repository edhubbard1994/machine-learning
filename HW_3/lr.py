from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

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
    print(classifier)   
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


if __name__ == "__main__":
    data_tuple = load_dataset()
    training_data = get_training_data(data_tuple)
    LR = LogisticRegression()
    train_model(LR,training_data)

    print("the accuracy of the prediction using Logistic Regression is:")
    print(predict(LR, data_tuple))

    print("the accuracy of the altered prediction using Logistic Regression is:")
    print(predict_altered(LR, data_tuple))



