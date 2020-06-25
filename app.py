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

total_sales_2014 = data2014['Sale Price'].sum().round()
total_cm_2014 = data2014['Total Mgt. Expenses'].sum().round()
year_r_2014 = total_sales_2014 - total_cm_2014

if st.button('Total Sales 2014'):
    st.write(total_sales_2014)

if st.button('Total Management Expenses 2014'):
    st.write(total_cm_2014)

if st.button('2014 Years Result'):
    st.write(year_r_2014)

#Data Sample and buttons 2015
st.subheader('2015')

data2015: object = pd.read_csv('2015-improved-property-sales.csv')
st.write(data2015.head())

total_sales_2015 = data2015['Sale Price'].sum().round()
total_cm_2015 = data2015['Total Mgt. Expenses'].sum().round()
year_r_2015 = total_sales_2015 - total_cm_2015

if st.button('Total Sales 2015'):
    st.write(total_sales_2015)

if st.button('Total Management Expenses 2015'):
    st.write(total_cm_2015)

if st.button('2015 Years Result'):
    st.write(year_r_2015)

#Data Sample and buttons 2016
st.subheader('2016')

data2016: object = pd.read_csv('2016-improved-property-sales.csv')
st.write(data2016.head())

total_sales_2016 = data2016['Sale Price '].sum().round()
total_cm_2016 = data2016['Total Mgt. Expenses'].sum().round()
year_r_2016 = total_sales_2016 - total_cm_2016

if st.button('Total Sales 2016'):
    st.write(total_sales_2016)

if st.button('Total Management Expenses 2016'):
    st.write(total_cm_2016)

if st.button('2016 Years Result'):
    st.write(year_r_2016)

#Data Sample and buttons 2017
st.subheader('2017')

data2017: object = pd.read_csv('2017-improved-property-sales.csv')
st.write(data2017.head())

total_sales_2017 = data2017['Sale Price '].sum().round()
total_cm_2017 = data2017['Total Mgt. Expenses'].sum().round()
year_r_2017 = total_sales_2017 - total_cm_2017

if st.button('Total Sales 2017'):
    st.write(total_sales_2017)

if st.button('Total Management Expenses 2017'):
    st.write(total_cm_2017)

if st.button('2017 Years Result'):
    st.write(year_r_2017)