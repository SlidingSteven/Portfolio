#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#case for texas.
def texas_sucks():
    return """
    
No info to return, texas sucks

"""

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
    #Make attempt at opening url, doesnt always work based on security
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

                #handle Texas Longhorn case
                if "Longhorns" in wordList[1]:
                    tex = texas_sucks()
                    print(tex)

                #search for coach
                else:
                    for word in wordList:
                        if "coach" in word:
                            #remove coach from the word
                            word = word.replace("coach","")
                            #display output
                            print(wordList[0],wordList[1],"- ",word, wordList[i+1])
                        i = i+1
    #handle the cases that cannot open by cleaning letting the user know it could not open
    except:
        print("error opening")

