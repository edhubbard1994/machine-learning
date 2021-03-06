"""
Passenger class for better code organization 
"""


class Passenger:

    def __init__(self,p_id, p_class, fare):
        self.p_id = p_id
        self.p_class = p_class
        self.fare = fare
        self.survived = False
        self.predicted_to_survive = False 

    #each member caluculates its own prediction with pre computed alpha
    def predict(self, alpha):
        if self.fare > alpha:
            self.predicted_to_survive = True
        #print("passenger:{} predicted survival = {} and the actual survival = {}".format(self.p_id,self.predicted_to_survive,self.survived))
        return self.predicted_to_survive == self.survived


    def set_actual_survival(self, did_survive):
        self.survived = bool(did_survive)
    
    def __call__(self):
        return self.predicted_to_survive
            


        

