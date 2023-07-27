#This program must calculate the frequency of every item in the database and output it as a dictionary. 
import pandas as pd
class frequenciesOfItems():
    def __init__(self, database):
        self.database = database
    
    def calc(self):
        frequency_dict = {}
        for item in self.database:
            frequency_dict[item] = frequency_dict.get(item, 0) + 1
        return frequency_dict
    
    print('test')
    
    
if __name__=="__main__":
    
    df = pd.read_csv("PM24HeavyPollutionRecordingSensors.csv", header=None)
    
    df1 = pd.read_csv("/Users/nakazawagai/Documents/UOA/G4/python ds/ex11/stationInfo.csv")
    freq = frequenciesOfItems(df)
    dict = freq.calc()
    print(dict)