# with open('notes.txt', 'w') as file:
#     file.write("This is a test file.\n")



# with open('notes.txt', 'r') as file:
#     content = file.read()
#     print(content)


# import csv
# with open('user.csv','w',newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Age', 'City'])
#     writer.writerow(['Alice', 30, 'New York'])
#     writer.writerow(['Bob', 25, 'Los Angeles'])
#     writer.writerow(['Charlie', 35, 'Chicago'])



# with open('user.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


import json
# data=[{
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# },{
#     "name": "Alice",
#     "age": 25,
#     "city": "Los Angeles"
# },{
#     "name": "Bob",
#     "age": 35,
#     "city": "Chicago"
# }]
# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)


# with open('data.json', 'r') as file:
#     data = json.load(file)
#     for item in data:
#         print(f"Name: {item['name']}, Age: {item['age']}, City: {item['city']}")

