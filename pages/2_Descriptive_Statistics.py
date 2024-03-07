import streamlit as st 

# Display descriptive statistics
data = st.session_state.data
if data is None:
    st.error("Please upload a dataset or use example data.")

if data is not None:
    numeric_cols = data.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = data.select_dtypes(include=['object']).columns.tolist()
    st.subheader("Descriptive Statistics")
    if len(numeric_cols) > 0:
        st.write("Numeric Columns:")
        st.write(data.describe())
    if(len(categorical_cols) > 0):   
        st.write("Categorical Columns:")
        st.write(data.describe(include='object'))