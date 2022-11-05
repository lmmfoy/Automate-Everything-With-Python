from pathlib import Path

root_dir = Path("018-create-empty-files/files")

for i in range(10, 14):
    filename = str(i) + ".txt"
    # Will create a path object
    filepath = root_dir / Path(filename)
    filepath.touch()