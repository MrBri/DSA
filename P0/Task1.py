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

import itertools
unique_numbers = set()

for (t, c) in itertools.zip_longest(texts, calls):
    unique_numbers.update([t[0], t[1]])
    if c != None:
        unique_numbers.update([c[0], c[1]])

print(f'There are {len(unique_numbers)} different telephone numbers in the records.')
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
