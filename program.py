import streamlit as st
import requests

# OpenWeatherMap API Key
api_key = "574faf8ec0644d7066eaa44851f48a56"

st.title("Weather Forecast")

location = st.text_input("Enter a location (city, zip code, or coordinates):")

if location:
    # Send API request
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Extract weather data
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    # Display weather data
    st.write(f"Temperature: {temperature}°C")
    st.write(f"Humidity: {humidity}%")
    st.write(f"Weather: {weather}")
    
    # API for forecast data
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    forecast_data = response.json()
    forecast = forecast_data["list"]
    st.write("5 Day Forecast:")
    for i in range(5):
        forecast_time = forecast[i]["dt_txt"]
        forecast_temp = forecast[i]["main"]["temp"]
        forecast_desc = forecast[i]["weather"][0]["description"]
        st.write(f"{forecast_time} - Temperature: {forecast_temp}°C, Description: {forecast_desc}")

