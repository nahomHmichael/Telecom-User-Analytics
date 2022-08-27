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
    
    st.header("Top 10 Users Experience analysis")
    st.subheader("Average Throughput")
    st.dataframe(avg_thrpt)
    st.bar_chart(avg_thrpt['Average throughput'])

    st.subheader("Round Trip Time")
    st.dataframe(rtt)
    st.bar_chart(rtt['Average RTT'])

    st.subheader("TCP")
    st.dataframe(tcp)
    st.bar_chart(tcp['Average TCP'])

    st.header("Most Frequenct Users")
    st.subheader('Frquent Average Throughput')
    st.dataframe(frqnt_thrpt)
    st.bar_chart(frqnt_thrpt['0'])

    st.subheader("Frquent Round Trip Time")
    st.dataframe(frqnt_rtt)
    st.bar_chart(frqnt_rtt['0'])

    st.subheader("Frquent TCP")
    st.dataframe(frqnt_tcp)
    st.bar_chart(frqnt_tcp['0'])

    st.header("Cluster with 3 group classification")
    st.image('data/clusterExp.png')