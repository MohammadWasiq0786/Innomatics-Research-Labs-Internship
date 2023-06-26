import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Home")
df=pd.read_csv('open_pubs2.csv')

st.title("Mohammad Wasiq")
st.markdown("## Innomatics Research Labs Feb-2023 Internship Project")
st.write("## Connect me on Linkedin [link](https://www.linkedin.com/in/mohammadwasiq0/)")
st.write("## Follow me on Github [link](https://github.com/mohammadwasiq0)")

# st.sidebar.success("navigate pages ^ ")
st.title(" Nearest Pub to Me")

img = Image.open("EDA.PNG") 
st.image(img)
         
st.text('''Let’s assume you are on a Vacation in the United Kingdom with your friends. Just for 
some fun, you decided to go to the Pubs nearby for some drinks. Google Map 
is down because of some issues. 

While searching the internet, you came across https://www.getthedata.com/open-pubs. 
On this website, you found all the pub locations (Specifically Latitude 
and Longitude info). 
In order to impress your friends, you decided to create a Web Application 
with the data available in your hand. 
''')

st.header("Available DataSet: ")
st.dataframe(df)

rows = df.count()[0]
columns = df.shape[1] - 1
st.subheader(f'Total Number of Rows in the data are : {rows}')
st.subheader(f'Total Number of Columns in the data are : {columns}')

st.subheader('Satistical Analysis (Five Number Summary) of Data')    
st.dataframe(df.describe())


st.subheader('Covariance in Dataset')
st.dataframe(df.cov())

st.subheader('Correlation')  
st.dataframe(df.corr())

fig, ax = plt.subplots()
sns.heatmap(df.corr(), annot=True,  ax=ax)
st.write(fig)
