import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import os


# loading the data using the address from os
basedir = os.path.dirname(__file__)
filename = basedir+"/pages/data/diamonds.csv"

df = pd.read_csv(filename)
# making two columns left and right
left, right = st.columns(2)

st.title('Diamonds Price Prediction & Historical EDA by Mohamamd Wasiq')

st.write("## Connect me on Linkedin [Link](https://www.linkedin.com/in/mohammadwasiq0/)")
st.write("## Follow me on Github [Link](https://github.com/mohammadwasiq0)")

st.header('**Problem Statement**')
'The diamond processing firm wants a model that can predict the price of the model based on its properties such as carat, color, cut, clarity and its size.'
st.subheader('EDA of the diamonds dataset')
# exp =st.expander(label='expand this to read')
# exp.text('this is the expander')


# Univariate Analysis
st.subheader('**Univariate analysis**')


rd = st.radio(label='Show DataFrame', options= ['Top 5', 'Bottom 5', 'Complete data'] )
if rd=='Top 5':
    st.write(df.head(5))
elif rd== 'Bottom 5':
    st.write(df.tail(5))

else:
    st.write(df)


cb = st.checkbox(label='Show all info')
if cb:
    st.write(f'* There are {len(df.columns)} features in the dataset')
    st.write(f'* There are {df.shape[0]} rows in the dataset')
    st.write(f'* There are no null values in the dataset.')

# Data Description
cb = st.checkbox(label='Data Description')
if cb:
    st.write('Data Description')
    st.write(df.describe())
    st.write("* The mean and median of price is \$ 3932 and \$ 2401 respectively which shows the mean is affected by outliers.\n * The 25% diamonds are priced below $ 950.")
# univariate plots
"**Distribution**"
opt = st.selectbox(label='Select Categorical Features', options=df.select_dtypes(include='object').columns)
fig = px.histogram(df, x=opt)


fig = px.bar(round(df[opt].value_counts(normalize=True)*100,2), labels={'value': 'percent', 'index':opt}, title=f'Distribution across {opt}')
st.plotly_chart(fig)
'* 40% diamonds are having ideal cut, followed by 25% premium cut and there are less than 5% diamonds having fair cut.'
'* Almost 21% diamonds are G colored, followed by 18% E colored, followed by 17.69% F colored and just 5% diamonds have J color.'
'* Almost 24% diamonds have SI1 clarity followed by, 22% VS2 clarity followed by, 17% S12 clarity and I1 clarity is the rarest.'


"**Histogram and Boxplot**"

options = st.selectbox(label='Select Continuous Features', options=df.select_dtypes(exclude='object').columns)

l, r = st.columns(2)
fig = px.histogram(df, x=options, title=f'Distribution across {options}')
st.write(fig)

fig = px.box(df, x=options, title=f'Boxplot of {options}')
st.write(fig)

'* The price is log normaly distributed.'
'* The depth has high kurtosis.'
'* Rest other features have bimodal distributions.'
'* All the features have outliers thus median would be a good metric for central tendency.'
