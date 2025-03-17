import csv

data = [
    ['Name', 'Age', 'Grade'],
    ['Joao', 18, 'A'],
    ['Bob', 22, 'B'],
    ['Charlie', 28, 'A+']
]

with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerows(data)

with open('output.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)