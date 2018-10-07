#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 17:17:04 2018
Data taken from: https://data.cityofnewyork.us/City-Government/NYC-Jobs/kpav-sd4t/data
@author: sameertulshyan
This program allows the user to extract a list of government jobs in NYC that meet their criteria for salary/work-type/payment schedule etc. 
It also cleans the datafile.
"""
import csv
filename = "NYC_Jobs.csv" # name of the input file

try: # try to open the file
    f = open(filename)
    input_file = csv.reader(f) # use the csv module to read the file
except FileNotFoundError: # file could not be found
    print("The input file could not be found. Please ensure that 'NYC_Jobs.csv' is \
          placed in the same folder as this program file") # let the user know that we failed to find the file
else:
    output_file = open("NYC_Jobs_scrubbed.csv", "w") # open an output file in write mode
    output_writer = csv.writer(output_file, delimiter=",") # use the csv module to write to the file
    
    while True: # ask the user whether they want to include the header
        header_required = input("Do you want to include a header row? (Y/N) ")
        if header_required.lower() not in ('y','n'): # validate their input
            print("\nPlease enter a valid response (Y/N)") # let them know their response was invalid and continue to ask them
        else: # if the user has entered a valid response
            break # break out of the input validation loop and continue with the program
    
    while True: # ask the user whether they would like to be paid hourly or annually or daily
        payment_schedule = input("Would you like to be paid on an Hourly, Daily or Annual basis? ")
        if payment_schedule not in ['Hourly','Annual','Daily']: # validate their input
            print("\nPlease enter a valid response (Hourly/Annual/Daily)") # let them know their response was invalid and continue to ask them
        else: # if the user has entered a valid response
            break # break out of the input validation loop and continue with the program
    
    while True: # get the user's desired minimum salary for processing
        user_minimum = input("What is your minimum salary requirement? $") 
        if not user_minimum.isnumeric(): # ensure that they enter a number
            print("You must enter a number for salary.")
        elif int(user_minimum) < 0: # ensure the number is positive
            print("You cannot have a negative salary.")
        else:
            user_minimum = int(user_minimum) # cast the input into an int for processing
            break # break out of the input validation loop and continue with the program
            
    while True: # ask the user whether they are interested in working full or part-time
        work_type = input("Do you want to work (F)ull or (P)art time? (F/P) ")
        if work_type not in ('F','P'): # validate their input
            print("\nPlease enter a valid response (F/P)") # let them know their response was invalid and continue to ask them
        else: # if the user has entered a valid response
            break # break out of the input validation loop and continue with the program
    
    lines_written = 0 # simple counter to keep track of how many entries are produced
    for line in input_file:
        
        # handle the line containing the header
        if line[0] == "Job ID":
            if header_required.lower() == "n":
                continue
            else:
                # get rid of unnecessary columns
                line.pop(6) 
                line.pop(6)
                line.pop(7)
                line.pop(9)
                for i in range(4):
                    line.pop(-1)
                output_writer.writerow(line) # write the header to the output file
                continue
        
        # exclude jobs that have a different payment schedule
        if line[12] != payment_schedule:
            continue
        
        # get the minimum salary for this job
        minimum_salary = float(line[10])
        
        # if the salary is less than the user's desired salary, we exclude it
        if minimum_salary < user_minimum:
            continue
        
        # if the work-type does not match the user's desired work type, we exclude it
        if line[9] != work_type:
            continue
        
        # get rid of unnecessary columns
        line.pop(6) 
        line.pop(6)
        line.pop(7)
        line.pop(9)
        for i in range(4):
            line.pop(-1)
        
        # since this line meets our criteria, write it to the output file
        output_writer.writerow(line)
        
        # increment the counter 
        lines_written += 1
        
    # close the input and output files
    f.close()
    output_file.close()
    
    # print the number of lines written to the console
    print(str(lines_written) + " lines written")
    
    
