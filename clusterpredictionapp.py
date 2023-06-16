import pandas as pd
import numpy as np
import pickle
import streamlit as st

# load the model from disk
loaded_model = pickle.load(open("C:/Users/shrut/world_model.pkl", 'rb'))

input_data =pd.read_csv("C:/Users/shrut/Clustered_ World_Development_Data.csv")

# Write the function for prediction
def cluster_prediction(input_data):
   
    #changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance 
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        
        
    predict = loaded_model.predict(input_data_reshaped)
     
            
    if predict[0] == 2:
        return 'Developed country'
    elif predict[0] == 1:
        return 'Developing Country'
    else:
        return 'Under Developed Country'

    
# Define the Streamlit app
def main():
   

        # Set the app title
        st.title('Cluster Prediction For Global Development Measurement Data')
    
        
        # Getting input from user
        Country = st.text_input('Enter Country Name')
        Birth_Rate = st.text_input('Enter the Birth Rate ')
        Business_Tax_Rate=st.text_input('Enter the Business Tax Rate')
        CO2_Emissions = st.text_input('Enter the CO2 Emissions ')
        Days_to_Start_Business= st.text_input('Enter the Days to start business')
        Energy_Usage = st.text_input('Enter the Energy Usage')
        GDP = st.text_input('Enter the GDP')
        Health_ExpGDP= st.text_input('Enter the Health Expenditure % on GDP')
        Health_ExpCapita= st.text_input('Enter the Health Expenditure per Capita')
        Hours_to_do_Tax= st.text_input('Enter the Hours to do Tax')
        Infant_Mortality_Rate = st.text_input("Enter the Infant Mortality Rate (0-1)")
        Internet_Usage = st.text_input("Enter the Internet Usage  (0-1)")
        Lending_Interest= st.text_input('Enter the Lending Interest')
        Life_Expectancy_Female = st.text_input('Enter the Life Expectancy of Female')
        Life_Expectancy_Male= st.text_input('Enter the Life Expectancy of Male')
        Mobile_Phone_Usage = st.text_input("Enter the Mobile Phone Usage (0-1)")
        Population_0to14 = st.text_input("Enter the Value of % Population of Age between 0-14")
        Population_15to64 = st.text_input("Enter the value of % Population of Age between 15-64")
        Population_65plus = st.text_input("Enter the value of % Population of Age above 65")
        Population_Total = st.text_input("Enter the Total Population Count")
        Population_Urban = st.text_input("Enter the Value of % Population in Urban")
        Tourism_Inbound = st.text_input("Enter the Tourism Inbound")
        Tourism_Outbound = st.text_input("Enter the Tourism Outbound")


       # code for prediction
        cluster= ''

        if st.button('Clustering Prediction Result'):
           cluster = cluster_prediction([Birth_Rate,Business_Tax_Rate,CO2_Emissions,Days_to_Start_Business,Energy_Usage,GDP,Health_ExpGDP,Health_ExpCapita,Hours_to_do_Tax,Infant_Mortality_Rate,Internet_Usage,Lending_Interest,Life_Expectancy_Female,Life_Expectancy_Male,Mobile_Phone_Usage,Population_0to14,Population_15to64,Population_65plus,Population_Total,Population_Urban,Tourism_Inbound,Tourism_Outbound])
           
           st.success(cluster)
           
           
# Run the app
if __name__ == '__main__':
        main()


