import pandas as pd
import streamlit as st

#st.sidebar.header("Choose the year")



st.image('milwaukee_city.jpg', width=680)
st.write(' ## Number of City-Owned Improved Properties by Year')
st.write("This apps is a walk trough Milwaukee City Owned Houses sales and total management costs between 2014 and 2017")
st.write(" ## **Data Sample by Year** ")

#Data Sample and buttons 2014
st.subheader('2014')

data2014: object = pd.read_csv('2014-improved-property-sales.csv')
st.write(data2014.head())

total_sales_14 = data2014['Sale Price'].sum().round()
total_cm_2014 = data2014['Total Mgt. Expenses'].sum().round()
year_r_2014 = total_sales_14 - total_cm_2014

if st.button('Total Sales'):
    st.write(total_sales_14)

if st.button('Total Management Expenses'):
    st.write(total_cm_2014)

if st.button('Years Result'):
    st.write(year_r_2014)

#Data Sample and buttons 2015
st.subheader('2015')

data2015: object = pd.read_csv('2015-improved-property-sales.csv')
st.write(data2015.head())

total_sales_15 = data2015['Sale Price'].sum().round()
total_cm_2015 = data2015['Total Mgt. Expenses'].sum().round()

st.subheader('2016')

data2016: object = pd.read_csv('2016-improved-property-sales.csv')
st.write(data2016.head())

st.subheader('2017')

data2017: object = pd.read_csv('2017-improved-property-sales.csv')
st.write(data2017.head())