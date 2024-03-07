import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno

# Check for Missing Values
data = st.session_state.data
if data is None:
    st.error("Please upload a dataset or use example data.")
    
if data is not None:
    # Create a DataFrame to display columns and their missing values count
    missing = pd.DataFrame(data.isnull().sum().sort_values(ascending=False), columns=["Missing Values"])
    missing.index.name = "Column"

    # Display the missing values in a bar graph using missingno library on the right side
    col1, col2 = st.columns([1, 2])
    with col1:
        # Display the DataFrame on the left side
        st.subheader("Missing Values")
        st.dataframe(missing)
    with col2:
        # Display the bar graph on the right side
        st.subheader("Visualization")
        fig, ax = plt.subplots()
        ax = msno.bar(data, sort="descending")
        st.pyplot(fig)