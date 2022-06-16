
from email.errors import HeaderDefect
from bs4 import BeautifulSoup
import requests

#we create a variable to store the server's response object in i.e. req variable
req = requests.get('https://tasty.co/article/melissaharrison/easy-dinner-recipes')

#we pick out specifically the html of the document 
html = req.text

#we ren the html through beautiful soup and create an instance of BeautifulSoup using the soup variable
soup = BeautifulSoup(html, 'lxml')

######--------------------RECIPE TITLES----------------------#########

""" #we search for all the spans with the specific class representing the recipe titles 
recipe_titles = soup.find_all('span', class_='js-subbuzz__title-text')

#wrapping everything in a for loop so we can iterate through all recipes and print clean titles
for recipes in recipe_titles: 
    print(recipes.text)
 """

######--------------------RECIPE TITLES----------------------#########


#get all recipe links
recipe_links = soup.find('a', class_='js-skimlink-subtag-modified')

print(recipe_links)

#create anoter for loop to iterate througha all items 
f""" or recipes in recipe_links: 
    print(recipes.href) """

#Practicing beautifulsoup prettify to print nicely organized html in terminal 
#print(soup.prettify)
