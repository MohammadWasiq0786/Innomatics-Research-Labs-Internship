import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import home
df=pd.read_csv('open_pubs2.csv')
st.set_page_config(page_title="Nearest Pubs")

lat=st.number_input('latitude')
lon=st.number_input('longitude')
new_df=df[['latitude','longitude']]
inputs=np.array([lat,lon])
distance=np.sqrt(np.sum((inputs-new_df)**2, axis=1))
k = 5
nearest_neighbor = distance.argsort()[:k]

if st.button('Find'):
    st.text("5 nearest pubs for you are: ")
    st.map(df.iloc[nearest_neighbor])
    st.dataframe(df.iloc[nearest_neighbor])