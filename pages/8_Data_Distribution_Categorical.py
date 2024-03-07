import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Display the data distribution for each column 
data = st.session_state.data
if data is None:
    st.error("Please upload a dataset or use example data.")
    
if data is not None:
    st.subheader("Bar Graphs of Categorical Columns")
    categorical_cols = data.select_dtypes(include=['object']).columns

    if categorical_cols.empty:
        st.write("No categorical columns found in the DataFrame.")
    else:
        # Number of subplots
        num_subplots = len(categorical_cols)

        # Create a figure with rows=ceil(num_subplots/3) and columns=3
        num_rows = num_subplots // 3
        if num_subplots%3 > 0:
            num_rows += 1
        fig, axs = plt.subplots(num_rows, 3, figsize=(20, 7*num_rows))

        # Flatten the axs array to handle both cases (1 row or more)
        axs = axs.flatten()

        # Loop through subplots
        for i, column in enumerate(categorical_cols):
            # Create a countplot on each subplot
            sns.countplot(x=column, data=data, ax=axs[i])
            axs[i].set_title(f'Frequency of {column.replace("_", " ").title()}')
            axs[i].tick_params(axis='x', rotation=90)

        # Adjust layout for better spacing
        plt.tight_layout()
        st.pyplot(fig)