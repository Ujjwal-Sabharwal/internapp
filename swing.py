import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import statistics

def show():
    df = pd.read_csv("Data_Additional_Columns.csv")

    df.drop('Unnamed: 0', axis='columns', inplace=True)  # DROPPING UNNAMED COLUMN AS IT IS NOT REQUIRED
    df.drop('Unnamed: 1', axis='columns', inplace=True)

    col1, col2, col3 = st.columns(3)
    with col2:
        st.write(df[['Predicted Mood', 'Overall']])

    df['BIF_1 (Who influence your decision in subject selection)'] = df[
        'BIF_1 (Who influence your decision in subject selection)'].replace('Family/Society ',
                                                                            'Family/Society')  # replacing values
    df['BIF_2 (Factor influencing decision)'] = df['BIF_2 (Factor influencing decision)'].replace('Career prospects',
                                                                                                  'Career Prospects')  # replacing values
    df['BIF_2 (Factor influencing decision)'] = df['BIF_2 (Factor influencing decision)'].replace(
        ['Personal interest', 'Personal Interest '], 'Personal Interest')  # replacing values
    df['SGIF_1 (Dependency)'] = df['SGIF_1 (Dependency)'].replace("Previous students' experiences",
                                                                  "Previous Students' Experiences")  # replacing values
    df['SGIF_1 (Dependency)'] = df['SGIF_1 (Dependency)'].replace('Academic advisors',
                                                                  'Academic Advisors')  # replacing values

    overall_count = df['Overall'].value_counts()
    predicted_count = df['Predicted Mood'].value_counts()

    fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
    # Create grid
    # Zorder tells it which layer to put it on. We are setting this to 1 and our data to 2 so the grid is behind the data.
    ax.grid(which="major", axis='both', color='#758D99', alpha=0.6, zorder=1)
    ax.hlines(y=overall_count.index, xmin=predicted_count[overall_count.index], xmax=overall_count[overall_count.index],
              color='#758D99', alpha=0.6, zorder=2)

    # Plot bubbles next
    ax.scatter(predicted_count[overall_count.index], overall_count.index, label='predicted', s=60, color='red',
               zorder=3)
    ax.scatter(overall_count[overall_count.index], overall_count.index, label='overall', s=60, color='blue', zorder=3)

    # Reformat x-axis tick labels

    ax.xaxis.set_tick_params(labeltop=True,  # Put x-axis labels on top
                             labelbottom=False,  # Set no x-axis labels on bottom
                             bottom=False,  # Set no ticks on bottom
                             labelsize=11,  # Set tick label size
                             pad=-1)  # Lower tick labels a bit

    # Reformat y-axis tick labels

    ax.set_yticks(overall_count.index)
    ax.set_yticklabels(overall_count.index,  # Set labels again
                       ha='left')  # Set horizontal alignment to left
    ax.yaxis.set_tick_params(pad=120,  # Pad tick labels so they don't go over y-axis
                             labelsize=11)  # Set label size

    # set legend
    ax.legend(['transition', 'predicted', 'overall'], loc=(0, 1.076), ncol=3, frameon=False, handletextpad=-.1,
              handleheight=1)
    st.pyplot(fig)