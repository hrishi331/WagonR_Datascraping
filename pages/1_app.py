import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


st.header("WagonR Resale-Price Analysis")
df = pd.read_csv('database/WagonR_DB_Cleaned1.csv')


years = st.multiselect(label='Select make year',options=sorted(df['Year'].unique()))
df = df[df['Year'].isin(years)]


location = st.multiselect(label='Select one or more location',options=sorted(df['Location'].unique()))
df = df[df['Location'].isin(location)]

variant = st.multiselect(label='Select one or more variant',options=sorted(df['Variant'].unique()))
df = df[df['Variant'].isin(variant)]

fuel = st.multiselect(label='Select one or more fuel type',options=sorted(df['Fuel'].unique()))
df = df[df['Fuel'].isin(fuel)]

km_driven = st.multiselect(label='Select one or more KM driven',options=sorted(df['KM driven'].unique()))
df = df[df['KM driven'].isin(km_driven)]

entries = df.shape[0]
mean_price = df['Price'].mean()
max_price = df['Price'].max()
min_price = df['Price'].min()
fig = plt.figure(figsize=[10,5])
sns.barplot(df['Price'].value_counts())
plt.xlabel('ResalePrice')
plt.ylabel('Count')
plt.xticks(rotation=90)


if st.button(label="Analyze"):
    st.subheader("RESULTS")
    st.write('For selected parameters')
    st.write(f'1. Total entries found : {entries}')
    st.write(f'2. Mean price : {mean_price}')
    st.write(f'3. Max price : {max_price}')
    st.write(f'4. Min price : {min_price}')
    st.write('5. Barplot')
    st.pyplot(fig)
    
    
    

