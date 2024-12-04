from django.shortcuts import render
import pandas as pd
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def australia_data_view(request):
    # Вчитување на CSV фајлот
    df = pd.read_csv('D:\DJANGO_ALL\myproject\cost_of_living.csv')
    
    # Филтрирање на податоците само за Австралија
    australia_data = df[df['Country'] == 'Australia']
    
    # Уникатни и сортирани години како стандардни цели броеви
    years = list(map(int, sorted(australia_data['Year'].unique())))
    
    # Групирање по години и пресметување на просечни вредности
    yearly_trends = australia_data.groupby('Year')[['Cost_of_Living', 'Average_Monthly_Income']].mean().reset_index()
    
    # Конвертирање на податоците за Австралија во речник за темплејтот
    australia_data_dict = australia_data.to_dict(orient='records')
    yearly_trends_dict = yearly_trends.to_dict(orient='records')
    
    # Основна статистика за сите нумерички податоци
    australia_stats = australia_data.describe().transpose()

    # Преименување на колоните за да се избегнат специјални знаци
    australia_stats.rename(
        columns={"25%": "percent_25", "50%": "percent_50", "75%": "percent_75"},
        inplace=True
    )
     # Конвертирање на статистиките во речник за темплејтот
    australia_stats_dict = australia_stats.to_dict(orient='index')
    
    education_costs = (
    australia_data.groupby('Year')['Education_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    healthcare_costs = (
    australia_data.groupby('Year')['Healthcare_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    transportation_costs = (
    australia_data.groupby('Year')['Transportation_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    housing_costs = (
    australia_data.groupby('Year')['Housing_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    
    cost_of_living = (
        australia_data.groupby('Year')['Cost_of_Living']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    average_monthly_income = (
        australia_data.groupby('Year')['Average_Monthly_Income']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    savings_percentage = (
        australia_data.groupby('Year')['Savings_Percentage']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    context = {
        'australia_data': australia_data_dict,  # Сите податоци за Австралија
        'yearly_trends': yearly_trends_dict,  # Трендови по години
        'australia_stats': australia_stats_dict,  # Основна статистика
        'years': years,  # Уникатни и сортирани години за Австралија
        'education_costs': education_costs,
        'healthcare_costs': healthcare_costs,
        'transportation_costs': transportation_costs,
        'housing_costs': housing_costs,
        'cost_of_living': cost_of_living,  # Нови податоци за Cost_of_Living
        'average_monthly_income': average_monthly_income,  # Нови податоци за Average_Monthly_Income
        'savings_percentage': savings_percentage,
    }
    return render(request, 'australia_analysis.html', context)

@login_required(login_url="login")
def germany_data_view(request):
    # Вчитување на CSV фајлот
    df = pd.read_csv('D:\DJANGO_ALL\myproject\cost_of_living.csv')
    
    # Филтрирање на податоците само за Австралија
    germany_data = df[df['Country'] == 'Germany']
    
    # Уникатни и сортирани години како стандардни цели броеви
    years = list(map(int, sorted(germany_data['Year'].unique())))
    
    # Групирање по години и пресметување на просечни вредности
    yearly_trends = germany_data.groupby('Year')[['Cost_of_Living', 'Average_Monthly_Income']].mean().reset_index()
    
    # Конвертирање на податоците за Австралија во речник за темплејтот
    germany_data_dict = germany_data.to_dict(orient='records')
    yearly_trends_dict = yearly_trends.to_dict(orient='records')
    
    # Основна статистика за сите нумерички податоци
    germany_stats = germany_data.describe().transpose()

    # Преименување на колоните за да се избегнат специјални знаци
    germany_stats.rename(
        columns={"25%": "percent_25", "50%": "percent_50", "75%": "percent_75"},
        inplace=True
    )
     # Конвертирање на статистиките во речник за темплејтот
    germany_stats_dict = germany_stats.to_dict(orient='index')
    
    education_costs = (
    germany_data.groupby('Year')['Education_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    healthcare_costs = (
    germany_data.groupby('Year')['Healthcare_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    transportation_costs = (
    germany_data.groupby('Year')['Transportation_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    housing_costs = (
    germany_data.groupby('Year')['Housing_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    
    cost_of_living = (
        germany_data.groupby('Year')['Cost_of_Living']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    average_monthly_income = (
        germany_data.groupby('Year')['Average_Monthly_Income']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    savings_percentage = (
        germany_data.groupby('Year')['Savings_Percentage']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    context = {
        'germany_data': germany_data_dict,  # Сите податоци за Австралија
        'yearly_trends': yearly_trends_dict,  # Трендови по години
        'germany_stats': germany_stats_dict,  # Основна статистика
        'years': years,  # Уникатни и сортирани години за Австралија
        'education_costs': education_costs,
        'healthcare_costs': healthcare_costs,
        'transportation_costs': transportation_costs,
        'housing_costs': housing_costs,
        'cost_of_living': cost_of_living,  # Нови податоци за Cost_of_Living
        'average_monthly_income': average_monthly_income,  # Нови податоци за Average_Monthly_Income
        'savings_percentage': savings_percentage,
    }
    return render(request, 'germany_analysis.html', context)