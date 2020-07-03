#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


#List of Big 12 football wikipedias to search through.  Yes there are only 10 teams in the big 12...
big12 = ["https://en.wikipedia.org/wiki/Oklahoma_Sooners_football",
         "https://en.wikipedia.org/wiki/Baylor_Bears_football",
         "https://en.wikipedia.org/wiki/Iowa_State_Cyclones_football",
         "https://en.wikipedia.org/wiki/Kansas_Jayhawks_football",
         "https://en.wikipedia.org/wiki/Oklahoma_State_Cowboys_football",
         "https://en.wikipedia.org/wiki/TCU_Horned_Frogs_football",
         "https://en.wikipedia.org/wiki/Texas_Tech_Red_Raiders_football",
         "https://en.wikipedia.org/wiki/West_Virginia_Mountaineers_football",
         "https://en.wikipedia.org/wiki/Texas_Longhorns_football"]
         
#Do this for each school in the big12 list
for school in big12:
    try:
        with urlopen(school) as response:
            #convert html to soup
            soup = BeautifulSoup(response, 'html.parser')
            #find the info box
            info_box = soup.find('table',{'class':'infobox'})
            #handle info_box
            for cell in info_box: 
                info = cell.text
                #Convert info box to list of words
                wordList = re.sub("[^\w]", " ",  info).split()
                
                #start counter
                i = 0
                for word in wordList:
                    if "coach" in word:
                        word = word.replace("coach","")
                        print(wordList[0],wordList[1],"- ",word, wordList[i+1])
                    i = i+1
    except:
        print("error opening")

# --- Expected Output ---
# Oklahoma Sooners -  Lincoln Riley
# Baylor Bears -  Dave Aranda
# Iowa State -  Matt Campbell
# Kansas Jayhawks -  Les Miles
# Oklahoma State -  Mike Gundy
# TCU Horned -  Gary Patterson
# Texas Tech -  Matt Wells
# West Virginia -  Neal Brown
# Texas Longhorns -  Tom Herman