from bs4 import BeautifulSoup
import requests
import csv

csvFilePath = 'salmonella_onions_table.csv'
jsonFilePath = 'salmonella_onions_table.json'
url = 'https://www.cdc.gov/salmonella/newport-07-20/map.html'
content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')

contentTable = soup.find('tbody')
rows = contentTable.find_all('tr')
with open('output.csv','w') as csv_file:
    writer = csv.writer(csv_file)
    for row in rows[:-1]:
        data = [th.text.rstrip() for th in row.find_all('td')]
        print(data)
        writer.writerow(data)
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['id']
        data[id] = rows

with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))