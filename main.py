import csv


csv_file_path1 = 'data/Доласци туриста - годишњи подаци.csv'
csv_file_path2 = 'data/Домаћинства која поседују широкопојасну интернет конекцију, по.csv'
csv_file_path3 = 'data/Предузећа која имају веб сајт, по регионима.csv'
csv_file_path4 = 'data/Укупно становништво према радној активности, образовању и региону..csv'
csv_file_path5 = 'data/Укупно становништво према радној активности, полу и региону. Годишњи.csv'
csv_file_path6 = 'data/Укупно становништво према радној активности, старости и региону..csv'

output_csv_file_path = 'data/main-table.csv'

with open(csv_file_path1, 'r', newline='', encoding='utf-8') as file1, \
        open(csv_file_path2, 'r', newline='', encoding='utf-8') as file2, \
        open(csv_file_path3, 'r', newline='', encoding='utf-8') as file3, \
        open(csv_file_path4, 'r', newline='', encoding='utf-8') as file4, \
        open(csv_file_path5, 'r', newline='', encoding='utf-8') as file5, \
        open(csv_file_path6, 'r', newline='', encoding='utf-8') as file6, \
        open(output_csv_file_path, 'w', newline='', encoding='utf-8') as output_file:

    csv_reader = csv.reader(file1, delimiter=';')

    csv_writer = csv.writer(output_file, delimiter=';')

    # header = next(csv_reader)

    # csv_writer.writerow(['Region', 'Year', 'TotalTourists','ForeignTourists'])

    result_mass = []
    edited_row = []
    for row in csv_reader:
        if int(row[8]) >= 2010:
            if row[5] == "1":
                if row[3] == "0":
                    edited_row.append(row[2])
                    edited_row.append(row[8])
                    edited_row.append(row[9])
                if row[3] == "2":
                    edited_row.append(row[9])
                    result_mass.append(edited_row)
                    csv_writer.writerow(edited_row)
                    edited_row = []

    print(result_mass)

    csv_reader = csv.reader(file2, delimiter=';')
