from pathlib import Path

root_dir = Path("014-rename-files-based-on-folder/files")

"""
We can do this:

file_paths = root_dir.iterdir()

for path in file_paths:
    for filepath in path.iterdir():
        print(filepath)

But instead:
"""

# Telling it to go into the folders - it will go down into folders, no matter how deep
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        # To see which folder file is in - -2 b/c it returns a tuple where folder is second to last element (filename is last element)
        parent_folder = path.parts[-2]
        new_filename = parent_folder + "-" + path.name
        # Creating new path object with our new name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filename)