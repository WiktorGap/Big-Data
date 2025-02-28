import pandas as pd 
import numpy as np 
import csv


data = pd.read_csv('data_01.csv',header=None,names=['timestamp','id','data timestamp type1','data timestamp type2','district','surname', 'outiliers val','outiliers val1','outiliers val minus','outiliers val plus','x','y','z'])
#data.columns=['timestamp','id','data timestamp type1','data timestamp type2','outiliers val','outiliers val','outiliers val minus','outiliers val plus','x','y','z']
#df = pd.DataFrame(data) #columns=['timestamp','id','data timestamp type1','data timestamp type2','outiliers val','outiliers val','outiliers val minus','outiliers val plus','x','y','z'])
#print(data)


def printCol(idx):
    print(data.loc[data.index[idx], "district"]) #->sama wartosc z konkretnej  kolumny
    print("--------")





def printRow(idx):
    print(data.loc[[idx]]) #->sum  cały wiersz 

def printCol(begin,end,idx_of_col):
    print(data.iloc[begin:end,idx_of_col]) #->wiersz kolumna , zakres wiersza 


print(data.aggregate(["sum"]))




#print(data.loc[data['id']=="2003000"])

#print(data[data['id'] == 2003000])

#printCol(2,6,3)



# with open("" )as csv_file: 
#     # read the csv file 
#     csv_reader = csv.reader(csv_file) 
  
#     # now we can use this csv files into the pandas 
#     df = pd.DataFrame([csv_reader], index = None) 
  
# # iterating values of first column  
# for val in list(df[1]): 
#     print(val) 
    