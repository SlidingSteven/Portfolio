# Steven Tucker's Portfolio

Typically, I use the security question checker app as my "go-to" project, but due to increasingly strict internet policies it seems my site has been blocked from scraping fastpeoplesearch.com.  I respect their decision to do what they feel is best for their service and I do not intend to make an attempt to work around the block.

Instead I have compiled a patchwork of example projects where I have used several different tools.  In this README I will give a brief explanation of each script and why it was made.

## Note: 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Most of the scripts you find here cannot run without you setting up a config file.  For this reason I have tried to give some sort of output either as a comment in the script file itself or as an output file.

## Big_12_Coaches.py

### Why?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;My capstone class required us to demonstrate a useful package that we were familiar with and I chose BeautifulSoup for my demonstration.  I chose this particular package because I had just finished using it in my internship the previous summer and I knew several of my classmates could benefit from learning about the tool.

### About 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I loaded a list of links to the wiki page for each football program in the Big 12 and my script would go through each link, finding the info box and parsing the coach name and program name out.  This was a very simple application of the library but it is really only meant to be a proof of concept.

## fitbit_API_demo.py

### Why?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I recently got a fitbit watch and I figured learning how to use thier API would be a good "exercise" (ba-dum-tsss)

### About
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In the file I have a few different methods for fetching different activities but heart rate has always been the most interesting to me.  This was a particularly challenging project because of the way they had authentication set up, but I learned a lot and had fun!  Below I have included the graph that I plotted in the script file.

![heart rate](fitbit_api_demo.png)

## github_api.py

### Why?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;My capstone project was with a company that requested an NDA so we had to provide some sort of proof we were doing productive work for the company and I decided it would be a good opportunity to try out Github's API.  

### About
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Using Github's API I fetched each branch of the repo, and then each commit of each branch and logged output to a file that I could then send to the TA.  Since the repo is private I have since modified the script to hit a public repo instead.  I also added a function to provide some work with Pandas and I included the associated graph below.

![commits](github_api.png)


## gmail_to_text.py

### Why?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In my internship I would regularly run scripts that would take several hours to complete and wanted a way to notify me when they completed.

### About 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This script uses a gmail account to send "text" messages to a cell phone number.  If I wanted to scale it up, I could use the API for https://www.freecarrierlookup.com/ but since it was just for myself I didn't need to.

## spotify_API_Demo.py
### Why? 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In some of my downtime I have been working on re-implementing the https://github.com/MichMich/MagicMirror in python just to keep skills sharp.  This project is still pretty new and not ready for any sort of live demo but I have attached one screenshot below, just to show what the spotify portion was supposed to do (bottom left).

### About 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You can read more on Magic-Mirrors here- https://magicmirror.builders/  

![magic-mirror](spotify_demo.PNG)


## Bigger Projects?

Sure, if you would like to see my work on larger scales I would encourage you to peek at these repos-    
* https://github.com/Kiddkos/WCAGCompChecker - This was a team project to parse the html of a given web page to see if it would pass Web Content Accessibility Guidelines (WCAG) set by W3.

* https://github.com/SlidingSteven/IHubPublicVideoRecorder - This was my first experience with Flask and the first large scale project I was involved with.  The purpose was to give users at the Innovation Hub a "video booth" to record a video about what they had made that day to be shared on our Facebook.  This particular project wasn't wildly successful but it was the project that sparked my interest in Python and webdevelopment.

* https://github.com/SlidingSteven/SecurityQuestionEvaluator - This was the largest public project I had made and unfortunately as I said earlier, this seems to be a dwindling flame as IP addresses are being blocked.  The code will remain up and I think it still remains a good example of what I can do.

* Aside from these I also constructed a massive automation effort for my internship from the ground up.  This effort automated 7 project types and brought the runtime of these projects down from a typical 45 minute job to less than 1 minute.  This had a massive impact for my team because each project saved the company thousands of dollars and my team was able to reallocate time.

## Deal with any Math?
Absolutely!  I have a minor in Math so it certainly came with the territory.  I have included two of note in this repository.  
* Statistics_project.html - This was my final project of my Statistics class and it aims to find a relationship between hummidity and percieved temperature.  This project was done in R and R markdown but I included it here because it shows my experience with processing large amounts of data.
* Algo_Report.html - This report was done for my Algorithm Analysis class.   It has some great examples of the ways I have applied Python to math.
* NumericalAnalysis-lab1.py / NumericalAnalysis-lab2.py - These labs were done in python for my numerical analysis class which covered how math on large data sets can impact performance.