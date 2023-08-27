import streamlit as st
import plotly.express as px
from backend import get_data

# Contains the front end od the App

st.title("Weather Forecast for the Next Days")

location = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {location}")

data = get_data(location, days, option)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
# the below method gets the figure object as input
st.plotly_chart(figure)
