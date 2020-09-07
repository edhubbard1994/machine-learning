


class Passenger:

    def __init__(self,p_id, p_class, age, fare,survived):
        self.p_id = p_id
        self.p_class = p_class
        self.age = age
        self.fare = fare
        self.survived = bool(survived)
        self.predicted_to_survive = False 

    #each member caluculates its own prediction with pre computed alpha
    def predict(self, alpha):
        if self.fare > alpha:
            self.predicted_to_survive = True
    
    def __call__(self):
        return self.predicted_to_survive
            


        

