import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# List all files and directories in the current directory
files_and_dirs = os.listdir(current_directory)
print(f"Files and Directories: {files_and_dirs}")

# Create a new directory
new_dir = "example_dir"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created.")
else:
    print(f"Directory '{new_dir}' already exists.")

# Rename the directory
renamed_dir = "renamed_example_dir"
if os.path.exists(new_dir):
    os.rename(new_dir, renamed_dir)
    print(f"Directory renamed to '{renamed_dir}'.")

# Remove the directory
if os.path.exists(renamed_dir):
    os.rmdir(renamed_dir)
    print(f"Directory '{renamed_dir}' removed.")