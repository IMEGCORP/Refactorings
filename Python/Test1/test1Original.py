### Open Ended Problem

### You have a list of 11 quarterback people
### You want to know, if you choose one at random, how many tries it will take to get N in a row
### Author a Python script that chooses one quarterback from the list,
### and then compares it to the previous choice. If the choice is the same,
### that is 2 choices in a row. If the quarterback people are the same,
### print the current choice, the previous choice, the number of tries it
### took to geth there, and how many in a row that choice is.

### Expected output to the terminal:
"""
Kirk ::: Kirk ::: Try 1427 ::: 2 in a row
Tom ::: Tom ::: Try 1432 ::: 2 in a row
Tom ::: Tom ::: Try 1433 ::: 3 in a row
Tom ::: Tom ::: Try 1434 ::: 4 in a row
It took 1435 tries to get 4 people in a row!
"""

### quarterback people
people = ['Patrick', 'Jared', 'Tua', 'Russell', 'Tom', 'Trevor', 'Matthew', 'Aaron', 'Kirk', 'Geno', 'Justin']

### TASK: choose the same person "people_in_a_row_target" number of times in a row


### CONSTRAINTS: the list and all inputs should be the only manually entered data

### ----------------------

### Debug

### imports the randrange function from the random library
import random

### quarterback people
people = ['Patrick', 'Jared', 'Tua', 'Russell', 'Tom', 'Trevor', 'Matthew', 'Aaron', 'Kirk', 'Geno', 'Justin']

### TASK: choose the same person "people_in_a_row_target" number of times in a row
current_person == ''
previous_person = ''

### CONSTRAINTS: the list and all inputs should be the only manually entered data
number_of_people = len(people)
people_in_a_row_target = '4'
in_a_row = 1
tries = 1

while in_a_row <= 5:
    choice = randrange(number_of_people)
    current_person = people[number_choice]

    if current_person = Previous_person:
        in_a_row = in_a_row + 1
        print(current_person, ":::", Previous_person, "::: Try", tries, ":::", in_a_row, "in a row")
    else:
        in_a_row = 1

    tries = tries + 1
    Previous_person = people[number_choice]

print('It took ' + tries + ' tries to get '
people_in_a_row_target + " people in a row!")

### Debug Answer
