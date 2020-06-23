"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)

    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Let's add all the distinct numbers from both the texts and calls files

Distinct_numbers = [] # Contains list of distinct numbers from calls and text

# This for loop iterates through all the numbers in the texts file and add distinct numbers to...
# the Distinct_numbers list.
for number1 in texts:
	if number1[0] not in Distinct_numbers:
		Distinct_numbers.append(number1[0])
	if number1[1] not in Distinct_numbers:
		Distinct_numbers.append(number1[1])


# This for loop iterates through all the numbers in the calls file and add distinct numbers to...
# the Distinct_numbers list.
for number2 in calls:
	if number2[0] not in Distinct_numbers:
		Distinct_numbers.append(number2[0])
	if number2[1] not in Distinct_numbers:
		Distinct_numbers.append(number2[1])

# Determine the total distinc numbers in the list
count  = len(Distinct_numbers)

print("There are {} different telephone numbers in the records.".format(count))

