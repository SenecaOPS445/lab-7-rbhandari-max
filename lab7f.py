#!/usr/bin/env python3
# Student ID: rbhandari17@myseneca.ca
class Time:
    """A simple time object with attributes: hour, minute, second."""
    
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for the Time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        """Return the time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __str__(self):
        """Return a string representation of the time object in HH:MM:SS format"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a string representation with dots instead of colons"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the result as a new Time object"""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def __add__(self, t2):
        """Overload the + operator to add two time objects."""
        return self.sum_times(t2)

    def change_time(self, seconds):
        """Adjust the time by adding/subtracting seconds"""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second
        return None

    def time_to_sec(self):
        """Convert a time object to a total number of seconds since midnight"""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """Check if the time object's hour, minute, and second are valid"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    """Convert a number of seconds into a time object (hour, minute, second)"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

