import pandas as pd

df = pd.read_csv('D:\DJANGO_ALL\myproject\cost_of_living.csv')
print(df)

print(df.columns)

# # Основна статистика за нумеричките колони
# basic_stats = df.describe()

# # Прикажување на резултатот
# print(basic_stats)

# years = sorted(df['Year'].unique())  # Уникатни и сортирани години
# education_costs = (
#     df.groupby('Year')['Education_Cost_Percentage']
#     .mean()
#     .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
#     .tolist()
# )
# print("Years:", years)
# print("Education Costs:", education_costs)