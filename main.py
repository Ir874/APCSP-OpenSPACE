import requests # allows HTTP requests 
from apikeys import NASA, GAPI # external API keys
import google.generativeai as genai # ai compiler
import os


# Google API config 
MODEL = "gemini-1.5-flash"
prompt = "Summarize the following text into 2 lines, prioritizing scientfic information, while keeping it simple enough for someone who is not an astronomer to understand. Make sure to include outstanding or visible details, explaining them also: "

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

def datagrab(api,api_key,param,prompt="",summarize=False): # --> Reusable function to grab data from API
    with requests.Session() as session: # Initializes request session

        for i in apis:

            with session.get(api, params={"api_key": api_key}) as response: # Opens api
                
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

datagrab(apis['apod'],NASA,'url') # returns url of image
datagrab(apis['apod'],NASA,'explanation')
print("\n")
datagrab(apis['apod'],NASA,'explanation',prompt,True) # returns summarized explanation of APOD image

f.close() # Closes file to prevent accidental writing