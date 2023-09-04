import requests
from datetime import datetime
import streamlit as st
url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"chennai"}

headers = {
	"X-RapidAPI-Key": "a059f63a96msh33ca9bf91205c1ap10da75jsnaaafd0aca17c",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
datadict={}
data=response.json()["current"]

location=response.json()["location"]
datadict["latitude"]=location["lat"]
datadict["longitude"]=location["lon"]
datadict["city"]=location["name"]
datadict["region"]=location["region"]
datadict["time"]=location["localtime"]



datadict["temperature"]=data["temp_c"]
datadict["windspeed"]=data["wind_kph"]
datadict["precipitaion"]=data["precip_mm"]
datadict["humidity"]=data["humidity"]
datadict["winddegree"]=data["wind_degree"]
datadict["tempfeelslike"]=data["feelslike_c"]
datadict["gustspeed"]=data["gust_kph"]
datadict["visisbility"]=data["vis_km"]
# print(response.json())
for i in datadict:
  st.text(i)
  st.text(datadict[i])
