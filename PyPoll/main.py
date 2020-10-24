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

total_votes = sum(poll_data.values())

print("Election Results")
print("---------------------------------")
print("Total Votes: {}".format(total_votes))
print("---------------------------------")
for candidate in poll_data:
    print("{}: {:.3f}% ({})".format(candidate, 100*(poll_data[candidate]/total_votes), poll_data[candidate]))
print("---------------------------------")
print("Winner: {}".format(max(poll_data, key=poll_data.get)))
print("---------------------------------")


output_path = os.path.join("analysis", "output.txt")
f = open(output_path, "w")

f.write("Election Results\n")
f.write("---------------------------------\n")
f.write("Total Votes: {}\n".format(total_votes))
f.write("---------------------------------\n")
for candidate in poll_data:
    f.write("{}: {:.3f}% ({})\n".format(candidate, 100*(poll_data[candidate]/total_votes), poll_data[candidate]))
f.write("---------------------------------\n")
f.write("Winner: {}\n".format(max(poll_data, key=poll_data.get)))
f.write("---------------------------------\n")

f.close()