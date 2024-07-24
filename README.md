# Data-Cleaning
Below is the Streamlit code with additional explanations for each step, displayed on the website to help users understand the data analysis process.


### Explanation for Each Step

1. **Initial Data Overview**:
   - Provides a snapshot of the dataset by displaying the first few rows. This helps in understanding the structure and content of the dataset.

2. **Null Values Analysis**:
   - Shows the number of null values in each column before any preprocessing. This is crucial to identify columns that need data cleaning.

3. **Number of Unique Values in Columns with Nulls**:
   - Lists the number of unique values in columns containing null values. This helps gauge the diversity of data within those columns.

4. **Mode Values Used for Filling Nulls**:
   - Displays the mode values (most frequent values) used to fill null values in the columns. Using mode values is a common approach to handle missing data.

5. **Columns with Null Values**:
   - Lists the columns that contained null values and were filled with mode values. This helps in tracking which columns were modified.

6. **Value Counts After Null Handling**:
   - Provides the value counts for each column after handling null values. This ensures that the null values have been appropriately replaced and gives an insight into the distribution of data.

7. **Data After Handling Nulls and Dropping Columns**:
   - Displays the first few rows of the dataset after null values are handled and columns with more than 90% of a single value are dropped. This step helps in cleaning the data by removing columns that may not provide meaningful insights.

8. **Data After Replacements**:
   - Shows summary statistics of the dataset after replacing specific values to standardize the data. This step ensures that the data is uniform and ready for further analysis.

This Streamlit code, along with explanations, provides a comprehensive view of the data preprocessing steps, helping users understand each part of the process.
