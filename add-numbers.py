import os

# Define the directory path
directory = "/home/daniel/Git/openwebui-models/static-import/25-Jan-25"

# Get a list of all Markdown files in the directory
markdown_files = [f for f in os.listdir(directory) if f.endswith('.md')]

# Sort the files to ensure they are processed in order
markdown_files.sort()

# Iterate over the files and rename them
for index, filename in enumerate(markdown_files, start=1):
    # Create the new filename with a three-digit identifier
    new_filename = f"{index:03d}-{filename}"
    
    # Get the full paths for the old and new filenames
    old_file_path = os.path.join(directory, filename)
    new_file_path = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(old_file_path, new_file_path)
    
    print(f"Renamed: {filename} -> {new_filename}")

print("All files have been renamed.")