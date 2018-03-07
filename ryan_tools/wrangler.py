
import pandas as pd
import numpy as np

class Encoder():
    data = None
    def __init__(self, blank = False):
        self.data = pd.DataFrame(columns = ['value', 'number'])
        self.data.loc[0, 'value'] = blank
        self.data.loc[0, 'number'] = 0
        
    def set_blank(self, blank):
        self.data.loc[0, 'value'] = blank
    
    def fit(self, iterable):
        unique_values = set(iterable) - set(self.data['value'].values)
        i = self.data['number'].max() + 1
        for value in unique_values:
            self.data.loc[i, 'number'] = i
            self.data.loc[i, 'value'] = value
            i = i + 1
    
    def to_nums(self, iterable):
        result =np.zeros(len(iterable))
        temp = self.data.copy()
        temp.set_index('value', inplace = True)
        
        for i, thing in enumerate(iterable):
            result[i] = temp.loc[thing, 'number']
        return result
            
    def from_nums(self, iterable):
        result = []
        temp = self.data.copy()
        for i, thing in enumerate(iterable):
            result.append(temp.loc[thing, 'value'])
        return np.array(result)

    def to_categorical(self, labels = None, iterable = None):
        if type(labels) == type(None):
            labels = self.to_nums(iterable)
        empty = np.zeros((len(labels),self.data['number'].max()))
        for i, label in enumerate(labels.astype(int)):
            if label != 0:
                empty[i][label - 1] = 1
        return empty
    
    def from_categorical(self, categoricals, to_nums = False):
        labels = np.zeros(len(categoricals))
        for i, row in enumerate(categoricals):
            labels[i] = np.argmax(row) + np.sum(row)
        if to_nums:
            return labels
        return self.from_nums(labels)
    
