import csv

data = [
    ['Item', 'Quantity'],
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2],
    ['Red Pants', 4],
    ['Mug', 7]
]

try:
    with open('packing_list.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("The specified file does not exists.")
    with open('packing_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        
