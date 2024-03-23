import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male_df = df[df['sex'] == 'Male']
    average_age_men = male_df['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    all_people = df.shape[0]
    bachelors_people = sum(df['education'] == 'Bachelors')
    percentage_bachelors = (bachelors_people / all_people) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df['education'].value_counts().loc[['Bachelors', 'Masters', 'Doctorate']].sum()
    total_education = df['education'].value_counts().sum()
    lower_education = total_education - higher_education

    # percentage with salary >50K
    # create dataframe with people of higher education
    higher_df = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    #find no of people in higher education earning >50K
    higher_education_high_salary_count = (higher_df['salary'] == '>50K').sum()
    #percentage of higher_education earning above 50K
    higher_education_rich = (higher_education_high_salary_count / higher_education) * 100
    #total number of population earning >50K
    pop_rich = (df['salary'] == '>50K').sum()
    #total no of lower education earning >50K
    total_lower_rich = pop_rich - higher_education_high_salary_count
    #percentage of lower education earning >50K
    lower_education_rich = (total_lower_rich / lower_education) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

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
