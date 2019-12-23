#MODIFY CSV
#SMALL SCRIPT TO CREATE A CSV FILE BASED ON MY BACK STATEMENT FORMATTING
#HOW IT WORKS
#   When running, it will ask for a save location, then will wait, line by line,
#   for a statement based on another statement format, and convert it to the csv file format

import numpy, os, csv
import tkinter as tk
from tkinter import filedialog

script_dir = os.path.dirname(__file__)

root = tk.Tk()
root.withdraw()
filename = filedialog.asksaveasfilename(initialdir = script_dir, title = "Select File Location")
root.quit()
root.destroy()

csv_header = 'Account Number,Post Date,Check,Description,Debit,Credit,Status\n'
account_number = '"******4582"' #dummy acct #
date = ''
check = ''
description = ''
debit = ''
credit = ''
status = 'Posted' #Specific to my back CSV formatting

#open file as w
with open(filename, 'w+') as csv_file:
    csv_file.write(csv_header)
    while(1):
        line = input('entry: ')

        if line == 'break_all': #exit command
            break

        else:
            sep_lin = line.split(' ') #split input by spaces
            date = sep_lin[0] + '/2019' #date will be first element, add year to it
            temp = sep_lin[-1] #retrieve the amount (unsure if credit or debit)

            if float(temp) < 0: #Negative on my credit card indicated a credit
                credit = sep_lin[-1]
            elif float(temp) > 0: #Positive on my credit card indicated a debit
                debit = sep_lin[-1]

            description += '"' #wrap in ""
            for i in sep_lin[1:-1]: #go through input except for first (date) and last (amount) elements
                description += str(i) + ' '
            description += '"' #wrap in ""

            csv_line = "{},{},{},{},{},{},{}\n".format(account_number, date, check, description, debit, credit, status) #use header
            print('adding: {}\n\n'.format(csv_line))
            csv_file.write(csv_line)

            #reset variable
            date = ''
            description = ''
            debit = ''
            credit = ''
