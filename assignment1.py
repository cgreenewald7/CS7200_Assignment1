import pandas as pd 

# open the input file 
input_data = []
with open('./Tests/Input0.txt', 'r') as input_file:
    n_persons = int(input_file.readline().strip())
    for i, row in enumerate(input_file):
        input_data.append(row.strip().split())

print("Number of persons of each gender: ", n_persons)

# make an array of men
men = []
for persons in input_data[0:n_persons]:
    men.append(persons[0])
print("Men: ", men)

# make an array of women
women = []
for persons in input_data[n_persons:n_persons+n_persons]:
    women.append(persons[0])
print("Women: ", women)

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

print(men_perfered)

# start everyone off as single
single_man = {man: True for man in men}
single_women = {woman: True for woman in women}


# list of everyone currently engaged 
couples_engaged = {}

# track the proposals that have already happened so that there are not repeats 
proposals_occured = {man: [] for man in men}

def person_is_single(test_person):
    return test_person not in couples_engaged.values() and test_person not in couples_engaged.keys()

def person_is_engaged(man, woman):
    couples_engaged[woman] = man

# count how many engagements there are 

num_engagements = 0
# Pseudo code from the textbook 
# Initially all m in M and w in W are free
# While there is a man m who is free and hasnt proposed to every woman
while any(single_man.values()):
    for man in men:
        
        # Choose such a man m 
        if single_man[man]:
            
            # Let w be the highest-ranked woman in ms preference list to whom m has not yet proposed 
            for woman in men_perfered[man]:
                if woman in proposals_occured[man]:
                    continue
                proposals_occured[man].append(woman)

                # If w is free than
                if person_is_single(woman):
                    # (m,w) become engaged
                    person_is_engaged(man, woman)
                    num_engagements += 1
                    single_man[man] = False
                    single_women[woman] = False
                    print(f"{woman} is free, now engaged to {man}")
                    break
                
                # Else w is currently engaged to m'
                else:
                    current_man = couples_engaged[woman]
                    print(f"{woman} is engaged to {current_man}, comparing {man} with {current_man}")
                    
                    # If w prefers m' to m then
                    if women_perfered[woman].index(man) > women_perfered[woman].index(current_man):
                        # m remains free
                        single_man[man] = True
                        print(f"{woman} prefers {current_man} over {man}, {man} remains single")
                        break  
                    
                    # Else w prefers m to m'
                    else:
                        # (m,w) become engaged
                        person_is_engaged(man, woman)
                        num_engagements += 1
                        # m' becomes free
                        single_man[current_man] = True
                        single_man[man] = False
                        single_women[woman] = False
                        print(f"{woman} prefers {man} over {current_man}, switching partners")
                        break                     

# return the set S of engaged pairs 
print("The engaged couples are: ", couples_engaged)

# print the number of engagements 
print("The number of engagements was: ", num_engagements)

# write engagements to the output file 
output_file = open(r"./Tests/Output0.txt", "w")
for woman, man in couples_engaged.items():
    output_file.write(man + ' ' + woman + '\n')
output_file.write(str(num_engagements))
output_file.close()
