import pandas as pd
import streamlit as st

# Print basic data information
data = st.session_state.data
if data is None:
    st.error("Please upload a dataset or use example data.")
    
if data is not None:
    st.subheader("Basic Data Information")
    st.write("Data Head:")
    st.write(data.head())
    st.write("Data Shape:", data.shape)
    # Create a DataFrame to display column names and data types
    column_info = pd.DataFrame({
        'Column Name': data.columns,
        'Data Type': data.dtypes
    })
    # Display the DataFrame as a table using st.dataframe()
    st.write("Columns and Data Types:")
    st.dataframe(column_info)
