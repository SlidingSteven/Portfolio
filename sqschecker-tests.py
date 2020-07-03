from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from prettytable import PrettyTable
import requests

testing = True
if testing: 
    baseURL = "http://127.0.0.1:5000/"
else: 
    baseURL = "https://sqschecker1.wn.r.appspot.com/"


people_list = [["Conan", "O'Brien", "90067"]]


def enter_info(first, last, zipcode):
    f_name = driver.find_element_by_name("first")
    f_name.clear()
    f_name.send_keys(first)

    l_name = driver.find_element_by_name("last")
    l_name.clear()
    l_name.send_keys(last)

    zipC = driver.find_element_by_name("zipcode")
    zipC.clear()
    zipC.send_keys(zipcode)

    zipC.send_keys(Keys.RETURN)
    return 


def secure_answer_entry():
    c0 = driver.find_element_by_name("component0")
    c0.clear()
    c0.send_keys("mother")

    c1 = driver.find_element_by_name("component1")
    c1.clear()
    c1.send_keys("maiden")

    c2 = driver.find_element_by_name("component2")
    c2.clear()
    c2.send_keys("name")
    c2.send_keys(Keys.RETURN)
    return 

# test with requests
list_of_other_urls = ["",
                      "team", 
                      "Mothers-Maiden-Name-Demo", 
                      "Secure-Answers", 
                      "Full-Public-Info-Search",
                      "Full-Public-Info-Search?first_name=Steven&last_name=Tucker&zipcode=74012"]
# build table
t = PrettyTable(['URL', 'Status'])
ctr = 0
for url in list_of_other_urls:
    x = requests.get(baseURL+url)
    t.add_row([baseURL + url, str(x.status_code)])
    if x.status_code!=200:
        ctr +=1
print(t)
print("Tests passed = " + str(len(list_of_other_urls)-ctr) + "----Tests Failed = " + str(ctr))
time.sleep(5)


# show the root page 
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseURL)
url = driver.find_element_by_name("url")
url.clear()
url.send_keys("https://cheatsheetseries.owasp.org/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html")
url.send_keys(Keys.RETURN)
scheight = 10
while scheight > .1:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
    scheight -= .01
time.sleep(5)


# demo the mother maiden name table 
driver.get(baseURL + "Mothers-Maiden-Name-Demo")
enter_info("Conan", "O'Brien", "90067")
time.sleep(2)
scheight = 10
while scheight > .1:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
    scheight -= .01
time.sleep(2)

# create secure answer
driver.get(baseURL + "Secure-Answers")
secure_answer_entry()
time.sleep(2)
scheight = 10
while scheight > .1:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
    scheight -= .01
time.sleep(2)

# demo the full public info search 
driver.get(baseURL + "Full-Public-Info-Search")
for person in people_list:
    enter_info(person[0], person[1], person[2])
    time.sleep(2)
    scheight = 10
    while scheight > .1:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
        scheight -= .01
    driver.get(baseURL + "Full-Public-Info-Search")
    
time.sleep(2)

# demo the api  
driver.get(baseURL + "Full-Public-Info-Search?first_name=Conan&last_name=O'Brien&zipcode=90067")
scheight = 10
while scheight > .1:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
    scheight -= .01

