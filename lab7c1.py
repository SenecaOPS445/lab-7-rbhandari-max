#!/usr/bin/env python3
# Student ID: rbhandari17@myseneca.ca

from lab7c import *

t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)
td = Time(0, 50, 0)

# Testing sum_times and change_time
tsum1 = sum_times(t1, td)
tsum2 = sum_times(t2, td)
t3 = change_time(t3, 1800)

ft = format_time
print(ft(t1), '+', ft(td), '-->', ft(tsum1))
print(ft(t2), '+', ft(td), '-->', ft(tsum2))
print('09:50:00 + 1800 sec', '-->', ft(t3))
