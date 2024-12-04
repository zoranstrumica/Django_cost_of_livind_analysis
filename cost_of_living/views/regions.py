from django.shortcuts import render
import pandas as pd
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def europe_data_view(request):
    # Вчитување на CSV фајлот
    df = pd.read_csv('D:\DJANGO_ALL\myproject\cost_of_living.csv')
    
    # Филтрирање на податоците само за Австралија
    europe_data = df[df['Region'] == 'Europe']
    
    # Уникатни и сортирани години како стандардни цели броеви
    years = list(map(int, sorted(europe_data['Year'].unique())))
    
    # Групирање по години и пресметување на просечни вредности
    yearly_trends = europe_data.groupby('Year')[['Cost_of_Living', 'Average_Monthly_Income']].mean().reset_index()
    
    # Конвертирање на податоците за Австралија во речник за темплејтот
    europe_data_dict = europe_data.to_dict(orient='records')
    yearly_trends_dict = yearly_trends.to_dict(orient='records')
    
    # Основна статистика за сите нумерички податоци
    europe_stats = europe_data.describe().transpose()

    # Преименување на колоните за да се избегнат специјални знаци
    europe_stats.rename(
        columns={"25%": "percent_25", "50%": "percent_50", "75%": "percent_75"},
        inplace=True
    )
     # Конвертирање на статистиките во речник за темплејтот
    europe_stats_dict = europe_stats.to_dict(orient='index')
    
    education_costs = (
    europe_data.groupby('Year')['Education_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    healthcare_costs = (
    europe_data.groupby('Year')['Healthcare_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    transportation_costs = (
    europe_data.groupby('Year')['Transportation_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    housing_costs = (
    europe_data.groupby('Year')['Housing_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    
    cost_of_living = (
        europe_data.groupby('Year')['Cost_of_Living']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    max_cost_of_living = (
        europe_data.groupby('Year')['Cost_of_Living']
        .max()
        .reindex(years, fill_value=0)
        .tolist()
    )
    min_cost_of_living = (
        europe_data.groupby('Year')['Cost_of_Living']
        .min()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    average_monthly_income = (
        europe_data.groupby('Year')['Average_Monthly_Income']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    savings_percentage = (
        europe_data.groupby('Year')['Savings_Percentage']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    context = {
        'europe_data': europe_data_dict,  
        'yearly_trends': yearly_trends_dict,  # Трендови по години
        'europe_stats': europe_stats_dict,  # Основна статистика
        'years': years,  # Уникатни и сортирани години за Австралија
        'education_costs': education_costs,
        'healthcare_costs': healthcare_costs,
        'transportation_costs': transportation_costs,
        'housing_costs': housing_costs,
        'cost_of_living': cost_of_living,  # Нови податоци за Cost_of_Living
        'max_cost_of_living': max_cost_of_living,  # Нови податоци за Cost_of_Living
        'min_cost_of_living': min_cost_of_living,  # Нови податоци за Cost_of_Living
        'average_monthly_income': average_monthly_income,  # Нови податоци за Average_Monthly_Income
        'savings_percentage': savings_percentage,
    }
    return render(request, 'europe_analysis.html', context)

@login_required(login_url="login")
def asia_data_view(request):
    # Вчитување на CSV фајлот
    df = pd.read_csv('D:\DJANGO_ALL\myproject\cost_of_living.csv')
    
    # Филтрирање на податоците само за Аsia
    asia_data = df[df['Region'] == 'Asia']
    
    # Уникатни и сортирани години како стандардни цели броеви
    years = list(map(int, sorted(asia_data['Year'].unique())))
    
    # Групирање по години и пресметување на просечни вредности
    yearly_trends = asia_data.groupby('Year')[['Cost_of_Living', 'Average_Monthly_Income']].mean().reset_index()
    
    # Конвертирање на податоците за Австралија во речник за темплејтот
    asia_data_dict = asia_data.to_dict(orient='records')
    yearly_trends_dict = yearly_trends.to_dict(orient='records')
    
    # Основна статистика за сите нумерички податоци
    asia_stats = asia_data.describe().transpose()

    # Преименување на колоните за да се избегнат специјални знаци
    asia_stats.rename(
        columns={"25%": "percent_25", "50%": "percent_50", "75%": "percent_75"},
        inplace=True
    )
     # Конвертирање на статистиките во речник за темплејтот
    asia_stats_dict = asia_stats.to_dict(orient='index')
    
    education_costs = (
    asia_data.groupby('Year')['Education_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    healthcare_costs = (
    asia_data.groupby('Year')['Healthcare_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    transportation_costs = (
    asia_data.groupby('Year')['Transportation_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    housing_costs = (
    asia_data.groupby('Year')['Housing_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    
    cost_of_living = (
        asia_data.groupby('Year')['Cost_of_Living']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    average_monthly_income = (
        asia_data.groupby('Year')['Average_Monthly_Income']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    savings_percentage = (
        asia_data.groupby('Year')['Savings_Percentage']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    context = {
        'asia_data': asia_data_dict,  # Сите податоци за Asia
        'yearly_trends': yearly_trends_dict,  # Трендови по години
        'asia_stats': asia_stats_dict,  # Основна статистика
        'years': years,  # Уникатни и сортирани години за Австралија
        'education_costs': education_costs,
        'healthcare_costs': healthcare_costs,
        'transportation_costs': transportation_costs,
        'housing_costs': housing_costs,
        'cost_of_living': cost_of_living,  # Нови податоци за Cost_of_Living
        'average_monthly_income': average_monthly_income,  # Нови податоци за Average_Monthly_Income
        'savings_percentage': savings_percentage,
    }
    return render(request, 'asia_analysis.html', context)

@login_required(login_url="login")
def africa_data_view(request):
    # Вчитување на CSV фајлот
    df = pd.read_csv('D:\DJANGO_ALL\myproject\cost_of_living.csv')
    
    # Филтрирање на податоците само за Аsia
    africa_data = df[df['Region'] == 'Africa']
    
    # Уникатни и сортирани години како стандардни цели броеви
    years = list(map(int, sorted(africa_data['Year'].unique())))
    
    # Групирање по години и пресметување на просечни вредности
    yearly_trends = africa_data.groupby('Year')[['Cost_of_Living', 'Average_Monthly_Income']].mean().reset_index()
    
    # Конвертирање на податоците за Австралија во речник за темплејтот
    africa_data_dict = africa_data.to_dict(orient='records')
    yearly_trends_dict = yearly_trends.to_dict(orient='records')
    
    # Основна статистика за сите нумерички податоци
    africa_stats = africa_data.describe().transpose()

    # Преименување на колоните за да се избегнат специјални знаци
    africa_stats.rename(
        columns={"25%": "percent_25", "50%": "percent_50", "75%": "percent_75"},
        inplace=True
    )
     # Конвертирање на статистиките во речник за темплејтот
    africa_stats_dict = africa_stats.to_dict(orient='index')
    
    education_costs = (
    africa_data.groupby('Year')['Education_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    healthcare_costs = (
    africa_data.groupby('Year')['Healthcare_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    transportation_costs = (
    africa_data.groupby('Year')['Transportation_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    housing_costs = (
    africa_data.groupby('Year')['Housing_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    
    cost_of_living = (
        africa_data.groupby('Year')['Cost_of_Living']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    average_monthly_income = (
        africa_data.groupby('Year')['Average_Monthly_Income']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    savings_percentage = (
        africa_data.groupby('Year')['Savings_Percentage']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    context = {
        'africa_data': africa_data_dict,  # Сите податоци за Asia
        'yearly_trends': yearly_trends_dict,  # Трендови по години
        'africa_stats': africa_stats_dict,  # Основна статистика
        'years': years,  # Уникатни и сортирани години за Австралија
        'education_costs': education_costs,
        'healthcare_costs': healthcare_costs,
        'transportation_costs': transportation_costs,
        'housing_costs': housing_costs,
        'cost_of_living': cost_of_living,  # Нови податоци за Cost_of_Living
        'average_monthly_income': average_monthly_income,  # Нови податоци за Average_Monthly_Income
        'savings_percentage': savings_percentage,
    }
    return render(request, 'africa_analysis.html', context)

@login_required(login_url="login")
def north_america_data_view(request):
    # Вчитување на CSV фајлот
    df = pd.read_csv('D:\DJANGO_ALL\myproject\cost_of_living.csv')
    
    # Филтрирање на податоците само за Аsia
    north_america_data = df[df['Region'] == 'North America']
    
    # Уникатни и сортирани години како стандардни цели броеви
    years = list(map(int, sorted(north_america_data['Year'].unique())))
    
    # Групирање по години и пресметување на просечни вредности
    yearly_trends = north_america_data.groupby('Year')[['Cost_of_Living', 'Average_Monthly_Income']].mean().reset_index()
    
    # Конвертирање на податоците за Австралија во речник за темплејтот
    north_america_data_dict = north_america_data.to_dict(orient='records')
    yearly_trends_dict = yearly_trends.to_dict(orient='records')
    
    # Основна статистика за сите нумерички податоци
    north_america_stats = north_america_data.describe().transpose()

    # Преименување на колоните за да се избегнат специјални знаци
    north_america_stats.rename(
        columns={"25%": "percent_25", "50%": "percent_50", "75%": "percent_75"},
        inplace=True
    )
     # Конвертирање на статистиките во речник за темплејтот
    north_america_stats_dict = north_america_stats.to_dict(orient='index')
    
    education_costs = (
    north_america_data.groupby('Year')['Education_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    healthcare_costs = (
    north_america_data.groupby('Year')['Healthcare_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    transportation_costs = (
    north_america_data.groupby('Year')['Transportation_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    housing_costs = (
    north_america_data.groupby('Year')['Housing_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    
    cost_of_living = (
        north_america_data.groupby('Year')['Cost_of_Living']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    average_monthly_income = (
        north_america_data.groupby('Year')['Average_Monthly_Income']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    savings_percentage = (
        north_america_data.groupby('Year')['Savings_Percentage']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    context = {
        'north_america_data': north_america_data_dict,  # Сите податоци за Asia
        'yearly_trends': yearly_trends_dict,  # Трендови по години
        'north_america_stats': north_america_stats_dict,  # Основна статистика
        'years': years,  # Уникатни и сортирани години за Австралија
        'education_costs': education_costs,
        'healthcare_costs': healthcare_costs,
        'transportation_costs': transportation_costs,
        'housing_costs': housing_costs,
        'cost_of_living': cost_of_living,  # Нови податоци за Cost_of_Living
        'average_monthly_income': average_monthly_income,  # Нови податоци за Average_Monthly_Income
        'savings_percentage': savings_percentage,
    }
    return render(request, 'north_america_analysis.html', context)

@login_required(login_url="login")
def oceania_data_view(request):
    # Вчитување на CSV фајлот
    df = pd.read_csv('D:\DJANGO_ALL\myproject\cost_of_living.csv')
    
    # Филтрирање на податоците само за Австралија
    oceania_data = df[df['Region'] == 'Oceania']
    
    # Уникатни и сортирани години како стандардни цели броеви
    years = list(map(int, sorted(oceania_data['Year'].unique())))
    
    # Групирање по години и пресметување на просечни вредности
    yearly_trends = oceania_data.groupby('Year')[['Cost_of_Living', 'Average_Monthly_Income']].mean().reset_index()
    
    # Конвертирање на податоците за Австралија во речник за темплејтот
    oceania_data_dict = oceania_data.to_dict(orient='records')
    yearly_trends_dict = yearly_trends.to_dict(orient='records')
    
    # Основна статистика за сите нумерички податоци
    oceania_stats = oceania_data.describe().transpose()

    # Преименување на колоните за да се избегнат специјални знаци
    oceania_stats.rename(
        columns={"25%": "percent_25", "50%": "percent_50", "75%": "percent_75"},
        inplace=True
    )
     # Конвертирање на статистиките во речник за темплејтот
    oceania_stats_dict = oceania_stats.to_dict(orient='index')
    
    education_costs = (
    oceania_data.groupby('Year')['Education_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    healthcare_costs = (
    oceania_data.groupby('Year')['Healthcare_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    transportation_costs = (
    oceania_data.groupby('Year')['Transportation_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    housing_costs = (
    oceania_data.groupby('Year')['Housing_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    
    cost_of_living = (
        oceania_data.groupby('Year')['Cost_of_Living']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    average_monthly_income = (
        oceania_data.groupby('Year')['Average_Monthly_Income']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    savings_percentage = (
        oceania_data.groupby('Year')['Savings_Percentage']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    context = {
        'oceania_data': oceania_data_dict,  
        'yearly_trends': yearly_trends_dict,  # Трендови по години
        'oceania_stats': oceania_stats_dict,  # Основна статистика
        'years': years,  # Уникатни и сортирани години за Австралија
        'education_costs': education_costs,
        'healthcare_costs': healthcare_costs,
        'transportation_costs': transportation_costs,
        'housing_costs': housing_costs,
        'cost_of_living': cost_of_living,  # Нови податоци за Cost_of_Living
        'average_monthly_income': average_monthly_income,  # Нови податоци за Average_Monthly_Income
        'savings_percentage': savings_percentage,
    }
    return render(request, 'oceania_analysis.html', context)

@login_required(login_url="login")
def south_america_data_view(request):
    # Вчитување на CSV фајлот
    df = pd.read_csv('D:\DJANGO_ALL\myproject\cost_of_living.csv')
    
    # Филтрирање на податоците само за Аsia
    south_america_data = df[df['Region'] == 'South America']
    
    # Уникатни и сортирани години како стандардни цели броеви
    years = list(map(int, sorted(south_america_data['Year'].unique())))
    
    # Групирање по години и пресметување на просечни вредности
    yearly_trends = south_america_data.groupby('Year')[['Cost_of_Living', 'Average_Monthly_Income']].mean().reset_index()
    
    # Конвертирање на податоците за Австралија во речник за темплејтот
    south_america_data_dict = south_america_data.to_dict(orient='records')
    yearly_trends_dict = yearly_trends.to_dict(orient='records')
    
    # Основна статистика за сите нумерички податоци
    south_america_stats = south_america_data.describe().transpose()

    # Преименување на колоните за да се избегнат специјални знаци
    south_america_stats.rename(
        columns={"25%": "percent_25", "50%": "percent_50", "75%": "percent_75"},
        inplace=True
    )
     # Конвертирање на статистиките во речник за темплејтот
    south_america_stats_dict = south_america_stats.to_dict(orient='index')
    
    education_costs = (
    south_america_data.groupby('Year')['Education_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    healthcare_costs = (
    south_america_data.groupby('Year')['Healthcare_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    transportation_costs = (
    south_america_data.groupby('Year')['Transportation_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    housing_costs = (
    south_america_data.groupby('Year')['Housing_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    
    cost_of_living = (
        south_america_data.groupby('Year')['Cost_of_Living']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    average_monthly_income = (
        south_america_data.groupby('Year')['Average_Monthly_Income']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    savings_percentage = (
        south_america_data.groupby('Year')['Savings_Percentage']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    context = {
        'south_america_data': south_america_data_dict,  # Сите податоци за Asia
        'yearly_trends': yearly_trends_dict,  # Трендови по години
        'south_america_stats': south_america_stats_dict,  # Основна статистика
        'years': years,  # Уникатни и сортирани години за Австралија
        'education_costs': education_costs,
        'healthcare_costs': healthcare_costs,
        'transportation_costs': transportation_costs,
        'housing_costs': housing_costs,
        'cost_of_living': cost_of_living,  # Нови податоци за Cost_of_Living
        'average_monthly_income': average_monthly_income,  # Нови податоци за Average_Monthly_Income
        'savings_percentage': savings_percentage,
    }
    return render(request, 'south_america_analysis.html', context)


