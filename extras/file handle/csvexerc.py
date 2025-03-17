import csv

file_path = 'bestseller.csv'

best_selling_book = None
max_sales = 0

with open(file_path, 'r', encoding="utf8") as file:
    reader = csv.reader(file)

    file.readline() #skip the header

    for row in reader:
        current_sales = float(row[4])
        if current_sales > max_sales:
            max_sales = current_sales
            best_selling_book = row

with open('bestseller_info.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(['Book', 'Author', 'sales in millions'])
    csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])
    