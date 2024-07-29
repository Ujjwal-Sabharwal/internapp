import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import statistics

def show():
    """
    Renders a Streamlit app page for analyzing and visualizing data from a CSV file.

    The app includes functionalities for displaying data, generating pie charts, bar charts,
    stacked bar charts, count plots, distribution plots (using seaborn), and box plots (using Plotly).

    """

    # Load the CSV data
    df = pd.read_csv("Data_Additional_Columns.csv")

    # Drop unnecessary columns
    df.drop(['Unnamed: 0', 'Unnamed: 1', 'Predicted Mood', 'Overall', 'Mood Swing Type', 'Swing Type', 'Zone Switch'], axis=1, inplace=True)

    # Display the DataFrame
    st.write(df)

    # Data cleaning: handle inconsistent values in specific columns
    df['BIF_1 (Who influence your decision in subject selection)'] = df['BIF_1 (Who influence your decision in subject selection)'].replace('Family/Society ', 'Family/Society')
    df['BIF_2 (Factor influencing decision)'] = df['BIF_2 (Factor influencing decision)'].replace('Career prospects', 'Career Prospects')
    df['BIF_2 (Factor influencing decision)'] = df['BIF_2 (Factor influencing decision)'].replace(['Personal interest', 'Personal Interest '], 'Personal Interest')
    df['SGIF_1 (Dependency)'] = df['SGIF_1 (Dependency)'].replace("Previous students' experiences", "Previous Students' Experiences")
    df['SGIF_1 (Dependency)'] = df['SGIF_1 (Dependency)'].replace('Academic advisors', 'Academic Advisors')

    # Function to create a pie chart
    def pie_chart(df, col):
        col_count = df[col].value_counts()
        fig = plt.figure(figsize=(8, 8))
        ax = plt.subplot()
        color_palette = ['#0077b6', '#0096c7', '#00b4d8', '#48cae4', '#90e0ef', '#ade8f4', '#caf0f8']
        plt.pie(col_count, labels=col_count.index, autopct='%1.1f%%', colors=color_palette)
        plt.title(col)
        plt.legend()
        st.pyplot(fig)

    # Function to create a bar chart
    def bar_chart(df, col):
        col_count = df[col].value_counts()
        fig = plt.figure(figsize=(8, 8))
        ax = plt.subplot()
        plot = plt.bar(col_count.index, col_count.values)
        plt.bar_label(plot)
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.title(col)
        st.pyplot(fig)

    # Function to create a stacked bar chart
    def stacked_bar_chart(df, col1, col2):
        df.columns = df.columns.str.strip()
        if col1 in df.columns and col2 in df.columns:
            cols_counts = df.groupby([col1, col2]).size().unstack()
            fig = plt.figure(figsize=(12, 8))
            ax = fig.add_subplot(111)
            color_palette = ['#0077b6', '#0096c7', '#00b4d8', '#48cae4', '#90e0ef', '#ade8f4', '#caf0f8']
            plot = cols_counts.plot(kind='bar', stacked=True, color=color_palette, ax=ax)
            for i in plot.containers:
                plot.bar_label(i)
            plt.title(f"{col1} by {col2}")
            plt.xlabel(col1)
            plt.ylabel('Count')
            plt.legend(title=col2)
            plt.xticks(rotation=0)
            plt.tight_layout()
            st.pyplot(fig)

    # Function to create a count plot
    def count_plot(df, col1, col2):
        color_palette = ['#0077b6', '#0096c7', '#00b4d8', '#48cae4', '#90e0ef', '#ade8f4', '#caf0f8']
        fig = plt.figure(figsize=(12, 6))
        ax = fig.add_subplot(111)
        plot = sns.countplot(x=col1, data=df, hue=col2, palette=color_palette, width=0.5, ax=ax)
        for i in plot.containers:
            plot.bar_label(i)
        st.pyplot(fig)

    # Function to create a distribution plot using seaborn
    def distplot(col):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        sns.set_style('whitegrid')
        sns.distplot(df[col], kde=False, color='blue', bins=30)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel('Count')
        st.pyplot(fig)

    # Function to create a box plot using Plotly
    def boxplot(df, col):
        fig = px.box(df, y=col)
        st.plotly_chart(fig)

    # Display interface for selecting a column to analyze its distribution or create charts
    st.header('Select A Field To Check Distribution of the Respondent')
    col_options = df.columns.tolist()
    col = st.selectbox("Please Select a Field", col_options, index=0)

    if col == df.columns[3] or col == df.columns[4]:  # Check if selected column is suitable for statistical analysis
        st.write('Mean:', statistics.mean(df[col]))
        st.write('Median:', statistics.median(df[col]))
        st.write('Mode:', statistics.mode(df[col]))
        st.write('Standard Deviation:', statistics.stdev(df[col]))
        st.write('Variance:', statistics.variance(df[col]))
        st.subheader('Distribution Plot')
        distplot(col)
        st.subheader('Box Plot')
        boxplot(df, col)
    else:  # Display charts for categorical columns
        st.subheader('Pie Chart')
        pie_chart(df, col)
        st.subheader('Bar Chart')
        bar_chart(df, col)

    # Display interface for selecting two columns to analyze their relationship
    st.header('Select Two Fields To Check Relationship Between Them')
    col1, col2 = st.columns(2)
    with col1:
        field1 = st.selectbox("Select Field 1", col_options, index=0, key='1')
    with col2:
        field2 = st.selectbox("Select Field 2", col_options, index=1, key='2')

    # Display charts for relationship analysis
    st.subheader('Stacked Bar Chart')
    stacked_bar_chart(df, field1, field2)
    st.subheader('Count Plot')
    count_plot(df, field1, field2)

