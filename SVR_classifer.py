import os
import pandas as pd
import numpy as np
from numpy import array
import process_test_data as test      
import process_train_data as train
from sklearn.svm import SVR


path = os.getcwd()+r'\data\output.csv'

svr = SVR(kernel='rbf',C=100000,gamma=0.00005,cache_size=1000)


svr.fit(train.dataset2,train.ad_view)

pred_SVR = svr.predict(test.dataset)

pred_SVR=np.array(pred_SVR)

pred_SVR=pred_SVR.astype(int)

output=[]

for i in range(len(pred_SVR)):
    if pred_SVR[i]<1:
        output.append((test.vid_id[i],1))
    else:
        output.append((test.vid_id[i],pred_SVR[i]))


output=pd.DataFrame(output)

columns1=["vidid","adview"]


output.to_csv(path,index=False,columns=columns1,sep=" ",delimiter=" ")
 
