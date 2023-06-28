from pickle import load
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_percentage_error
import seaborn as sns
import os



# loading the data using the address from os
basedir = os.path.dirname(__file__)
filename = basedir+"/data/diamonds.csv"

df = pd.read_csv(filename)
oe_load = load(open(basedir+'/data/ordinal_encoder.pkl', 'rb'))
sc_load = load(open(basedir+'/data/std_scaler.pkl', 'rb'))
dt_load = load(open(basedir+'/data/decision_tree.pkl', 'rb'))

st.title('Model')
'Please fill all the inputs.'

with st.form('my_form'):
    carat = st.number_input(label='Input your carat', min_value=0.02, max_value=5.2)
    x = st.number_input(label='Enter length of diamond',min_value=0.01, max_value=11.0)
    cut = st.selectbox(label='Select finish of your diamond', options=df.cut.unique())
    color = st.selectbox(label='Select color of your diamond', options=df.color.unique())
    clarity= st.selectbox(label='Select clarity level of your diamond', options=df.clarity.unique())
    
    btn = st.form_submit_button(label='Predict')

if btn:
    if carat and x and cut and color and clarity:
        query_num = pd.DataFrame({'carat':[carat], 'x':[x]})
        query_cat = pd.DataFrame({'cut':[cut], 'color':[color], 'clarity':[clarity]})
        query_num = sc_load.transform(query_num)
        query_cat = oe_load.transform(query_cat)
        
        query_point = pd.concat([pd.DataFrame(query_num), query_cat], axis=1)
        out = dt_load.predict(query_point)

        st.success(f"This diamond would cost you $ {round(out[0],2)}")
        st.balloons()


    else:
        st.error('Enter all the values')
        st.snow()

