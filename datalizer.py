import requests, json

PUZZLE_PIECE_VALUE = 10


request = requests.get("http://localhost:5984/donors/_design/donors/_view/donors")

rows = request.json()["rows"]

index = 0

donors = {}

for row in rows:
    amount = int(row["value"][5])
    count = int(amount/PUZZLE_PIECE_VALUE)
    name = row["value"][2]
    location = row["value"][3]
    date = row["value"][4]
    drange = range(index, index+count)
    for i in drange:
        donors[i] = {"name": name, "location": location, "amount": amount}
        index += 1

with open('../json/donors.json', 'w') as outfile:
    json.dump(donors, outfile)