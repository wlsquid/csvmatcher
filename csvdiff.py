import csv



with open('products_export_2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # put the values you want matched here
    variantSku = ['1234','456']
    outputCSV = open('output.csv', 'w')
    for row in csv_reader:
           if row[2] in variantSku:
            # print({row[0]}','{row[1]})
            print(f'\t{row[0]} , {row[1]} , {row[2]}.')
            csv_writer = csv.writer(outputCSV, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csv_writer.writerow([row[0], row[1], row[2]])
            line_count += 1
    print(f'Processed {line_count} lines.')
