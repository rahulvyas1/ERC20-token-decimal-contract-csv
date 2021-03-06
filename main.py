import requests
import csv
import time
URL = "http://api.ethplorer.io/"
REQUEST_URL = "getTokenInfo/"
token_address = "0xb8c77482e45f1f44de1745f52c74426c631bdd52"
API_URL = "?apiKey=freekey"

addresses = []
decimals = []
names = []


#Read from the CSV file
with open("/Users/rahulvyas/token_contract.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ' ',quotechar='|')
        for row in csv_reader:
            if len(row) <= 1:
                continue
            print(type(row))
            print(row[1].replace("'", "")[:-1])
            addresses.append(row[1].replace("'", "")[:-1])


#Pulling data & Writing to CSV 

#####WARNING#####
##ETHPLORER API allows 1 call ever 2 seconds for testing##
with open('/Users/rahulvyas/coins_data.txt', 'w') as txtFile:
    for address in addresses:
        data = requests.get(URL+REQUEST_URL+address+API_URL)
        #wait 2 seconds after 1 request
        txtFile.write(data.json()['name'] + ": " + data.json()['symbol'] + ": " + address + " ," + str(data.json()['decimals']) + "\n" )
        print(data.json()['name'] + ": " + data.json()['symbol'] + ": " + address + " ," + str(data.json()['decimals']))
        time.sleep(1)

