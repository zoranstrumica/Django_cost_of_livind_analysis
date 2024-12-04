from django.shortcuts import render
import pandas as pd
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    # Вчитување на CSV фајлот
    df = pd.read_csv(r'D:\DJANGO_ALL\myproject\cost_of_living.csv')  # Користете `r` за raw string за да избегнете escape проблеми
    # Пресметување на просечниот `Cost_of_Living`
    average_cost_of_living = df['Cost_of_Living'].mean()
    max_cost_of_living = df['Cost_of_Living'].max()
    min_cost_of_living = df['Cost_of_Living'].min()
    # Заокружување на просекот на две децимали
    average_cost_of_living = round(average_cost_of_living, 2)
    max_cost_of_living = round(max_cost_of_living, 2)
    min_cost_of_living = round(min_cost_of_living, 2)
    
     # Пресметување на просек на `Cost_of_Living` по региони
    averages_by_region = (
        df.groupby('Region')['Cost_of_Living']
        .mean()
        .reset_index()
        .rename(columns={'Cost_of_Living': 'Average_Cost_of_Living'})
    )
    # Конвертирање во речник за полесно користење во темплејтот
    averages_by_region = averages_by_region.to_dict(orient='records')
    
    max_by_region = (
        df.groupby('Region')['Cost_of_Living']
        .max()
        .reset_index()
        .rename(columns={'Cost_of_Living': 'Max_Cost_of_Living'})
    )
    # Конвертирање во речник за полесно користење во темплејтот
    max_by_region = max_by_region.to_dict(orient='records')
    
    min_by_region = (
        df.groupby('Region')['Cost_of_Living']
        .min()
        .reset_index()
        .rename(columns={'Cost_of_Living': 'Min_Cost_of_Living'})
    )
    # Конвертирање во речник за полесно користење во темплејтот
    min_by_region = min_by_region.to_dict(orient='records')
    
    # Пресметување на просек на `Cost_of_Living` по земји
    averages_by_country = (
        df.groupby('Country')['Cost_of_Living']
        .mean()
        .reset_index()
        .rename(columns={'Cost_of_Living': 'Average_Cost_of_Living'})
    ).to_dict(orient='records')
    
     # Пресметување на максимален `Cost_of_Living` по земји
    max_by_country = (
        df.groupby('Country')['Cost_of_Living']
        .max()
        .reset_index()
        .rename(columns={'Cost_of_Living': 'Max_Cost_of_Living'})
    ).to_dict(orient='records')
    
    # Пресметување на минимален `Cost_of_Living` по земји
    min_by_country = (
        df.groupby('Country')['Cost_of_Living']
        .min()
        .reset_index()
        .rename(columns={'Cost_of_Living': 'Min_Cost_of_Living'})
    ).to_dict(orient='records')
    
    # Пресметување на општи статистики за Average_Monthly_Income
    average_monthly_income = round(df['Average_Monthly_Income'].mean(), 2)
    max_monthly_income = round(df['Average_Monthly_Income'].max(), 2)
    min_monthly_income = round(df['Average_Monthly_Income'].min(), 2)
    
    # Пресметување на просек на `Average_Monthly_Income` по региони
    averages_income_by_region = (
        df.groupby('Region')['Average_Monthly_Income']
        .mean()
        .reset_index()
        .rename(columns={'Average_Monthly_Income': 'Average_Income_By_Region'})
    ).to_dict(orient='records')
    
    max_income_by_region = (
        df.groupby('Region')['Average_Monthly_Income']
        .max()
        .reset_index()
        .rename(columns={'Average_Monthly_Income': 'Max_Income_By_Region'})
    ).to_dict(orient='records')

    min_income_by_region = (
        df.groupby('Region')['Average_Monthly_Income']
        .min()
        .reset_index()
        .rename(columns={'Average_Monthly_Income': 'Min_Income_By_Region'})
    ).to_dict(orient='records')
    
    # Пресметување на просек, максимум и минимум на `Average_Monthly_Income` по земји
    averages_income_by_country = (
        df.groupby('Country')['Average_Monthly_Income']
        .mean()
        .reset_index()
        .rename(columns={'Average_Monthly_Income': 'Average_Income_By_Country'})
        .sort_values(by='Average_Income_By_Country', ascending=True)  # Сортирање од најголема кон најмала вредност
    ).to_dict(orient='records')

    max_income_by_country = (
        df.groupby('Country')['Average_Monthly_Income']
        .max()
        .reset_index()
        .rename(columns={'Average_Monthly_Income': 'Max_Income_By_Country'})
        .sort_values(by='Max_Income_By_Country', ascending=True)  # Сортирање
    ).to_dict(orient='records')

    min_income_by_country = (
        df.groupby('Country')['Average_Monthly_Income']
        .min()
        .reset_index()
        .rename(columns={'Average_Monthly_Income': 'Min_Income_By_Country'})
        .sort_values(by='Min_Income_By_Country', ascending=True)  # Сортирање
    ).to_dict(orient='records')

    
    # Податоци за прикажување на dashboard
    context = {
        'average_cost_of_living': average_cost_of_living,
        'max_cost_of_living': max_cost_of_living,
        'min_cost_of_living': min_cost_of_living,
        'averages_by_region': averages_by_region,
        'max_by_region': max_by_region,
        'min_by_region': min_by_region,
        'averages_by_country': averages_by_country,
        'max_by_country': max_by_country,
        'min_by_country': min_by_country,
        'average_monthly_income': average_monthly_income,
        'max_monthly_income': max_monthly_income,
        'min_monthly_income': min_monthly_income,
        'averages_income_by_region': averages_income_by_region,
        'max_income_by_region': max_income_by_region,
        'min_income_by_region': min_income_by_region,
        'averages_income_by_country': averages_income_by_country,
        'max_income_by_country': max_income_by_country,
        'min_income_by_country': min_income_by_country,
    }
    
    
    return render(request, 'dashboard.html', context)


