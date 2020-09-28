import pandas
import numpy
from functools import reduce

from preceptron import Perceptron





def linear_seperable():
    t = numpy.array([
        [2,20],
        [1,10],
        [3,30],
        [2,20],
        [1,10],
        [2,2],
        [1,1],
        [5,5],
        [2,2],
        [1,1]
    ])
    w = numpy.array([1,0])
    p = Perceptron()
    p.fit(t,w)
    print(p.net_input(t))
    print(p.predict(t,1))


def nonlinear_seperable():
    t = numpy.array([
        [2,20],
        [2,20],
        [2,20],
        [2,20],
        [2,20],
        [2,20],
        [2,20],
        [2,20],
        [2,20],
        [2,20]
    ])
    w = numpy.array([1,1])
    p = Perceptron()
    p.fit(t,w)
    print(p.net_input(t))
    print(p.predict(t,1))

def titanic():
    df_train = pandas.read_csv("titanic/train.csv",",")
    df_test =  pandas.read_csv("titanic/test.csv",",")
    
    df_train = df_train.fillna(0)
    df_test = df_test.fillna(0)
    transform = {"male":-1, "female": 1}
    df_sex = df_train["Sex"].apply(lambda x: transform[x])
    df_age = df_train["Age"].apply(
        lambda x: 
            int(bool(int(x) <= 50 or int(x) > 18))
    )
    np_train_sex = df_sex.to_numpy() 
    np_train_age = df_age.to_numpy()
    np_train = numpy.stack((np_train_age,np_train_sex), axis=1)
    p = Perceptron()
    p.fit(np_train,[1,-1])

    
    df_sex2 = df_test["Sex"].apply(lambda x: transform[x])
    df_age2 = df_test["Age"].apply(
        lambda x: 
            int((int(x) <= 50 or int(x) > 18))
    )

    np_train_sex2 = df_sex2.to_numpy() 
    np_train_age2 = df_age2.to_numpy()
    np_train2 = numpy.stack((np_train_age2,np_train_sex2), axis=1)
    print(p.net_input(np_train2))
    prediction = p.predict(np_train2,0,True)


    survived = pandas.read_csv("titanic/gender_submission.csv")["Survived"].to_numpy()
    prediction = numpy.where(prediction==-1,0,prediction)
    results = numpy.stack((survived,prediction),1)
    print(results)
    tot = []
    for i in results:
        if i[0] == i[1]:
            tot.append(1)
        else:
            tot.append(0)
    total = reduce(add_up,tot, 0)
    print(total/len(tot) * 100)
    
def add_up(x,y):
    return x + y
if __name__ == "__main__":
    linear_seperable()
    print("+++")
    nonlinear_seperable()
    titanic()