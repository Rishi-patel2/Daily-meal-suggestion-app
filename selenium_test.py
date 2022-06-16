##Rishi Patel 
##python_recipe



####Libraries used
#webdriver is the basic import that you need in order to do anything in a specific browser in selenium
#By is an import for the find_element(by=By.CLASS_NAME, value="value") function - it's just a rule, idk why. 
#time is imported for a sleep function to keep the execution of commands sychronized with the browser 


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#including path to the chromedriver webdriver - needed to enable automated browser control
PATH = ("/Applications/chromedriver")

#instantiating the webdriver object and specifying chrome browser and subsequently linking path to executable 
browser = webdriver.Chrome(PATH)

#opens web browser on screen and goes to URL 
browser.get("https://tasty.co/article/melissaharrison/easy-dinner-recipes")

#we want to just grab the <a> tag that has the href to the recipe, but because the class is not uniquely named
#and there is no other attirbute as part of our desired <a> tag we are going to grab the div that is our <a> tags parent
descriptions = browser.find_elements(by=By.CLASS_NAME, value="subbuzz__description")

#creating a list to store all of our hrefs in in
hrefs = []


#here we wil construct a for loop that iterates through all of the elements with the class name "subbuzz__description"
#and we will extract the href for each one and store it in a separate list that we will print out at the end of the script
for description in descriptions: 
    a_tag = description.find_element(by=By.CLASS_NAME, value="js-skimlink-subtag-modified")
    hrefs.append(a_tag.get_attribute("href"))

#here we will extract specifically the <a> tag from within the parent div we just extracted 
#a_tag = descriptions.find_element(by=By.CLASS_NAME, value="js-skimlink-subtag-modified")

#now that we have the <a> tag element stored in a_tag we use get_attribute to get the specific value of the href attribute of the html element 
#href = a_tag.get_attribute("href")

#now we print the results 
print(*hrefs, sep='\n')

#a timed wait function
time.sleep(2)

#closing the browser window
browser.quit()

