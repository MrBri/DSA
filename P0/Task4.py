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

tele = set()

for c in calls:
    if c[0][:3] == '140':
        tele.add(c[0]) 

for c in calls:
    if c[1][:3] == '140':
        tele.remove(c)

for t in texts:
    if t[0][:3] == '140':
        tele.remove(t[0])
    if t[1][:3] == '140':
        tele.remove(t[1])

print(f'These numbers could be telemarketers: ')
for t in sorted(tele):
    print(t)

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

