import streamlit as st
import os

#EDA packages
import pandas as pd
import numpy as np

#Visualization packages
#import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('Agg')
#import seaborn as sns

#Sidebar
st.sidebar.header("About me ""💬")

st.sidebar.markdown("""

Hi, my name is Marina. 
I'm a Data Science Student 
and this is my first Streamlit App.

You can find my LinkedIn and GitHub profile links below.

""")

st.sidebar.subheader("Social ""🙋‍♀")
st.sidebar.markdown("""

[LinkedIn](https://www.linkedin.com/in/marinahsborges/)

[GitHub](https://github.com/inaborges)

""")

st.sidebar.subheader("Goals for this project " "💜")

st.sidebar.markdown("""

- ❌ Put the buttons in the same row
- ❌ Create download datasets option
- :heavy_check_mark: Create choose dataset to display option
- :heavy_check_mark: Add charts

This project is part of the 10 weeks Data Science BootCamp, from [Codenation](https://codenation.dev/).


""")
#End of sidebar section


#Main app



st.image('milwaukee_city.jpg', width=680)
st.write(' ## Number of City-Owned Improved Properties by Year')
st.write("This apps is a data explorer for Milwaukee City Owned Houses sales and total management costs between 2014 and 2017.")
#st.write(" ## **Data Sample by Year** ")

def main():


    def file_selector(folder_path='./datasets'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Select a file", filenames)
        return os.path.join(folder_path, selected_filename)

    filename = file_selector()
    st.info("You selected {}".format(filename))

    #Read data function
    df = pd.read_csv(filename)

    #Show dataset
    if st.checkbox("Show Dataset"):
        number = st.number_input("Number of Rows to View",1)
        st.dataframe(df.head(number))

    #Show columns
    st.write("**Selected dataset column names**")
    if st.button("Column Names"):
        st.write(df.columns)

    #Show shape
    st.write("**Selected dataset shape**")
    if st.checkbox("Shape of Dataset"):
        data_dim = st.radio("Show dimension by", ("Rows","Columns"))
        if data_dim == 'Rows':
            st.text("Number of Rows")
            st.write(df.shape[0])
        elif data_dim == 'Columns':
            st.text("Number of Columns")
            st.write(df.shape[1])
        else:
            st.write(df.shape)



    #Select columns
    st.write("**Selected dataset columns**")
    if st.checkbox("Select columns to show"):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("Select", all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)

    #Show datatypes
    st.write("**Selected dataset datatypes**")
    if st.button("Data Types"):
        st.write(df.dtypes)


    #Plot and visualization
    st.subheader("Data Visualization")
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox("Select the type of Plot", ["area", "bar", "hist","kde"])
    selected_column_names = st.multiselect("Select Columns to Plot", all_columns_names)

    if st.button("Generate Plot"):
        st.success("Generating Customizable Plot of {} for {} ".format(type_of_plot, selected_column_names))

        #Plots by Streamlit:
        if type_of_plot == 'area':
            cust_data = df[selected_column_names]
            st.area_chart(cust_data)

        elif type_of_plot == 'bar':
            cust_data = df[selected_column_names]
            st.bar_chart(cust_data)

        elif type_of_plot:
            cust_plot = df[selected_column_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()



if __name__ == '__main__':
    main()





