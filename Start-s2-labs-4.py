# Author: IBN (AMDG) 1/26/2022

def double_every_other(lst):
    blank = [] # blank list for final numbers
    for i,v in enumerate(lst): # enumerate the list
        if i % 2 != 0: # if the index is odd:
            blank.append(lst[i] * 2) # append number * 2 to new list
        else:
            blank.append(lst[i]) # append even numbers to list normally
    return blank
    pass