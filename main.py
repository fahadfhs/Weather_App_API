import streamlit as st
import plotly.express as px
from backend import get_data

# Contains the front end od the App

st.title("Weather Forecast for the Next Days")

place = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

# if there is place provided then run the below function
if place:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images_/clear.png", "Clouds": "images_/cloud.png",
                  "Rain": "images_/rain.png", "Snow": "images_/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        # list comprehension over here
        image_path = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(image_path, width=115)