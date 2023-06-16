# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 18:54:11 2023

@author: shrut
"""

import pandas as pd
import numpy as np
import pickle

# load the model from disk
loaded_model = pickle.load(open("C:/Users/shrut/world_model.pkl", 'rb')) 

input_data =pd.read_csv("C:/Users/shrut/Clustered_ World_Development_Data.csv")

# write the function for pca
def cluster_prediction(input_data):
   
    #changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance 
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        
        
    predict = loaded_model.predict(input_data_reshaped)
     
            
    if predict[0] == 2:
        print ('Developed country')
    elif predict[0] == 1:
        print ('Developing Country')
    else:
        print ('Under Developed Country')


