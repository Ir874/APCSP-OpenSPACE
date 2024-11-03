# imports for functionality
import requests 
import google.generativeai as genai # ai compiler
import os
# requests module -->  allows us to send/recieve packets to/from APIs
# We use 3 APIs in this program; 2 NASA OpenAPIs, and a Google AI api SDK .
# We extract information from the first 2 apis, and summarize using the Google API,
# which is then presented to the user in a simple webpage.


# NASA API config
key = "S6Z5MD5j0b6RpnXaxVbBRderzcsSJwpTLLabatO1" # --> NASA API key

# Google API config --> migrate to openai after developing ai key
genai.configure(api_key=os.environ["AIzaSyDtzwP93lpst_lOXwFR_0YhK-6OXrIXLMI"]) # --> Google ai API
model = genai.GenerativeModel("gemini-1.5-flash") # --> generates stable model

# function for passing text thru google openai library: -> 
def summarize(inp):
    pass


# API ref dict
apis = {
    "apod" : "https://api.nasa.gov/planetary/apod?api_key="+ key 


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
    # This block appends apod data to data.txt
    f.write(i + ": \n")
    print(data['date']) # date
    f.write(str(data['url'] + "\n")) # url 
    
    imgexp = str(data['explanation']) # vaiable to store explanation
    f.write(imgexp) # <-- writes explanation to data.txt


f = open("data.txt", "w") # Opens data file in write-over mode

for i in apis: # Runs through api list
    
    # GRABS DATA FROM API: I    
    response = requests.get(apis[i]) # returns status code
    respt = response.json() # Stores text values of api data as a dict
    
    # Delete this part after fully integrated -->
    print(i + "-" + rcodes[response.status_code]) # prints status code 
    print(respt['url']) 
    # Delete this part after fully integrated <--

    # block to determine parsing func
    if i == "apod":
        apod(respt) # <-- passes dict of api response thru parsing function
    else: pass
    

# Call this line last, to enable full data writing
f.close() # Closes file to prevent accidental writing