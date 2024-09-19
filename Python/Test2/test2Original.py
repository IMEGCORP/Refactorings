
### imports the randrange function from the random library
import random

### quarterback people
people = ['Patrick', 'Jared', 'Tua', 'Russell', 'Tom', 'Trevor', 'Matthew', 'Aaron', 'Kirk', 'Geno', 'Justin']

### TASK: choose the same person "people_in_a_row_target" number of times in a row
current_person = ''
previous_person = ''

### CONSTRAINTS: the list and all inputs should be the only manually entered data
number_of_people = len(people)
people_in_a_row_target = 4  ### change to int instead of string
in_a_row = 1
tries = 1

while in_a_row < people_in_a_row_target:  ### change to variable instead of verbatim number
    choice = random.randrange(number_of_people)  ### change randrange to random.randrange
    current_person = people[choice]  ### change number_choice choice

    if current_person == previous_person:  ### change previous_person to lowercase variable name
        in_a_row = in_a_row + 1
        print(current_person, ":::", previous_person, "::: Try", tries, ":::", in_a_row,
              "in a row")  ### change previous_person to lowercase variable name
    else:
        in_a_row = 1

    tries = tries + 1
    previous_person = people[
        choice]  ### change previous_person to lowercase variable name and change number_choice choice

print('It took ' + str(tries) + ' tries to get ' + str(
    people_in_a_row_target) + " people in a row!")  ### conversions and add a +