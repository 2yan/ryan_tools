
import pandas as pd
import numpy as np

class Encoder():

    num_data = None
    cat_data = None
    def __init__(self, fit = False):
        if type(fit) != type(False):
            self.fit(fit)
        return 
        
        
    def fit(self, iterable):
        vals = list(iterable)
        vals.insert(0, False)
        vals = list(set(vals))
        self.num_data = pd.Series(data = vals)
        self.cat_data = pd.get_dummies(vals, drop_first= True)
        self.cat_data[False] = 0
        return 

    def to_categorical(self, iterable):
        x = self.cat_data[iterable]
        x = x.values
        return x.T
    
    def from_categorical(self, cats):
        argmax = np.argmax(cats,axis = 1)
        result = self.from_numeric(argmax)
        return result
    
    def to_numeric(self, iterable):
        index = self.num_data.values
        vals = self.num_data.index
        temp = pd.DataFrame(data = vals, index = index)
        return temp.loc[iterable].values.T[0]
    
    def from_numeric(self, nums):
        result = self.num_data.loc[nums]
        return result.values
    
