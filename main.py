import pandas as pd

df = pd.read_csv('data/main-table.csv')
regions = ['РЕПУБЛИКА СРБИЈА', 'Београдски регион', 'Регион Војводине',
           'Регион Шумадије и Западне Србије', 'Регион Јужне и Источне Србије']
columns_to_analyze = ["AmountOfPeopleWithHighEducation", "PeopleWithHighEducationWithoutJob",
                        "AmountOfPeopleWithSecondaryEducation", "PeopleWithSecondaryEducationWithoutJob",
                        "AmountOfPeopleWithoutEducation", "PeopleWithoutEducationWithoutJob",
                        "AmountOfMales", "AmountOfMalesWithoutJob", "AmountOfFemales", "AmountOfFemalesWithoutJob",
                        "AmountOfPeopleInRegion", "AmountOfPeopleInRegionWithoutJob", "AmountOf_15-24_PeopleInRegion",
                        "AmountOf_15-24_PeopleInRegionWithoutJob", "AmountOf_15-64_PeopleInRegion",
                        "AmountOf_15-64_PeopleInRegionWithoutJob", "AmountOf_25-34_PeopleInRegion",
                        "AmountOf_25-34_PeopleInRegionWithoutJob", "AmountOf_35-44_PeopleInRegion",
                        "AmountOf_35-44_PeopleInRegionWithoutJob", "AmountOf_45-54_PeopleInRegion",
                        "AmountOf_45-54_PeopleInRegionWithoutJob", "AmountOf_55-64_PeopleInRegion",
                        "AmountOf_55-64_PeopleInRegionWithoutJob", "AmountOf_65+_PeopleInRegion"]

regions = df['Region'].unique()

# Рассчитываем процентный рост для каждой колонки внутри каждого региона
for column in columns_to_analyze:
    df[column + '_Growth'] = df.groupby('Region')[column].transform(lambda x: (x.iloc[-1] - x.iloc[0]) / x.iloc[0] * 100)

# Применяем отрицательную экстраполяцию для каждой колонки
for column in columns_to_analyze:
    growth_column = column + '_Growth'
    df[column] = df.apply(lambda row: row[column] * (1 + row[growth_column] / 100) if pd.notna(row[growth_column]) else row[column], axis=1)

# Удаляем временные столбцы с процентным ростом
df = df.drop(columns=[column + '_Growth' for column in columns_to_analyze])

# Сохраняем обновленные данные в новый CSV-файл
df.to_csv('extrapolated_data_by_region.csv', index=False)

# grouped_dfs = df.groupby('Region')
# region_dfs = []
# for region in regions:
#     if region in grouped_dfs.groups:
#         region_dfs.append(grouped_dfs.get_group(region))
# print(region_dfs)
#
# interpolated_dfs = []
#
#
# for region_df in region_dfs:
#     interpolated_df = region_df.drop('Region',axis=1).interpolate(method='linear', limit_direction='forward', axis=0)
#     interpolated_dfs.append(pd.concat([region_df['Region'], interpolated_df], axis=1))
#     interpolated_dfs.append(interpolated_df)
#
# print(interpolated_dfs)

# .interpolate(method='linear', limit_direction='forward', axis=0)
# df['Region'] = pd.Categorical(df['Region'])
# #
# # Затим, груписање по региону и рачунање суме за сваки регион
# print(df['Region'].unique())
# grouped_dfs = df.groupby('Region')
# print(df['Region'].unique())
# # Исписивање груписаних података
# print(grouped_dfs.get_group('Регион Војводине'))
# # grouped_dfs = df.groupby('Region')
# # grouped_dfs.first()
# # grouped_dfs.get_group(regions[0])
# # region_dfs = []
# # for region in regions:
# #     if region in grouped_dfs.groups:
# #         region_dfs.append(grouped_dfs.get_group(region))
# # # Рассчитываем процентный рост для каждой колонки
# # print(region_dfs)
