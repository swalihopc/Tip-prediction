import streamlit as st 
import pickle
import pandas as pd

with open('model.pkl','rb') as model_file:
    model=pickle.load(model_file)
    
st.title('Tips Prediction App')

total_bill=st.number_input('total_bill')    
size=st.number_input('size',min_value=1,max_value=10,value=2)
sex=st.selectbox('sex',['Male','Female'])
smoker=st.selectbox('smoker',['yes','no'])
day=st.selectbox('Day',['Thur','Fri','Sat','sun'])
time=st.selectbox('Time',['Lunch','Dinner'])

input_data=pd.DataFrame({
    'total_bill':[total_bill],
    'sex':[sex],
    'smoker':[smoker],
    'day':[day],
    'time':[time],
    'size':[size],
})

sex_mapping={'Male':0,'Female':1}
smoker_mapping={'No':0,'Yes':1}
day_mapping={'Thur':0,'Fri':1,'set':2,'Sun':3}
time_mapping={'Lunch':0,'Dinner':1}

input_data['sex']=input_data['sex'].map(sex_mapping)
input_data['smoker']=input_data['smoker'].map(smoker_mapping)
input_data['day']=input_data['day'].map(day_mapping)
input_data['time']=input_data['time'].map(time_mapping)

if st.button('Predict Tip'):
    predition=model.predict(input_data)
    st.write(f"predited Tip:${round(predition[0],2)}")
    
    