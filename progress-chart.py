import os
import csv

# Define the root directory
root_directory = "/home/daniel/Git/openwebui-models/static-import/25-Jan-25"

# Define the output CSV file path
output_csv = os.path.join(root_directory, "file_list.csv")

# Initialize the list to hold the file data
file_data = []

# Walk through the directory and collect file names
for dirpath, dirnames, filenames in os.walk(root_directory):
    for filename in filenames:
        # Construct the full file path
        file_path = os.path.join(dirpath, filename)
        # Append the file name and empty columns to the list
        file_data.append([filename, "", "", ""])

# Write the data to the CSV file
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["File Name", "Instance", "Exported", "Ready to Share"])
    # Write the file data
    writer.writerows(file_data)

print(f"CSV file has been created at {output_csv}")