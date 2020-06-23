"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from collections import defaultdict
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

spent_time = defaultdict(int)

for call in calls:

	spent_time[call[0]] += int(call[3])
	spent_time[call[1]] += int(call[3]) 

longest_time_spent = max(spent_time.values())


for tel_num, time in spent_time.items():
	if time == longest_time_spent:
		print("{} spent the longest time, {} seconds, on the phone during September 2016".format(tel_num,time))