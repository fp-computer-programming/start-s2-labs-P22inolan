# Author: IBN (AMDG) 1/25/2022
def smash(lst):
    blank = "" # creating blank string for words to be put in
    for x in lst: # for a word in the list:
        blank += str(x) + "" # adding the word at x with no space in the middle to the blank string
    return blank


print(smash(["apple", "banana", "orange", "grape"]))