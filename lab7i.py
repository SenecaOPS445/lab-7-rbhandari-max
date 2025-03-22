#!/usr/bin/env python3
# Student ID: rbhandari17@myseneca.ca

def function1():
    global schoolName  # Ensure this refers to the global variable
    schoolName = 'SICT'  # Modify global variable directly
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)

function1()

print('print() in main on schoolName:', schoolName)

function2()

print('print() in main on schoolName:', schoolName)
