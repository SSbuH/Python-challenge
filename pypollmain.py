import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = os.path.join('..', 'Resources', 'election_data.csv')


# Declaring variables for analysis
poll_info={}
total_votes = 0
with open(pypoll_csv, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)

    for row in csvread:
        total_votes += 1
        if row[2] in poll_info.keys():
            poll_data[row[2]]= poll_info[row[2]] + 1
            else:
                poll_info[row[2]] = 1

candidates = []
total_num_votes = []
# Calculating the total number of votes each candidate won
for key, value in poll_info.items():
    candidates.append(key)
    total_num_votes.append(value)

# Calculating the percentage of votes per candidate
percentage_votes = []
for n in total_num_votes:
    percentage_votes.append(round(n/total_votes * 100, 1))

# Finding winner based on popular votes
cleanlist_data = list(zip(candidates, total_num_votes, percentage_votes))

popwin_list = []
for name in cleanlist_data:
    if max(total_num_votes) == name[1]:
        popwin_list.append(name[0])
winner = popwin_list[0]

# Print results of poll analysis
print ("Election results:")
print(total_votes)
print(candidates)
print(percentage_votes)
print(total_num_votes)
print(winner)

# Writing output files
PyPoll = open("output.txt", "w+")
PyPoll.write("Election Results") 
PyPoll.write('\n' + str(candidates))
PyPoll.write('\n' + str(percentage_votes))
PyPoll.write('\n' + str(total_num_votes))
PyPoll.write('\n' + "Winner:" + winner)

