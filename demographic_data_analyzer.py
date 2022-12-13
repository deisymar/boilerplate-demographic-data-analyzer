import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    df.head()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race')['race'].count()

    # What is the average age of men?
    df_age_men = df['age'].where(df['sex']=='Male')
    #print(df_age_men)
    average_age_men = round(df_age_men.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    df_bachelors = df['education'].where(df['education']=='Bachelors')
    #print(df_bachelors.dropna().count())
    num_bachelors = df_bachelors.dropna().count()
    num_education_total = df['education'].count()
    percentage_bachelors = round((num_bachelors/num_education_total) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    df_filter_higher = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    
    df_filter_lower = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    
    higher_education = df_filter_higher['education'].dropna().count()
    
    lower_education = df_filter_lower['education'].dropna().count()
    
    # percentage with salary >50K
    higher_education_rich = round( df_filter_higher['salary'].where( df['salary'] == '>50K' ).dropna().count() / higher_education * 100, 1)
    
    lower_education_rich = round( df_filter_lower['salary'].where( df['salary'] == '>50K' ).dropna().count() / lower_education * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    workers_hours_min = df[df['hours-per-week'] == min_work_hours]
    
    workers_hoursmin_salary = workers_hours_min[ workers_hours_min['salary'] == '>50K'] 
    
    rich_percentage = round( len(workers_hoursmin_salary) / len(workers_hours_min) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    countrys_wealthy = df.groupby('native-country')['salary'].value_counts(normalize=True).loc[:, ('>50K')]
    
    highest_earning_country = countrys_wealthy.idxmax()
       
    highest_earning_country_percentage = round( countrys_wealthy.max() * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_india_wealthy = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    
    top_IN_occupation = df_india_wealthy['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
