from select import select
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import os



# loading the data using the address from os
basedir = os.path.dirname(__file__)
filename = basedir+"/data/diamonds.csv"

df = pd.read_csv(filename)
st.title('Bivariate Analysis')
# "**Bivariate Analysis**"

'Since the boxplot shows that most of the features have outliers thus median would be good choice for central tendency'

'**Barchart shown below is controled with features in the sidebar**'
opt = st.sidebar.selectbox(label='Select any categorical feature', options=df.select_dtypes(include='object').columns)
fig = px.bar(df.groupby(opt).median().price,labels={'value':'price'}, text_auto=True, title=f'Median price across {opt}').update_xaxes(categoryorder='total descending')
st.write(fig)



"* Fair cut diamonds has highest median price followed by premium cut followed by good cut."
"* J colored diamonds has highest median price followed by I colored followed by H colored where as E colored diamonds have the least median price."
"* SI2 clarity diamond has highest median price followed by I1 followed, by SI1 clarity followed  where as IF colored diamonds has least median price."
'**Boxplot shown below is controled with features in the sidebar**'
fig = px.box(df, x=opt, y='price', title=f'Boxplot: {opt} vs price')
st.write(fig)
'* Price has good variation across various clarity levels.'
"* Price has good variation across various colors."

opt2 = st.selectbox(label='Select any continuous feature', options=['carat', 'x'])
fig = px.scatter(df, x=opt2, y='price', title=f'Scatterplot {opt2} vs price')
st.write(fig)
'* Carat has good correlation with price'
'* X has good correlation with price'

'**Correlation Heatmap**'
#########################################################
# fig = plt.figure(figsize=(15,10))
# sns.heatmap(data, mask= np.triu(data,1), annot=True)
# st.pyplot(fig)
############################################################
data = df.corr()
st.write(px.imshow(data, text_auto = '.2f', aspect='auto', color_continuous_scale='viridis'))
'* Price has very good correlation with carat, x, y and z features'
###############################################################

# making sns plots in streamlit
# fig = plt.figure(figsize=(15, 12))
# for i, col in enumerate(df.select_dtypes(exclude='object')):
#     plt.subplot(4, 3, i+1)
#     sns.boxplot(df[col])
    # plt.tight_layout()

# st.write(fig)
##############################################################

st.header('Feature Selection for model:')
