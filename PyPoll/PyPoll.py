import os
import csv
path= "c:/Users/khinh/Documents/activity/pythondata/test/Assignment/Solved/Resources"
election_data = os.path.join(path,"election_data.csv")
Output_file = os.path.join(path, "election_analysis.txt")


#Set variable
total_votes = 0
candidate_options=[]
candidate_votes={}
winning_candidate = ""
winning_count = 0

# Open and read
with open(election_data) as election_data:
    csv_reader = csv.reader(election_data)
    header = next(csv_reader)

    for row in csv_reader:
        #Total vote count
        total_votes = total_votes + 1
        candidate_name = row[1] 

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #Candidate's count 
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(Output_file, "w") as txt_file:

    #Analysis Output 
    Output = (
        f"\nElection Results\n"
        f"-----------------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------------------------------------\n"
    )
        

    print(Output)

    # Export the results to text file
    txt_file.write(Output)

    # Winner Loop
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Vote Count
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Candidate's vote count and %
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)

        # Export the results to text file   
        txt_file.write(voter_output)

    # Winning Candidate
    winning_candidate_summary = (
        f"-----------------------------------\n"
        f"Winner :{winning_candidate}\n"
        f"-----------------------------------\n"

    )
    print(winning_candidate_summary)

    # Export the results to text file
    txt_file.write(winning_candidate_summary)











