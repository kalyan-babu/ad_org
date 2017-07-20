import os
import pandas as pd
import numpy as np
import process_test_data as test      
import process_train_data as train
from sklearn import tree


path = os.getcwd()+r'\data\output.csv'


trees= tree.DecisionTreeRegressor()

trees=trees.fit(train.dataset2,train.ad_view)

pred_trees=trees.predict(test.dataset)

pred_trees=np.array(pred_trees)
pred_trees=pred_trees.astype(int)


output=[]

for i in range(len(pred_trees)):
    output.append((test.vid_id[i],pred_trees[i]))

columns1=["vidid","adview"]

output=pd.DataFrame(output,columns=columns1)

output.to_csv(path,sep="\t",index=False)


pred_trees=pred_trees.astype(int)
pred_trees=pd.DataFrame(pred_trees)



 
