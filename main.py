import requests
import csv

URL = "http://api.ethplorer.io/"
REQUEST_URL = "getTokenInfo/"
token_address = "0xb8c77482e45f1f44de1745f52c74426c631bdd52"
API_URL = "?apiKey=freekey"

data = requests.get(URL+REQUEST_URL+token_addres+API_URL)

print(data.json())
addresses = []

#Read from the CSV file
with open("/Users/rahulvyas/token_contract.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ' ',quotechar='|')
        for row in csv_reader:
            if len(row) <= 1:
                continue
            print(type(row))
            print(row[1].replace("'", "")[:-1])
            addresses.append(row[1].replace("'", "")[:-1])