@login_required(login_url="login")
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

@login_required(login_url="login")
def grafikoni_view(request):
    # Вчитување на CSV фајлот
    df = pd.read_csv('D:\DJANGO_ALL\myproject\cost_of_living.csv')
    
    # Групирање по региони и пресметување на просечен приход
    region_income = df.groupby('Region')['Average_Monthly_Income'].mean().reset_index()
    region_cost_of_living = df.groupby('Region')['Cost_of_Living'].mean().reset_index()

    # Претворање на податоците во листи за графиконот
    regions = region_income['Region'].tolist()
    average_income = region_income['Average_Monthly_Income'].tolist()
    average_cost_of_living = region_cost_of_living['Cost_of_Living'].tolist()
    
    context = {
        'regions': regions,  # Список со имиња на региони
        'average_income': average_income,  # Список со просечни приходи
        'average_cost_of_living': average_cost_of_living,  # Список со просечни приходи
        
    }
    return render(request, 'grafikoni.html', context)

@login_required(login_url="login")
def cost_of_living_by_year_view(request):
    # Вчитување на CSV фајлот
    df = pd.read_csv('D:\DJANGO_ALL\myproject\cost_of_living.csv')
    
    # Заменете ги `0` со просечни вредности за сите нумерички колони
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_columns:
        df[col] = df[col].replace(0, df[col].mean())

    # Групирање по `Year` и `Region` и пресметување на просек
    yearly_region_cost = df.groupby(['Year', 'Region'])['Cost_of_Living'].mean().reset_index()
    yearly_region_monthly_income = df.groupby(['Year', 'Region'])['Average_Monthly_Income'].mean().reset_index()

    # Список на сите години, конвертирано во Python `int`
    years = sorted([int(year) for year in df['Year'].unique()])

    # Список на сите региони
    regions = sorted(df['Region'].unique())

    # Подготовка на податоците за секој регион
    region_yearly_cost_of_living = {
        region: yearly_region_cost[yearly_region_cost['Region'] == region]
        .set_index('Year')['Cost_of_Living']
        .reindex(years, fill_value=0)  # Пополнување на недостасувачки години со 0
        .tolist()
        for region in regions
    }
    
    # Подготовка на податоците за приход по години за секој регион
    region_yearly_income = {
        region: yearly_region_monthly_income[yearly_region_monthly_income['Region'] == region]
        .set_index('Year')['Average_Monthly_Income']
        .reindex(years, fill_value=0)  # Пополнување на недостасувачки години со 0
        .tolist()
        for region in regions
    }

    context = {
        'years': years,  # Список на години
        'regions': regions,  # Список на региони
        'region_yearly_cost_of_living': region_yearly_cost_of_living,
        'region_yearly_income': region_yearly_income,
    }

    return render(request, 'godisni_proseci.html', context)