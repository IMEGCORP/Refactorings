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