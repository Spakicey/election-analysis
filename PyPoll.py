# Add dependencies
import csv, os

def main():
  # Indirect path to load the file into variable file_to_load
  file_to_load = os.path.join("Resources", "election_results.csv")
  # Indirect path to create elecion_analysis.txt file in Analysis folder
  file_to_save = os.path.join("Analysis", "election_analysis.txt")

  # Initialize a total vote counter
  total_votes = 0
  # Initialize candidate list
  candidate_options = []
  # Initialize candidate dict
  candidate_votes = {}
  # Winning candidate and winning count tracker
  winning_candidate = ""
  winning_count = 0
  winning_percentage = 0

  # Open election results and read data
  with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Loop through each row in the election data
    for row in file_reader:
      # Add to total vote count
      total_votes += 1

      # Get candidate name
      candidate_name = row[2]

      # If candidate name does not exist in candidate list:
      if candidate_name not in candidate_options:
        # Add candidate name
        candidate_options.append(candidate_name)
        # Track candidate vote count
        candidate_votes[candidate_name] = 0

      # Add a vote count to candidate's count
      candidate_votes[candidate_name] += 1

    with open(file_to_save, "w") as txt_file:
      election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
      )
      print(election_results, end="")
      txt_file.write(election_results)

      for candidate_name in candidate_votes:
        # Get votes for individual candidate
        votes = candidate_votes[candidate_name]
        # Create percentage of votes
        vote_percentage = (float(votes) / float(total_votes)) * 100
        # Print info
        # print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
          # If True set winning_count = votes
          # and winning_percentage = vote_percentage
          winning_count = votes
          winning_percentage = vote_percentage
          # Set winning_candidate = candidate_name
          winning_candidate = candidate_name

        # Print candidate info for each candidate
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

      # Print formatted info for winning candidate
      winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n"
      )
      print(winning_candidate_summary)
      txt_file.write(winning_candidate_summary)

if __name__ == "__main__":
  main()
