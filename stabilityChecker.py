# Assignment completed exclusively by: Calvin Greenewald
# Email: greenewald.6@wright.edu

# check if the engaged pairs are a stable matching or not 
import pandas as pd 
from assignment1 import men_perfered, women_perfered


# open the input file 
engaged_couples_input = []
with open('./Tests/Output1.txt', 'r') as input_file:
    rows = input_file.readlines()
    for row in rows[:-1]:
        engaged_couples_input.append(row.strip().split())

print(engaged_couples_input)

def stability(men_prefered, women_perfered):
    couples_male = {man: woman for man, woman in engaged_couples_input}  
    couples_female = {woman: man for man, woman in engaged_couples_input} 

    for current_man, current_woman in engaged_couples_input:
        for new_woman in men_prefered[current_man]:
            if new_woman == current_woman:
                break 

            new_woman_partner = couples_female[new_woman]

            if women_perfered[new_woman].index(current_man) < women_perfered[new_woman].index(new_woman_partner):
                return False  
    
    return True

output_file = open(r"Verified.txt", "w")
if stability(men_perfered, women_perfered):
    # write stability to file 
    output_file.write("Stable")
    print("The matching is stable.")
else:
    output_file.write("Unstable")
    print("The matching is unstable.")

output_file.close()