import pandas as pd
import numpy as np
from numpy import array
import os


#Calculating the duration in seconds
def find_time(data,result,header):
    result1=[]
    value=[]
    sum2=0
    for i in range(len(dataset)):
       
        sum1=0.0
        if result.iloc[i][2]=="M":
            sum1+=result.iloc[i][1]*60
            if result.iloc[i][5]=="S":
                sum1+=result.iloc[i][4]
        elif result.iloc[i][2]=="H":
            sum1+=result.iloc[i][1]*60*60
            if result.iloc[i][5]=="M":
                sum1+=result.iloc[i][4]*60
                if result.iloc[i][8]=="S":
                    sum1+=result.iloc[i][7]
            if result.iloc[i][5]=="S":
                sum1+=result.iloc[i][4]
        else:
            sum1+=result.iloc[i][1]
        result1.append(sum1)
        
        # Assigning interger values based on the category of the video
        
        if header[i]=="A":
            value.append(1)
            sum2+=1
        if header[i]=="B":
            value.append(2)
            sum2+=1
        if header[i]=="C":
            value.append(3)
            sum2+=1
        if header[i]=="D":
            value.append(4)
            sum2+=1
        if header[i]=="E":
            value.append(5)
            sum2+=1
        if header[i]=="F":
            value.append(6)
            sum2+=1
        if header[i]=="G":
            value.append(7)
            sum2+=1
        if header[i]=="H":
            value.append(8)
            sum2+=1
 
    return result1,value
    

path = os.getcwd()+r'\data\train.csv'
dataset1=pd.read_csv(path)
dataset1 = dataset1.convert_objects(convert_numeric=True)



result = dataset1['duration'].str.split('(\d+)([A-z]+)', expand=True)

dataset=dataset1[["adview","views","likes","dislikes","comment"]]

header=dataset1["category"]


#changing the dtype for  time calculation
result[1] = result[1].astype(float)
result[4] = result[4].astype(float)
result[7] = result[7].astype(float)

result1,value=find_time(dataset,result,header)

#adding duration column to dataset
dataset["duration"]=result1

 

dataset["comment"].fillna(0, inplace=True)
dataset["likes"].fillna(0, inplace=True)
dataset["dislikes"].fillna(0, inplace=True)
dataset["views"].fillna(0, inplace=True)

dataset2=dataset[["views","likes","dislikes","comment","duration"]]


ad_view=dataset["adview"]

#adding category in integer form
dataset2["category"]=value       





        



    


