import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="EDA"
)

# Title and brief description
st.title("Exploratory Data Analysis (EDA)")
st.subheader("Upload your dataset here (or use example data) for a complete exploratory data analysis.")

# 2. Ask the user if they want to upload data or use example data
data_option = st.radio("Select Data Input Option", ("Upload Data", "Use Example Data"))

# Function to load example data
def load_example_data(dataset_name):
    if dataset_name == "Titanic":
        return sns.load_dataset("titanic")
    elif dataset_name == "Tips":
        return sns.load_dataset("tips")
    elif dataset_name == "Iris":
        return sns.load_dataset("iris")

# Function to handle data input
def handle_data_input():
    if data_option == "Upload Data":
        uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])
        if uploaded_file is not None:
            return pd.read_csv(uploaded_file) if uploaded_file.name.endswith('csv') else pd.read_excel(uploaded_file)
        else:
            st.error("Please upload a CSV or Excel file or use Example Data.")
    else:
        dataset_name = st.selectbox("Select Example Dataset", ("Select Dataset", "Titanic", "Tips", "Iris"))
        return load_example_data(dataset_name)
    
# 3. Upload or use example data
data = handle_data_input()

if data is not None:
    st.success("Your dataset has been uploaded/selected. Navigate through the side bar to explore your data.")

st.session_state.data = data