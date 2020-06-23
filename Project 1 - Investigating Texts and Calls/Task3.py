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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


''' Solution for PART A '''

Bangalore_area_code = set()  # Using the ensures that there are no duplications

for number in calls:
	if number[0][:5] == "(080)" :
		if number[1][1] == "0" :
			for x, y in enumerate(number[1]):
				if y == ")" :
					Bangalore_area_code.add(number[1][:x+1])


		elif " " in number[1]:
			Bangalore_area_code.add(number[1][:4])

		elif number[1][:3] == "140" :
			Bangalore_area_code.add("140")

sorted_list = sorted(list(Bangalore_area_code))


''' Let's print the codes now'''

print("The numbers called by people in Bangalore have codes:")
for sort_code in sorted_list:
	print(sort_code)

# Solution for Part B

calls_in_bangalore = 0
calls_from_bang_to_elsehere = 0

for number in calls:
	if number[0][:5] == "(080)" :
		if number[1][:5] == "(080)" :
			calls_in_bangalore += 1
			calls_from_bang_to_elsehere += 1

		else:
			calls_from_bang_to_elsehere += 1

	# Let's calculate the Percentage
percentage = (calls_in_bangalore/calls_from_bang_to_elsehere) * 100

# Print the message

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format("%.2f" % percentage))
