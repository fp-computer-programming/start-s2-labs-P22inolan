# Author: IBN (AMDG) 1/25/2022
def comes_after(st, l):
    result = [] # blank list for results
    l = l.lower() # makes everything lowercase
    try:
        for i in range(len(st)): # for letter in the range of the string
            if st[i].lower() == l and st[i+1].isalpha(): # if the letter at said index is the same as the input letter, and the index after is a letter:
                result.append(st[i+1]) # appends letter to blank list
    except:
        pass
    return "".join(result) # turns result into a string