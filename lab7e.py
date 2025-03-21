#!/usr/bin/env python3
# Student ID: rbhandari17@myseneca.ca

class Time:
    """Simple object type for time of the day.
    Data attributes: hour, minute, second
    Function attributes: __init__, __str__, __repr__,
                          time_to_sec, format_time,
                          change_time, sum_time
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        '''Return a string representation for the object self.'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        '''Return a string representation for the object self.'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Return time object (self) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the sum."""
        sec1 = self.time_to_sec()  # Convert self (current time) to seconds
        sec2 = t2.time_to_sec()  # Convert t2 to seconds
        total_seconds = sec1 + sec2  # Sum the seconds
        return sec_to_time(total_seconds)  # Convert total seconds back to time

    def change_time(self, seconds):
        """Change the time object by adding/subtracting seconds."""
        current_seconds = self.time_to_sec()  # Convert current time to seconds
        new_seconds = current_seconds + seconds  # Add/subtract seconds
        if new_seconds < 0:
            new_seconds = 86400 + new_seconds  # Wrap around if seconds are negative
        new_time = sec_to_time(new_seconds)  # Convert back to time object
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second
        return None

    def time_to_sec(self):
        """Convert a time object to a single integer representing the number of seconds from midnight"""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """Check for the validity of the time object attributes:
        24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    """Convert a given number of seconds to a time object in hour:minute:second format"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
