import csv

#variable for file , open and read
with open("Resources/election_data.csv") as election_file:
    csv_reader = csv.DictReader(election_file)

    #create empty lists
    candidate_votes = []
    candidate_list = []
    
    #create canditate votes number, total and percentage variables
    candidate1_votes = 0
    candidate2_votes = 0
    candidate3_votes = 0
    total_votes = 0 
    candidate1_percentage = float
    candidate2_percentage = float
    candidate3_percentage = float
    
    #populate candidate_votes list with Candidate column of csv as it's the only column we need for this analysis
    for col in csv_reader:
        candidate_votes.append(col['Candidate'])

    #populate candidate_list with unique candidate values
    for x in candidate_votes:
        # check if exists in candidate_list or not
        if x not in candidate_list:
            candidate_list.append(x)
  
    #count and store number of votes for each candidates
    for items in candidate_votes:
        if items == "Charles Casper Stockham":
            candidate1_votes = candidate1_votes + 1
        elif items == "Diana DeGette":
            candidate2_votes = candidate2_votes + 1
        elif items == "Raymon Anthony Doane":
            candidate3_votes = candidate3_votes + 1
    
    #add for total of votes
    total_votes = candidate1_votes + candidate2_votes + candidate3_votes

    #calculate and store vote percentage values
    candidate1_percentage = (candidate1_votes/total_votes)*100
    candidate2_percentage = (candidate2_votes/total_votes)*100
    candidate3_percentage = (candidate3_votes/total_votes)*100

    #create variable to hold winner name
    winner = ""

    #determine winner and store in variable    
    voteTotals=[]
    voteTotals.append(candidate1_votes)
    voteTotals.append(candidate2_votes)
    voteTotals.append(candidate3_votes)
    winner_index = voteTotals.index(max(voteTotals))
    winner = candidate_list[winner_index]
    
#output block------------------------------------------------------


#output "Election Results"
print("Election Results \n" )
#output "-------------------------"
print("----------------------------\n")
#output "Total Votes: number_votesCast "
#output "-------------------------"
print(f"Total Votes: {total_votes}\n")
print("----------------------------\n")
#output "name: percent (number) "
#online exmaple output:
#Charles Casper Stockham: 23.049% (85213)
print(f"{candidate_list[0]}: {candidate1_percentage:.3f}% ({candidate1_votes})")
#output "name: percent (number) "
#online exmaple output:
#Diana DeGette: 73.812% (272892)
print(f"{candidate_list[1]}: {candidate2_percentage:.3f}% ({candidate2_votes})")
#output "name: percent (number) "
#online exmaple output: Raymon Anthony Doane: 3.139% (11606)
print(f"{candidate_list[2]}: {candidate3_percentage:.3f}% ({candidate3_votes})\n")
#output"-------------------------
print("----------------------------\n")
#output "Winner: "
print(f"Winner: {winner}\n")
#output"-------------------------
print("----------------------------")

#export text file with above results
with open("analysis/pyPollAnalysis.txt", "w") as analysis_file:
    analysis_file.write("Election Results \n------------------------- \nTotal Votes: "+ str(total_votes) + "\n------------------------- \n" )
    analysis_file.write(f"{candidate_list[0]}: {candidate1_percentage:.3f}% ({candidate1_votes})\n{candidate_list[1]}: {candidate2_percentage:.3f}% ({candidate2_votes})\n{candidate_list[2]}: {candidate3_percentage:.3f}% ({candidate3_votes})\n----------------------------\nWinner: {winner}\n----------------------------")

