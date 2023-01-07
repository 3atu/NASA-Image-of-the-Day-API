import requests
import streamlit as st
import pandas

api_key = "zo4ZxcZAc3Tg4OFhOdoFD3srdhhqkFm60kBMN60g"
api_url = "https://api.nasa.gov/planetary/apod?api_key=zo4ZxcZAc3Tg4OFhOdoFD3srdhhqkFm60kBMN60g"

#Make Request
request = requests.get(api_url)

#Place API data into json dictionary
content = request.json() #gets content as dictionary

#layout
st.set_page_config(layout="wide")

#content on site

st.title("NASA Image of the Day")

image = content["url"]
st.image(image)

title = content["title"]
st.subheader(title)

explanation = content["explanation"]
st.write(explanation)