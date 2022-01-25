# Author: IBN (AMDG) 1/25/2022
def smash(lst):
    blank = "" # creating blank string for words to be put in
    for x in lst:
        blank += str(x) + "" # adding the str of x with no space in the middle to the blank string
    return blank


print(smash(["apple", "banana", "orange", "grape"]))