import sys
sys.path.insert(0, './dashboard')

import streamlit as st
from dashboard.multiapp import MultiApp
from dashboard import user_engagement, user_experience , user_satisfaction, predict_satisfaction
# import your app modules here

st.set_page_config(page_title="TellCo Telecom Analytics", layout="wide")

app = MultiApp()


st.sidebar.markdown("""
# TellCo's User Analytics
### Multi-Page App
""")

# Add all your application here

app.add_app("user_engagement", user_engagement.app)
app.add_app("user_experience", user_experience.app)
app.add_app("user_satisfaction", user_satisfaction.app)
app.add_app("predict_satisfaction", predict_satisfaction.app)

# The main app
app.run()
