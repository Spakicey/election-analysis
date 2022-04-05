# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates that received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add dependencies
import csv, os

def main():
  # Indirect path to load the file into variable file_to_load
  file_to_load = os.path.join("Resources", "election_results.csv")
  # Indirect path to create elecion_analysis.txt file in Analysis folder
  file_to_save = os.path.join("Analysis", "election_analysis.txt")

  # Open election results and read data
  with open(file_to_load) as election_data:
    # To Do: read and analyze data here
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    # Open election_analysis.txt and enable write
    with open(file_to_save, "w") as txt_file:
      txt_file.write("Counties in the Election\n")
      txt_file.write("------------------------\n")
      txt_file.write("Arapahoe\nDenver\nJefferson")



if __name__ == "__main__":
  main()
