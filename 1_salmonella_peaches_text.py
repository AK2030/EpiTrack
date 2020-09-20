from bs4 import BeautifulSoup
import requests

url = 'https://www.cdc.gov/salmonella/enteritidis-08-20/index.html'
content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')

paragraphID = soup.find('div', {"class": "card-body bg-white"})
print(paragraphID.get_text())
