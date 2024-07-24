import streamlit as st
import pandas as pd

# Load data
url = 'https://raw.githubusercontent.com/singhrau0/Big-Data-Preprocessing/main/Leads.csv'
dff = pd.read_csv(url)

# Data Preprocessing
initial_nulls = dff.isnull().sum()
num_cols = len(list(dff.columns))

kf = [len(list(dff[i].unique())) for i in list(dff.columns) if dff[i].isnull().sum() > 0]
kf_mode = [dff[i].mode()[0] for i in list(dff.columns) if dff[i].isnull().sum() > 0]
kg = [i for i in list(dff.columns) if dff[i].isnull().sum() > 0]

[dff[col].fillna(value=val, inplace=True) for col, val in zip(kg, kf_mode)]

value_each_column = [dff[i].value_counts() for i in list(dff.columns)]
dff.drop(columns=[i for i in list(dff.columns) if ((dff[i].value_counts()[dff[i].value_counts().index[0]] / len(dff)) * 100 >= 90)], inplace=True)

dff['Lead Source'].replace({'google': 'Google'}, inplace=True)
dff['Specialization'].replace({'Select': 'Unknown'}, inplace=True)
dff['Lead Profile'].replace({'Select': 'Others'}, inplace=True)
dff['City'].replace({'Select': 'Unknown'}, inplace=True)
dff.drop(columns=['How did you hear about X Education'], inplace=True)

# Streamlit App
st.title("Leads Data Analysis")

st.header("Initial Data Overview")
st.write("This section displays the first few rows of the dataset to give an initial overview of the data.")
st.write(dff.head())

st.header("Null Values Analysis")
st.write("This section shows the number of null values in each column before any preprocessing.")
st.write(initial_nulls)

st.header("Number of Unique Values in Columns with Nulls")
st.write("This section lists the number of unique values in columns that contain null values. This helps to understand the diversity of data in these columns.")
st.write(kf)

st.header("Mode Values Used for Filling Nulls")
st.write("This section shows the mode (most frequent) values used to fill null values in columns. Filling nulls with mode values is a common technique in data preprocessing.")
st.write(kf_mode)

st.header("Columns with Null Values")
st.write("This section lists the columns that had null values and were filled with mode values.")
st.write(kg)

st.header("Value Counts After Null Handling")
st.write("This section provides the value counts for each column after null values have been handled. It helps to verify that null values were appropriately replaced.")
st.write(value_each_column)

st.header("Data After Handling Nulls and Dropping Columns")
st.write("This section displays the first few rows of the dataset after handling null values and dropping columns with more than 90% of a single value.")
st.write(dff.head())

st.header("Data After Replacements")
st.write("This section provides summary statistics of the dataset after replacing specific values to standardize the data.")
st.write(dff.describe())
