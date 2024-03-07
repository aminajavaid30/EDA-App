import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Check for Missing Values
data = st.session_state.data
if data is None:
    st.error("Please upload a dataset or use example data.")

# Function to create bar graph
def create_bar_graph(selected_columns):
    # Select the data for the selected columns
    selected_data = data[selected_columns]
    
    fig, ax = plt.subplots()
    # Plot bar graph for each column
    for column in selected_data.columns:
        sns.barplot(selected_data[column], label=column)
    
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.title('Bar Graph')
    plt.legend()  # Add legend to distinguish between columns
    st.pyplot(fig)

# Function to create line chart
def create_line_chart(selected_columns):
    # Select the data for the selected columns
    selected_data = data[selected_columns]
    
    fig, ax = plt.subplots()
    # Plot line chart for each column
    for column in selected_data.columns:
        plt.plot(selected_data.index, selected_data[column], label=column)

    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.title('Line Chart')
    plt.legend()  # Add legend to distinguish between columns
    st.pyplot(fig)

# Function to create pie chart
def create_pie_chart(selected_columns):
    # Calculate frequencies or proportions for each category
    counts = data[selected_columns].value_counts()
    labels = counts.index
    sizes = counts.values

    # Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title('Pie Chart')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the plot
    st.pyplot(fig)

# Function to create histogram
def create_histogram(selected_columns):
    # Select the data for the selected column
    selected_data = data[selected_columns]
    
    fig, ax = plt.subplots()
    # Plot histogram for the selected column
    plt.hist(selected_data, label=selected_columns)
    
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.legend()  # Add legend to distinguish between columns
    st.pyplot(fig)

# Function to create box plot
def create_box_plot(selected_column):
    # Select the data for the selected columns
    selected_data = data[selected_columns]
    
    # Create box plots for the selected columns
    fig, ax = plt.subplots()
    sns.boxplot(selected_data[selected_column])
    plt.xlabel(selected_column)
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    plt.title('Box Plot')
    plt.tight_layout()
    st.pyplot(fig)

# Function to create scatter plot
def create_scatter_plot(x_column, y_column):
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(data[x_column], data[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title('Scatter Plot')
    st.pyplot(fig)

# Function to create heatmap
def create_heatmap(selected_columns):
    selected_data = data[selected_columns]
    selected_data = selected_data.select_dtypes(include=['number'])
    # Calculate the correlation matrix
    corr = selected_data.corr()
    
    # Create heatmap
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Heatmap')
    st.pyplot(fig)
    
if data is not None:
    st.subheader("Data Visualizations")

    col1, col2 = st.columns([1, 2])

    with col1:
        data_visual = st.selectbox("Select Visualization", ("Bar Graph", "Line Chart", "Pie Chart", "Histogram", "Box Plot", "Scatter Plot", "Heatmap"))
            
    with col2:
        selected_columns = st.multiselect("Select Columns", data.columns)

    if selected_columns and st.button("Create Visualization"):
        if data_visual == "Bar Graph":
            create_bar_graph(selected_columns)
        elif data_visual == "Line Chart":
            create_line_chart(selected_columns)
        elif data_visual == "Pie Chart":
            create_pie_chart(selected_columns)
        elif data_visual == "Histogram":
            create_histogram(selected_columns)
        elif data_visual == "Box Plot":
            create_box_plot(selected_columns[0])
        elif data_visual == "Scatter Plot":
            create_scatter_plot(selected_columns[0], selected_columns[1])
        elif data_visual == "Heatmap":
            create_heatmap(selected_columns)