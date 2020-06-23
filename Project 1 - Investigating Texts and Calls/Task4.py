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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

''' Task 4 Soluton'''

outgoing_calls = set()
receieved_calls = set()
sent_texts = set()
received_texts = set()

for number in calls:
	outgoing_calls.add(number[0])
	receieved_calls.add(number[1])

for text in texts:
	sent_texts.add(text[0])
	received_texts.add(text[1])

possible_telemarkers = sorted(list(outgoing_calls - (receieved_calls | sent_texts | received_texts)))
print("These numbers could be telemarketers: ")
for telemarketers in possible_telemarkers:
	print(telemarketers)