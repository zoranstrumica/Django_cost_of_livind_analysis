from django.shortcuts import render
import pandas as pd

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def cost_of_living_view(request):
    # Читање на CSV фајлот
    df = pd.read_csv('D:\DJANGO_ALL\myproject\cost_of_living.csv')
    # Izvleci gi podatocite od csv fajlot
    cost_of_living_data = df.to_dict(orient='records')
    
    # Основна статистика за сите нумерички податоци
    basic_stats = df.describe().transpose()

    # Преименување на колоните за да се избегнат специјални знаци
    basic_stats.rename(
        columns={"25%": "percent_25", "50%": "percent_50", "75%": "percent_75"},
        inplace=True
    )

    # Конвертирање на DataFrame во речник за темплејтот
    stats_dict = basic_stats.to_dict(orient='index')
    
    # Уникатни и сортирани години како стандардни цели броеви
    years = list(map(int, sorted(df['Year'].unique())))  # Конверзија во int
    
    
    education_costs = (
    df.groupby('Year')['Education_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    healthcare_costs = (
    df.groupby('Year')['Healthcare_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    transportation_costs = (
    df.groupby('Year')['Transportation_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    housing_costs = (
    df.groupby('Year')['Housing_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    
    cost_of_living = (
        df.groupby('Year')['Cost_of_Living']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    average_monthly_income = (
        df.groupby('Year')['Average_Monthly_Income']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    savings_percentage = (
        df.groupby('Year')['Savings_Percentage']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    # Извлекување на уникатни држави и региони
    unique_countries = df['Country'].unique().tolist()
    unique_regions = df['Region'].unique().tolist()
    
    # Броење на уникатни држави и региони
    number_of_unique_countries = len(unique_countries)
    number_of_unique_regions = len(unique_regions)
    
    context = {
        'cost_of_living_data': cost_of_living_data,
        'basic_stats': stats_dict,
        'years': years,
        'education_costs': education_costs,
        'healthcare_costs': healthcare_costs,
        'transportation_costs': transportation_costs,
        'housing_costs': housing_costs,
        'cost_of_living': cost_of_living,  # Нови податоци за Cost_of_Living
        'average_monthly_income': average_monthly_income,  # Нови податоци за Average_Monthly_Income
        'savings_percentage': savings_percentage,
        'unique_countries': unique_countries,  # Листа со уникатни држави
        'unique_regions': unique_regions,  # Листа со уникатни региони
        'number_of_unique_countries': number_of_unique_countries,  # Број на уникатни држави
        'number_of_unique_regions': number_of_unique_regions,  # Број на уникатни региони
    }
    return render(request, 'general_data.html', context)

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
    df.groupby('Year')['Education_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    healthcare_costs = (
    df.groupby('Year')['Healthcare_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    transportation_costs = (
    df.groupby('Year')['Transportation_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    housing_costs = (
    df.groupby('Year')['Housing_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    
    cost_of_living = (
        df.groupby('Year')['Cost_of_Living']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    average_monthly_income = (
        df.groupby('Year')['Average_Monthly_Income']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    savings_percentage = (
        df.groupby('Year')['Savings_Percentage']
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
    df.groupby('Year')['Education_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    healthcare_costs = (
    df.groupby('Year')['Healthcare_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    transportation_costs = (
    df.groupby('Year')['Transportation_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    housing_costs = (
    df.groupby('Year')['Housing_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    
    cost_of_living = (
        df.groupby('Year')['Cost_of_Living']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    average_monthly_income = (
        df.groupby('Year')['Average_Monthly_Income']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    savings_percentage = (
        df.groupby('Year')['Savings_Percentage']
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
    df.groupby('Year')['Education_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    healthcare_costs = (
    df.groupby('Year')['Healthcare_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    transportation_costs = (
    df.groupby('Year')['Transportation_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    housing_costs = (
    df.groupby('Year')['Housing_Cost_Percentage']
    .mean()
    .reindex(years, fill_value=0)  # Пополнување со 0 ако нема податоци
    .tolist()
)
    
    cost_of_living = (
        df.groupby('Year')['Cost_of_Living']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    average_monthly_income = (
        df.groupby('Year')['Average_Monthly_Income']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    savings_percentage = (
        df.groupby('Year')['Savings_Percentage']
        .mean()
        .reindex(years, fill_value=0)
        .tolist()
    )
    
    context = {
        'europe_data': europe_data_dict,  # Сите податоци за Австралија
        'yearly_trends': yearly_trends_dict,  # Трендови по години
        'europe_stats': europe_stats_dict,  # Основна статистика
        'years': years,  # Уникатни и сортирани години за Австралија
        'education_costs': education_costs,
        'healthcare_costs': healthcare_costs,
        'transportation_costs': transportation_costs,
        'housing_costs': housing_costs,
        'cost_of_living': cost_of_living,  # Нови податоци за Cost_of_Living
        'average_monthly_income': average_monthly_income,  # Нови податоци за Average_Monthly_Income
        'savings_percentage': savings_percentage,
    }
    return render(request, 'europe_analysis.html', context)

