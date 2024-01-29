import csv

csv_file_path1 = 'data/Доласци туриста - годишњи подаци.csv'
csv_file_path2 = 'data/Домаћинства која поседују широкопојасну интернет конекцију, по.csv'
csv_file_path3 = 'data/Предузећа која имају веб сајт, по регионима.csv'
csv_file_path4 = 'data/Укупно становништво према радној активности, образовању и региону..csv'
csv_file_path5 = 'data/Укупно становништво према радној активности, полу и региону. Годишњи.csv'
csv_file_path6 = 'data/Укупно становништво према радној активности, старости и региону.csv'

output_csv_file_path = 'data/main-table.csv'

with open(csv_file_path1, 'r', newline='', encoding='utf-8') as file1, \
        open(csv_file_path2, 'r', newline='', encoding='utf-8') as file2, \
        open(csv_file_path3, 'r', newline='', encoding='utf-8') as file3, \
        open(csv_file_path4, 'r', newline='', encoding='utf-8') as file4, \
        open(csv_file_path5, 'r', newline='', encoding='utf-8') as file5, \
        open(csv_file_path6, 'r', newline='', encoding='utf-8') as file6, \
        open(output_csv_file_path, 'w', newline='', encoding='utf-8') as output_file:
    csv_reader = csv.reader(file1, delimiter=';')

    csv_writer = csv.writer(output_file, delimiter=',') 

    header = next(csv_reader)

    # csv_writer.writerow(['Region', 'Year', 'TotalTourists','ForeignTourists'])
    regions = ["Београдски регион", "Регион Војводине", "РЕПУБЛИКА СРБИЈА", "Регион Шумадије и Западне Србије",
               "Регион Јужне и Источне Србије"]
    result_mass = []
    edited_row = []
    for row in csv_reader:
        if (int(row[8]) >= 2010) and (int(row[8]) <= 2020):
            if row[5] == "1":
                if row[2] in regions:
                    if row[3] == "0":
                        edited_row.append(row[2])
                        edited_row.append(row[8])
                        edited_row.append(row[9])
                    if row[3] == "2":
                        edited_row.append(row[9])
                        result_mass.append(edited_row)
                        edited_row = []

    csv_reader = csv.reader(file2, delimiter=';')

    header = next(csv_reader)

    for row in csv_reader:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[2] in regions:
                for i, x in enumerate(result_mass):
                    if (x[0] == row[2]) and (int(x[1]) == int(row[4])):
                        result_mass[i].append(row[5])

    csv_reader = csv.reader(file3, delimiter=';')

    header = next(csv_reader)

    for row in csv_reader:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[2] in regions:
                for i, x in enumerate(result_mass):
                    if (x[0] == row[2]) and (int(x[1]) == int(row[4])):
                        result_mass[i].append(row[5])

    csv_reader = csv.reader(file4, delimiter=';')

    header = next(csv_reader)

    data = list(csv_reader)

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "4") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "4") and (row[2] == "Незапослена лица"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "3") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "3") and (row[2] == "Незапослена лица"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "2") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "2") and (row[2] == "Незапослена лица"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))
    for i, x in enumerate(result_mass):
        if int(x[1]) < 2014:
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)

    csv_reader = csv.reader(file5, delimiter=';')

    header = next(csv_reader)

    data = list(csv_reader)

    ####### pol. Mus, zen
    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "1") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "1") and (row[2] == "Незапослена лица"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "2") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "2") and (row[2] == "Незапослена лица"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for i, x in enumerate(result_mass):
        if int(x[1]) < 2014:
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)

    csv_reader = csv.reader(file6, delimiter=';')

    header = next(csv_reader)

    data = list(csv_reader)

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "0") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "0") and (row[2] == "Незапослена лица"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "15-24") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "15-24") and (row[2] == "Незапослена лица"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "15-64") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "15-64") and (row[2] == "Незапослена лица"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "25-34") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "25-34") and (row[2] == "Незапослена лица"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "35-44") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "35-44") and (row[2] == "Незапослена лица"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "45-54") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "45-54") and (row[2] == "Незапослена лица"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "55-64") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "55-64") and (row[2] == "Незапослена лица"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))

    for row in data:
        if (int(row[4]) >= 2010) and (int(row[4]) <= 2020):
            if row[8] in regions:
                if (row[5] == "65") and (row[2] == "Укупно"):
                    for i, x in enumerate(result_mass):
                        if (x[0] == row[8]) and (int(x[1]) == int(row[4])):
                            result_mass[i].append(str(float(row[9]) * 1000))


    for i, x in enumerate(result_mass):
        if int(x[1]) < 2014:
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)
            result_mass[i].append(None)

    result_mass.insert(0,
                       ["Region", "Year", "TotalTourists", "ForeignTourists", "HousesWithInternet%", "CompaniesWithWebSites%",
                        "AmountOfPeopleWithHighEducation", "PeopleWithHighEducationWithoutJob",
                        "AmountOfPeopleWithSecondaryEducation", "PeopleWithSecondaryEducationWithoutJob",
                        "AmountOfPeopleWithoutEducation", "PeopleWithoutEducationWithoutJob",
                        "AmountOfMales", "AmountOfMalesWithoutJob", "AmountOfFemales", "AmountOfFemalesWithoutJob",
                        "AmountOfPeopleInRegion", "AmountOfPeopleInRegionWithoutJob", "AmountOf_15-24_PeopleInRegion",
                        "AmountOf_15-24_PeopleInRegionWithoutJob", "AmountOf_15-64_PeopleInRegion",
                        "AmountOf_15-64_PeopleInRegionWithoutJob", "AmountOf_25-34_PeopleInRegion",
                        "AmountOf_25-34_PeopleInRegionWithoutJob", "AmountOf_35-44_PeopleInRegion",
                        "AmountOf_35-44_PeopleInRegionWithoutJob", "AmountOf_45-54_PeopleInRegion",
                        "AmountOf_45-54_PeopleInRegionWithoutJob", "AmountOf_55-64_PeopleInRegion",
                        "AmountOf_55-64_PeopleInRegionWithoutJob", "AmountOf_65+_PeopleInRegion"])
    csv_writer.writerows(result_mass)
    print(result_mass)
