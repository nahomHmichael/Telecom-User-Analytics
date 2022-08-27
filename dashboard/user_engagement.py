import streamlit as st
import pandas as pd
import os
import sys

def app():

    st.title("User Engagement Analysis")

    df_email = pd.read_csv('data/top10_email_users.csv')
    df_game = pd.read_csv('data/top10_gameApp_users.csv')
    df_google = pd.read_csv('data/top10_google_users.csv')
    df_netflix = pd.read_csv('data/top10_netflix_users.csv')
    df_otherAct = pd.read_csv('data/top10_otherAct_users.csv')
    df_social = pd.read_csv('data/top10_socialMedia_users.csv')
    df_youtube = pd.read_csv('data/top_ten_youtube_users.csv')
    df_session = pd.read_csv('data/top_ten_session_duration.csv')
    df_DLUL = pd.read_csv('data/top_ten_UL_DL.csv')
    
    st.header("Top 3 best Handset Manufacturers")
    st.image('data/top 3 headsets.png')

    st.header("Top 10 best Handsets used for communication")
    st.image('data/top 10 headsets.png')

    st.header("Top 3 Most Used Applications")
    st.image('data/donut_topApps.png')

    st.header("Data transfers and overall data usage correlation.")
    st.image('data/corr.png')
    st.markdown(
        'There is a correlation Total data usage and Gaming data usage.')

    st.header("Top 10 Users Engaged Per Application")
    st.subheader("Email App users")
    st.dataframe(df_email)
    st.bar_chart(df_email['Email(UL/DL)'])

    st.subheader("Game App users")
    st.dataframe(df_game)
    st.bar_chart(df_game['Gaming(UL/DL)'])

    st.subheader("Google App users")
    st.dataframe(df_google)
    st.bar_chart(df_google['Google(UL/DL)'])

    st.subheader("Netflix App users")
    st.dataframe(df_netflix)
    st.bar_chart(df_netflix['Netflix(UL/DL)'])
