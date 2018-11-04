#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:28:31 2018
Data taken from: https://data.cityofnewyork.us/City-Government/NYC-Jobs/kpav-sd4t/data
@author: sameertulshyan
"""
import pylab
import csv

filename = "NYC_Jobs_scrubbed.csv" # name of the input file

try: # try to open the file
    f = open(filename)
    input_file = csv.reader(f) # use the csv module to read the file
except FileNotFoundError: # file could not be found
    print("The input file could not be found. Please ensure that 'NYC_Jobs_scrubbed.csv' is \
          placed in the same folder as this program file") # let the user know that we failed to find the file
else:
    agencies = [] # create lists to store data from file
    min_salaries = []
    max_salaries = []
    # create a dictionary for data processing and counting occurrences
    agency_names = {"DEPT OF ENVIRONMENT PROTECTION":0,"NYC HOUSING AUTHORITY":0, "ADMIN FOR CHILDREN'S SVCS":0, "LAW DEPARTMENT":0, \
                    "DEPARTMENT OF TRANSPORTATION":0, "POLICE DEPARTMENT":0, "DEPT OF HEALTH/MENTAL HYGIENE":0} 
    
    # Request range of values from user and validate input
    while True: # get the user's desired minimum salary for processing
        user_minimum = input("What is your minimum salary requirement? $") 
        if not user_minimum.isnumeric(): # ensure that they enter a number
            print("You must enter a number for salary.")
        elif int(user_minimum) < 0: # ensure the number is positive
            print("You cannot have a negative salary.")
        else:
            user_minimum = float(user_minimum) # cast the input into an int for processing
            break # break out of the input validation loop and continue with the program
            
    while True: # get the user's desired maximum salary for processing
        user_maximum = input("What is your maximum salary requirement? $") 
        if not user_maximum.isnumeric(): # ensure that they enter a number
            print("You must enter a number for salary.")
        elif int(user_maximum) < user_minimum: # ensure the number is greater than min
            print("Your maximum must be larger than your minimum.")
        else:
            user_maximum = float(user_maximum) # cast the input into an int for processing
            break # break out of the input validation loop and continue with the program
    
    # iterate over the file
    for line in input_file:
        if line[0] == "Job ID": # skip the header row
            continue
        else:
            if (line[1] not in agency_names): # determine if the job is from our list of approved agencies
                continue # if not, skip this listing
            min_salary = float(line[7]) # get the min salary for this job
            max_salary = float(line[8]) # get the max salary for this job
            
            # if this job's salary falls inside the user-specified range
            if (user_minimum < min_salary and user_maximum > max_salary):
                agencies.append(line[1]) # get the agency
                agency_names[line[1]] += 1 # increment the count for this agency
                min_salaries.append(min_salary) # get the minimum salary
                max_salaries.append(max_salary) # get the maximum salary
    
    # plot the first figure
    pylab.figure(1)
    pylab.scatter(min_salaries, agencies) # scatter plot of minimum salaries by agency
    pylab.scatter(max_salaries, agencies) # scatter plot of maximum salaries- second record of data on same plot
    pylab.legend(['Minimum Salary', 'Maximum Salary'], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    pylab.xlabel("Salary (USD)")
    pylab.title("Minimum and Maximum Salary by Agency")
    
    # plot the second figure
    pylab.figure(2)
    # pie plot of percentage of jobs listed by each agency- use the dictionary we built earlier
    pylab.pie([float(v) for v in agency_names.values()], autopct = '%1.1f%%')
    pylab.legend(agency_names.keys(), bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    pylab.title("Share of Job Listings by Agency")
    
    # display both figures
    pylab.show()
    
