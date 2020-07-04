import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city you wish to obtain stats for: \n")
    cities = ['Chicago', 'chicago', 'New York City','new york city', 'Washington','washington']
    months = ['All', 'all', 'January', 'january', 'February', 'february', 'March', 'march', 'April', 'april', 'May', 'may', 'June', 'june']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday','All', 'all', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']
    #The while loop checks whether the city entered is found in the CITY_DATA dictionary and tell the user to renter the city if not found
    while city not in cities :
        city = input("You entered the wrong city! please enter either Chicago, New York City or Washington to get stats for: \n")
    # TO DO: get user input for month (all, january, february, ... , june)

    month = input("Enter the month you wish to obtain stats or all if you wants stats for all months: \n")
    #The while loop checks whether the month entered is found in the months list and tell the user to renter the month if not found
    while month not in months :
        month = input("You entered the wrong month! Please enter either January, February, March, April, May, June or all to get stats for all months: \n")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day you wish to obtain stats or all if you wants stats for all days: \n")
    #The while loop checks whether the day entered is found in the days list and tell the user to renter the day if not found
    while day not in days :
        day = input("You entered the wrong day! Please enter either Monday, Tuesday,Wednesday,Thurday,Friday, Saturday, Sunday or all to get stats for all days: \n")
    print('-'*120)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
    # use the index of the months list to get the corresponding int 
        months = ['january', 'february', 'march', 'april', 'may', 'june','January', 'February', 'March', 'April', 'May', 'June']
        if months.index(month) <= 5 :
            month = months.index(month) + 1
        else:  
            month = months.index(month)-5
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
       

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from the Start Time column to create an hour column
    df['month'] = df['Start Time'].dt.month
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('\nCommon month of travel...')
    if popular_month ==1 :
        pop_month = 'January'
        print('Most common month of travel:', pop_month)
    elif popular_month ==2 :
        pop_month = 'February'
        print('Most common month of travel:', pop_month)
    elif popular_month ==3 :
        pop_month = 'March'
        print('Most common month of travel:', pop_month)
    elif popular_month ==4 :
        pop_month = 'April'
        print('Most common month of travel:', pop_month)
    elif popular_month ==5 :
        pop_month = 'May'
        print('Most common month of travel:', pop_month)
    else :
        pop_month = 'June'
        print('Most common month of travel:', pop_month)
    

    # TO DO: display the most common day of week
    # extract day from the Start Time column to create an hour column
    df['day'] = df['Start Time'].dt.weekday_name
    # find the most popular day
    popular_day = df['day'].mode()[0]
    print('\nCommon day of travel...')
    print('Most common day of travel:', popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('\nCommon hour of travel...')
    print('Most common hour of travel:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nCommon Start station...')
    print('Most common Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['Start Station'].mode()[0]
    print('\nCommon End station...')
    print('Most common End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + ' to ' + df['End Station']
    popular_station_combination = df['Combination'].mode()[0]
    print('\nCommon combination of start station and end station trip...')
    print('Most common combination of start station and end station trip:', popular_station_combination)
    # TO DO: Satrt station of shortes trip
    print('\nStart stations of shortest journeys...')
    print('Start stations of shortest journeys:')
    """print(df.query("Trip Duration == 3")["Start Station"].head())"""
   
    print(df[df['Trip Duration']== df['Trip Duration'].min()]['Start Station'].values)
    #TO DO: End stations of shortest journeys
    print('\nEnd stations of shortest journeys...')
    print('End stations of shortest journeys:')
    print(df[df['Trip Duration']== df['Trip Duration'].min()]['End Station'].values)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    """df['End hour'] = pd.to_datetime(df['End Time'], errors='coerce')
    df['Start hour'] = pd.to_datetime(df['Start Time'], errors='coerce')
    df['Duration'] = df['End hour'] - df['Start hour']"""
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal time of travel...')
    print("Total time of travel: {} seconds".format(total_travel_time))
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nAverage time of travel...')
    print("Average of travel: {} seconds".format(mean_travel_time))
    # TO DO: display maximum travel time
    max_travel_time = df['Trip Duration'].max()
    print('\nMaximum time of travel...')
    print("Maximum time of travel:{} seconds".format(max_travel_time)) 
    # TO DO: display minimum travel time
    min_travel_time = df['Trip Duration'].min()
    print('\nMinimum time of travel...')
    print("Minimum time of travel:{} seconds".format(min_travel_time))
    # TO DO: display standard deviation of travel time
    std_travel_time = df['Trip Duration'].std()
    print('\nStandard deviation of time of travel...')
    print("Standard deviation of time of travel:{} seconds".format(std_travel_time))
    # TO DO: display variance of travel time
    var_travel_time = df['Trip Duration'].var()
    print('\nVariance of time of travel...')
    print("Variance of time of travel:{} seconds".format(var_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nUser Types...')
    print(user_types)
    print('-'*60)

    # TO DO: Display counts of gender
    
    if city in ['Washington', 'washington'] :
       print("Gender stats")
       print("There is no gender data for ", city) 
       print('-'*60)
       print("Birth Year stats")
       print("There is no birth year data for ", city)
       
    else : 
        print('\nGender Types...')
        gender_types = df['Gender'].value_counts()
        print(gender_types)
        print('-'*60)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_date_of_birth = df['Birth Year'].min()
        most_recent_date_of_birth = df['Birth Year'].max()
        Popular_year_of_birth = df['Birth Year'].mode()[0]
        print("\nEarliest date of birth.....")
        print("Earliest date of birth:", earliest_date_of_birth)
        print("\nMost recent date of birth.....")
        print("Most recent date of birth:", most_recent_date_of_birth)
        print("\nMost common date of birth.....")
        print("Most common date of birth:",  Popular_year_of_birth)
        print("\nThis took %s seconds." % (time.time() - start_time))
        
    print('-'*120)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        count = 0
        df1 = load_data(city, month, day)
        while True:
           if count == 0:
                show_head = input('\nWould you like to see the first five lines of data? Enter yes or no\n')
           else:
                show_head = input('\nWould you like to see the next five lines of data? Enter yes or no\n')
           if show_head.lower() != 'yes':
                break
           else:
                count += 5
                print(df1.head(count))
                

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
