import requests
from bs4 import BeautifulSoup

# Make a request to the website
URL = "https://chaldal.com/"
page = requests.get(URL)

# Parse the HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# Find all links on the page
links = soup.find_all('a')

# Find the first element with the class "content"
content = soup.select('.content')[0]

# Find all elements with the class "product" and extract the text
products = [p.text for p in soup.select('.product')]

# Print the results
print(links)
print(content)
print(products)
