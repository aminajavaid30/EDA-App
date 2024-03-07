import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Check for Missing Values
data = st.session_state.data
if data is None:
    st.error("Please upload a dataset or use example data.")
    
if data is not None:
    st.subheader("Outliers")
    # Draw box plots of numerical columns using subplots
    # Adjusting the subplot grid size to accommodate all numeric columns
    numeric_cols = data.select_dtypes(include=['number']).columns.tolist()

    num_cols = len(numeric_cols)
    num_rows = (num_cols // 4) + (1 if num_cols % 4 else 0)  # Adjust the number of rows in the grid

    fig = plt.figure(figsize=(10, num_rows * 3))
    for i, col in enumerate(numeric_cols, 1):
        plt.subplot(num_rows, 4, i)
        sns.boxplot(data=data[col])
        plt.title(col)

    plt.tight_layout()
    st.pyplot(fig)

