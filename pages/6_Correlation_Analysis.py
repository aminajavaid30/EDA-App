import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Check for Missing Values
data = st.session_state.data
if data is None:
    st.error("Please upload a dataset or use example data.")
    
if data is not None:
    # Filter numeric columns
    numeric_data = data.select_dtypes(include=['number'])

    if not numeric_data.empty:
        # Calculate the correlation matrix
        corr = numeric_data.corr()

        # Create heatmap to visualize the correlation matrix
        st.subheader("Correlation Analysis")
        fig, ax = plt.subplots()
        ax = sns.heatmap(corr)
        st.pyplot(fig)
    else:
        st.write("No numeric columns found in the DataFrame.")