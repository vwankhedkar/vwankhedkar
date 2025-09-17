import csv
with open("myfile.csv","r") as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
print("*****************************************")
with open("myfile.csv","r") as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        print(lines)
print("*****************************************")
rows = []
with open("myfile.csv","r") as file:
    csvFile = csv.reader(file)
    header = next(csvFile)
    for lines in csvFile:
        rows.append(lines)
print(rows)
for row in rows:
    print(row)
['user', 'city', 'email']
['jake', 'Lucas', 'jake@mymail.com']
['lucas', 'London.lucas@mymail.com']
['Barcelona', 'Doha', 'Barcelona@mymail.com']
*****************************************
{'user': 'jake', 'city': 'Lucas', 'email': 'jake@mymail.com'}
{'user': 'lucas', 'city': 'London.lucas@mymail.com', 'email': None}
{'user': 'Barcelona', 'city': 'Doha', 'email': 'Barcelona@mymail.com'}
*****************************************
[['jake', 'Lucas', 'jake@mymail.com'], ['lucas', 'London.lucas@mymail.com'], ['Barcelona', 'Doha', 'Barcelona@mymail.com']]
['jake', 'Lucas', 'jake@mymail.com']
['lucas', 'London.lucas@mymail.com']
['Barcelona', 'Doha', 'Barcelona@mymail.com']
*******************************************************************************
import csv,json
with open("data.csv","w",newline="") as f:
    csv.writer(f).writerow(["name","age"])
    data = {"name":"Alice","age":25}
with open("data.json","w") as f:
    json.dump(data,f)
