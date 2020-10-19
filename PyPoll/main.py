import os
import csv

#prep the data file and load it into a list of tuples
poll_path = os.path.join("resources","election_data.csv")
poll_data = {}

with open(poll_path) as poll_file:
    poll_reader = csv.reader(poll_file, delimiter = ",")
    #discard header
    next(poll_reader)

    for row in poll_reader:
        if row[2] in poll_data:
            poll_data[row[2]] += 1
        else:
            poll_data[row[2]] = 1

print(sum(poll_data.values()))    
print(poll_data)