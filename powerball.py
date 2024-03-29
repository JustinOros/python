#!/usr/bin/python3
# Description: CLI to Powerball.com (prints previous winning results)
# Usage: python3 powerball.py
# Author: Justin Oros
# Source: https://github.com/JustinOros

import requests
from bs4 import BeautifulSoup as BS

# Perform an HTTP GET request to the Powerball website
powerballUrl = 'https://www.powerball.com/previous-results?gc=powerball'
r = requests.get(powerballUrl, verify=True)

# Parse out our HTML using BeautifulSoup
soup = BS(r.text, 'html.parser')

# Parse Drawing Dates
drawingDates = soup.find_all('h5',class_='card-title')

# Parse White Balls
whiteballs = soup.find_all('div',class_='form-control col white-balls item-powerball') 

# Parse Power Balls 
powerballs = soup.find_all('div',class_='form-control col powerball item-powerball') 

# Initalize and Set starting positions
whiteballPos = powerballPos = 0

# Loop through previous Drawing Dates
for date in drawingDates:
        
        # Print Drawing Date
        print (date.text + ":", end=" ")

        # Print 5 White Balls
        for i in range(0,5):
            print (whiteballs[whiteballPos].text + ",", end=" ")
            whiteballPos += 1
        
        # Print 1 Power Ball
        print (powerballs[powerballPos].text)
        powerballPos += 1
