import streamlit as st
import requests

api_key='574faf8ec0644d7066eaa44851f48a56'

def convert_to_celcius(temperature_in_kelvin):
    return temperature_in_kelvin - 273.15
def find_current_weather(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city }&appid={api_key}"
    weather_data=requests.get(base_url).json()
    st.json(weather_data)
    try:
        general = weather_data['weather'][0]['main']
        icon_id = weather_data['weather'][0]['main']
        temperature = round(convert_to_celcius(weather_data['main']['temp']))
        icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City Not Found")
        st.stop()
    return general,temperature,icon    

def main():
    st.header("Find the weather")
    city=st.text_input("Enter the city").lower()
    if st.button("Find"):
        general,temperature,icon = find_current_weather(city)
        col_1,col_2 = st.columns(2)
        with col_1:
            st.metric("temperature",value=f"{temperature}°C")
        with col_2:
            st.write(general)
            st.image(icon)    


if __name__=='__main__':
    main()
