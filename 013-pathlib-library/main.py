from pathlib import Path

p1 = Path("013-pathlib-library/files/ex.txt")

if p1.exists():
    with open(p1, "r") as file:
        print(file.read())
    
else:
    with open(p1, "w") as file:
        file.write("Hello")

print(p1.name)
print(p1.stem)
print(p1.suffix)

# Iterdir: When the path points to a directory, yield path objects of the directory contents
p2 = Path("013-pathlib-library/files")
print(list(p2.iterdir()))

# Accessing files in a folder
root_dir = Path("013-pathlib-library/files")
file_paths = root_dir.iterdir()
print(file_paths)

# To see current working directory (it's always where main.py is located)
print(Path.cwd)

# Renaming files
for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    # If instead of above, did "new_filepath = Path(new_filename)", files would be moved to current working directory (a level above where we want them)
    print(new_filename)
    path.rename(new_filepath)