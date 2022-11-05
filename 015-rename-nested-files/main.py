from pathlib import Path

root_dir = Path("015-rename-nested-files")

file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        parts = path.parts[-3:]
        new_filename = f"{parts[0]}-{parts[1]}-{path.name}"
        new_filepath = path.with_name(new_filename)
        print(new_filepath)
        path.rename(new_filename)