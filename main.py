import requests # allows HTTP requests 
from apikeys import NASA, GAPI # external API keys
import google.generativeai as genai # ai compiler
import os
from datetime import date, timedelta


# Today's date
toda = date.today()
yesterda = toda - timedelta(days=1)

today = toda.strftime("%Y-%m-%d")
# Yesterday's date
yesterday = yesterda.strftime("%Y-%m-%d")


# Google API config 
MODEL = "gemini-1.5-flash"
prompt = "Summarize the following text into 3 lines, prioritizing scientfic information, while keeping it simple enough for someone who is not an astronomer to understand. Make sure to include outstanding or visible details, explaining them also. Make sure to include details about how the photo was taken, if present: "

def get_model(): # Initialize Google Gemini AI library to be callable
    genai.configure(api_key=GAPI)
    return genai.GenerativeModel(MODEL)

# API ref dict
apis = {
    "apod" : "https://api.nasa.gov/planetary/apod?api_key="+ NASA,

}
# check for API error codes
rcodes = {
    200 : "Success",
    301 : "Redirecting",
    400 : "Invalid request",
    401 : "Invalid login",
    403 : "Unauthorized page",
    404 : "Page not found",
    503 : "Server not ready"
}

# Function blocks for parsing each API data
def apod(data):
    f.write(i + ": \n")
    print(data['date']) 
    f.write(str(data['url'] + "\n"))
    
    imgexp = str(data['explanation'])
    f.write(imgexp) 

f = open("data.txt", "w") # Opens data file in write-over mode

# Resusable data retrieval function, prioritized for NASA APOD api
def datagrab(api,api_key,param,prompt="",summarize=False,date=today): # --> Reusable function to grab data from API
    with requests.Session() as session: # Initializes request session

        for i in apis:

            with session.get(api, params={"api_key": api_key, "date":date}) as response: # Opens api
                
                response.raise_for_status() # Checks response ping
                data = response.json()
                
                returnvalue = data.get(param) # Gets data from specific parameter, param
                
                if returnvalue and summarize: # If we want to summarize, summarize == True
                    summarized = get_model().generate_content(prompt + returnvalue).text
                    print(summarized)
                    f.write(str(summarized+ "\n"))
                elif summarize != True:
                    print(returnvalue)
                    f.write(str(returnvalue + "\n"))
                else:
                    print("Error: Runtime error")

def todaydata(): # Grab today's data
    datagrab(apis['apod'],NASA,'url') # returns url of image
    print("\n")
    datagrab(apis['apod'],NASA,'explanation') # returns regular explanation
    print("\n")
    datagrab(apis['apod'],NASA,'explanation',prompt,True) # returns summarized explanation of APOD image

def yesterdata(): # Grab yesterday's data
    datagrab(apis['apod'],NASA,'url',date=yesterday) # returns url of image
    print("\n")
    datagrab(apis['apod'],NASA,'explanation',date=yesterday) # returns regular explanation
    print("\n")
    datagrab(apis['apod'],NASA,'explanation',prompt,True,date=yesterday)

f.close() # Closes file to prevent accidental writing
