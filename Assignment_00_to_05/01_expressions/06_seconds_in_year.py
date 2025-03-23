'''
Problem Statement
Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

There are 5 seconds in a year!

You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.
'''

def main():
    # Define constants
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_YEAR = 365
    # Calculate seconds in a year
    seconds_in_year = DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
    # Print result
    print(f"There are {seconds_in_year} seconds in a year!")
    
if __name__ == '__main__':
    main()