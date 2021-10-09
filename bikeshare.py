import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Date 10-09-2021 project 3
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input('Enter the city name: ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        c()

    month = input('Enter the month name: ')
    while month not in ['all','january', 'february', 'march', 'april', 'may']:
        month = input('ENTER MONTH january, february, ... , june : ').lower()
    
  


    
    day = input('Enter the day: ').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('Enter the day: ').lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv('{}.csv'.format(city))

    #convert into date format yyyy-mm-dd
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #extract month for comparision
    df['month'] = df['Start Time'].dt.month

    #filter by month

    if month != 'all':
        # from the month index, we get the correspodeing order or int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #create the new dataframe
        df = df[df['month'] == month]

    # extract day 
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by day of week 
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print("Most common month is: ", df['month'].value_counts().idxmax())


    print("Most common day is: ", df['day_of_week'].value_counts().idxmax())


    df['hour'] = df['Start Time'].dt.hour
    print("Most common hour is: ", df['hour'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("The most common start station: ", df ['Start Station'].value_counts().idxmax())


    print("The most common end station: ", df['End Station'].value_counts().idxmax())


    print("The most frequent combination of start station and end station trip")
    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    sum_duration = df['Trip Duration'].sum() / 3600.0
    print("total travel time in hours is: ", sum_duration)

    mean_travel_time = df['Trip Duration'].mean() / 3600.0
    print("mean travel time in hours is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_types = df['User Type'].value_counts()
    print(user_types)

# use try-except in case some cities mising some values
    try: 
        user_gender = df['Gender'].value_counts()
        print(user_gender)

        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].value_counts().idxmax())
        print("The earliest year of birth is:",earliest_year_of_birth,
          ", most recent one is:",most_recent_year_of_birth,
           "and the most common one is: ",most_common_year_of_birth)
    except:
        print('no data available on the birth year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data (df):
    """Displays the data due filteration.
    5 rows will added in each press"""
    print('Would you like to view 5 rows of individual trip data? Enter yes or no?')
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
