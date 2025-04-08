import streamlit as st
import pandas as pd

# Title of the app
st.title("Simple Data Dashboard")

# File uploader for CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Display the first few rows of the dataframe
    st.subheader("Data Preview")
    st.write(df.head())

    # Display a summary of the dataframe
    st.subheader("Data Summary")
    st.write(df.describe())

    # Filter Data
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    # Filter the dataframe based on the selected value
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # Plot Data
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        # Check if the selected columns are valid
        if x_column in filtered_df.columns and y_column in filtered_df.columns:
            # Create a line chart using Streamlit's built-in function
            st.line_chart(filtered_df.set_index(x_column)[y_column])
        else:
            st.error("Please select valid columns for plotting.")
else:
    st.write("Waiting on file upload...")