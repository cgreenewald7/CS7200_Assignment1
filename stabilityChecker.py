# Assignment completed exclusively by: Calvin Greenewald
# Email: greenewald.6@wright.edu

# check if the engaged pairs are a stable matching or not 
import pandas as pd 
import sys

# get the input and output files
if len(sys.argv) > 2:
    input_file = sys.argv[1]
    outputToBeVerified = sys.argv[2]
else:
    input_file = "Input.txt"
    outputToBeVerified = "Output.txt"

# input file
input_data = []
with open(input_file, 'r') as file:
    n_persons = int(file.readline().strip())
    for i, row in enumerate(file):
        input_data.append(row.strip().split())

# get a list of the perfered list 
# the following code to aquire the preferences is taken from my code in assignment1.py
# make a group of each persons preferences
men_perfered = {}
for persons in input_data[0:n_persons]:
    each_man = persons[0]
    prefered_women = persons[1:]
    men_perfered[each_man] = prefered_women

women_perfered = {}
for persons in input_data[n_persons:n_persons+n_persons]:
    each_woman = persons[0]
    prefered_man = persons[1:]
    women_perfered[each_woman] = prefered_man
# end off my code copied from assignment1.py

# outputToBeVerified file 
engaged_couples_input = []
with open(outputToBeVerified, 'r') as otbv:
    rows = otbv.readlines()
    # check if there is an integer at the bottom of the file 
    # the output to be verified files dont require the integer at the bottom per the assignment 
    if rows[-1].strip().isdigit():
        rows = rows[:-1]

    for row in rows:
        engaged_couples_input.append(row.strip().split())

# print(engaged_couples_input)

# Check if a stable match 
def stabilityChecker(men_prefered, women_perfered):
    # matchings from male and female perspective for access 
    couples_male = {man: woman for man, woman in engaged_couples_input}  
    couples_female = {woman: man for man, woman in engaged_couples_input} 

    # for each couple
    for current_man, current_woman in engaged_couples_input:
        # check the women he perfers over his current match 
        for new_woman in men_prefered[current_man]:
            # if his current match is the highest on his preference list then break 
            if new_woman == current_woman:
                break 
            
            # check the womans preferences 
            new_woman_partner = couples_female[new_woman]

            # check if the woman also perfers the man over her current match 
            if women_perfered[new_woman].index(current_man) < women_perfered[new_woman].index(new_woman_partner):
                # matching is unstable
                return False  
    
    # matching is stable
    return True

out_file = open(r"Verified.txt", "w")
if stabilityChecker(men_perfered, women_perfered):
    # write stability to file 
    out_file.write("Stable")
    # print("The matching is stable.")
else:
    out_file.write("Unstable")
    # print("The matching is unstable.")

out_file.close()

