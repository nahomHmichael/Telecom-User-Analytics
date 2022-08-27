import streamlit as st
import pandas as pd
import os
import sys


def app():

    st.title("User Experience Analysis")
    
    rtt = pd.read_csv('data/top10_rtt.csv')
    tcp = pd.read_csv('data/top10tcp.csv')
    frqnt_thrpt = pd.read_csv('data/most_freqAvgThr.csv')
    frqnt_rtt = pd.read_csv('data/most_freqRTT.csv')
    frqnt_tcp = pd.read_csv('data/most_freqTCP.csv')
    avg_thrpt = pd.read_csv('data/top10avgThroughput.csv')