#!/usr/bin/env python3
# Student ID: rbhandari17@myseneca.ca

class Time:
    """Simple object type for time of the day.
    Data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def time_to_sec(time):
    """Convert a time object to a single integer representing the number of seconds from midnight"""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    """Convert a given number of seconds to a time object in hour:minute:second format"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    """Add two time objects and return the sum using time_to_sec and sec_to_time."""
    sec1 = time_to_sec(t1)  # Convert time1 to seconds
    sec2 = time_to_sec(t2)  # Convert time2 to seconds
    total_seconds = sec1 + sec2  # Sum the seconds
    return sec_to_time(total_seconds)  # Convert total seconds back to time

def change_time(time, seconds):
    """Change the time object by adding/subtracting seconds using time_to_sec and sec_to_time."""
    current_seconds = time_to_sec(time)  # Convert current time to seconds
    new_seconds = current_seconds + seconds  # Add/subtract the specified seconds
    if new_seconds < 0:
        new_seconds = 86400 + new_seconds  # Wrap around if seconds are negative
    return sec_to_time(new_seconds)  # Convert back to time object

def valid_time(t):
    """Check for the validity of the time object attributes:
    24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0"""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
