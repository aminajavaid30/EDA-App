import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Display the data distribution for each column 
data = st.session_state.data
if data is None:
    st.error("Please upload a dataset or use example data.")
    
if data is not None:
    # Distribution of numeric columns
    st.subheader("Distribution of Numeric Columns")
    numeric_cols = data.select_dtypes(include=['number']).columns
    
    if numeric_cols.empty:
        st.write("No numeric columns found in the DataFrame.")
    else:
        rows = len(numeric_cols)//4 # Calculate the number of rows needed for the subplots
        if len(numeric_cols)%4 > 0:
            rows += 1
        fig, axes = plt.subplots(nrows=rows, ncols=4, figsize=(20, 5 * rows))

        if rows > 1:
            for i, col in enumerate(numeric_cols):
                sns.histplot(data[col], kde=True, ax=axes[i // 4, i % 4])
                axes[i // 4, i % 4].set_title(col)
        else:
            for i, col in enumerate(numeric_cols):
                sns.histplot(data[col], kde=True, ax=axes[i])
                axes[i].set_title(col)
        
        plt.tight_layout()
        st.pyplot(fig)    