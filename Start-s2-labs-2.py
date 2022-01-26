# Author: IBN (AMDG) 1/12/2022

last_initials = ["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"] # Initials of people
rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]] # list of people by row

for row in rows: # for each list inside rows
        for i, v in enumerate(row): # enumerating the specific names of people
            row[i] = "{0} {1}.".format(v, last_initials[0]) # interpolating the name of the person with their initial into a string
            del last_initials[0] # deletes used initial so next person's initial falls in position 0
print(rows)
