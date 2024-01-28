import pandas as pd

df = pd.read_csv('your_data.csv')

columns_to_analyze = ['AmountOfPeopleWithHighEducation', 'PeopleWithHighEducationWithoutJob',
                      'AmountOfPeopleWithSecondaryEducation', 'PeopleWithSecondaryEducationWithoutJob',
                      'AmountOfPeopleWithoutEducation', 'PeopleWithoutEducationWithoutJob',
                      'AmountOfMales', 'AmountOfMalesWithoutJob',
                      'AmountOfFemales', 'AmountOfFemalesWithoutJob',
                      'AmountOfPeopleInRegion', 'AmountOfPeopleInRegionWithoutJob',
                      'AmountOf_15-24_PeopleInRegion', 'AmountOf_15-24_PeopleInRegionWithoutJob',
                      'AmountOf_15-64_PeopleInRegion', 'AmountOf_15-64_PeopleInRegionWithoutJob',
                      'AmountOf_25-34_PeopleInRegion', 'AmountOf_25-34_PeopleInRegionWithoutJob',
                      'AmountOf_35-44_PeopleInRegion', 'AmountOf_35-44_PeopleInRegionWithoutJob',
                      'AmountOf_45-54_PeopleInRegion', 'AmountOf_45-54_PeopleInRegionWithoutJob',
                      'AmountOf_55-64_PeopleInRegion', 'AmountOf_55-64_PeopleInRegionWithoutJob',
                      'AmountOf_65+_PeopleInRegion', 'AmountOf_65+_PeopleInRegionWithoutJob']

# Годы в данных
years = df['Year'].unique()

# Рассчитываем процентный рост для каждой колонки
growth_data = {}

for column in columns_to_analyze:
    initial_value = df[df['Year'] == years[0]][column].values[0]
    final_value = df[df['Year'] == years[-1]][column].values[0]

    growth_percentage = ((final_value - initial_value) / initial_value) * 100
    growth_data[column] = growth_percentage