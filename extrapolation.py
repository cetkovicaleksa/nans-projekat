import pandas as pd

df = pd.read_csv('data/main-table.csv')
df_ind = df[
            ['Region', 'Year', 'TotalTourists', 'ForeignTourists', 'HousesWithInternet%', 'CompaniesWithWebSites%']]
df_without_ind = df.drop(columns=['Region', 'Year', 'TotalTourists', 'ForeignTourists', 'HousesWithInternet%',
                                          'CompaniesWithWebSites%'])
for i in range(20):
    df_without_ind.iloc[19 - i] = df_without_ind.iloc[24 - i] - (df_without_ind.iloc[29 - i] - df_without_ind.iloc[24 - i])

result_df = pd.merge(df_ind, df_without_ind, left_index=True, right_index=True)

print(result_df)

result_df.to_csv('data/extrapolated_data.csv', index=False)
# print(region_dfs)
# print(df.iloc[15])

# for col in columns_to_analyze:
#     for region_df in region_dfs:
#         region_df[col] = region_df[col].apply(fill_missing_values)
#
# # Создаем новый DataFrame с интерполированными значениями
# interpolated_dfs = []
# for region_df in region_dfs:
#     interpolated_df = region_df.drop('Region', axis=1).interpolate(method='linear', limit_direction='forward', axis=0).ffill().bfill()
#     interpolated_dfs.append(pd.concat([region_df['Region'], interpolated_df], axis=1))

# Сохраняем результат в новый CSV-файл
# result_df = pd.concat(interpolated_dfs)
# result_df.to_csv('data/interpolated_data1.csv', index=False)

#
# interpolated_dfs = []
#
# for region_df in region_dfs:
#     interpolated_df = region_df.drop('Region', axis=1).interpolate(method='linear', limit_direction='forward', axis=0).ffill().bfill()
#     interpolated_dfs.append(pd.concat([region_df['Region'], interpolated_df], axis=1))
#     # interpolated_dfs.append(interpolated_df)
#
# print(interpolated_dfs)

# regions = df['Region'].unique()
#
# # Рассчитываем процентный рост для каждой колонки внутри каждого региона
# for column in columns_to_analyze:
#     df[column + '_Growth'] = df.groupby('Region')[column].transform(lambda x: (x.iloc[-1] - x.iloc[0]) / x.iloc[0] * 100)
#
# # Применяем отрицательную экстраполяцию для каждой колонки
# for column in columns_to_analyze:
#     growth_column = column + '_Growth'
#     df[column] = df.apply(lambda row: row[column] * (1 + row[growth_column] / 100) if pd.notna(row[growth_column]) else row[column], axis=1)
#
# # Удаляем временные столбцы с процентным ростом
# df = df.drop(columns=[column + '_Growth' for column in columns_to_analyze])
#
# # Сохраняем обновленные данные в новый CSV-файл
# df.to_csv('extrapolated_data_by_region.csv', index=False)
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
