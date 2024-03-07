import streamlit as st 

# Check for Duplicates
data = st.session_state.data
if data is None:
    st.error("Please upload a dataset or use example data.")
    
if data is not None:
    duplicates = data.duplicated()
    duplicate_count = duplicates.sum()
    
    st.subheader("Duplicate Values")
    if duplicate_count > 0:
        st.write(data[duplicates])
    else:
        st.write("No duplicate values found.")