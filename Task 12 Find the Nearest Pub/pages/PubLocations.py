import streamlit as st
import pandas as pd
import numpy as np
import home
df=pd.read_csv('open_pubs2.csv')
st.set_page_config(page_title="Pub Locations")
opt=st.selectbox('',('Local Authority','Postal Code'))
if opt=='Local Authority':
    option=st.selectbox(opt,df.local_authority.unique())

    if st.button("Find"):
        pubs_data = df.loc[df["local_authority"]==option]
        "You searched for:",option
        "Total no of pubs in this location is:",len(pubs_data)
        st.map(pubs_data)
        st.dataframe(pubs_data)
else:
    pc=st.selectbox(opt,df.postcode.unique())

    if st.button("Find"):
        pubs_data = df.loc[df["postcode"]==pc]
        "You searched for:",pc
        "Total no of pubs in this location is:",len(pubs_data)
        st.map(pubs_data)
        st.dataframe(pubs_data)
