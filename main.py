import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


url = "https://reedsy.com/discovery/blog/best-books-to-read-in-a-lifetime"
base_url = "https://reedsy.com/"

r = requests.get(url)
soup = bs(r.text, 'html.parser')
if soup:
    print("connection made")

# books = soup.find_all("//*[@class_='blurb']")
# print(f'There are {len(books)} books')
print(soup)