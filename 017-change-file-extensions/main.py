from pathlib import Path
root_dir = Path("017-change-file-extensions/files")

# rglob is useful when have subfolders
for path in root_dir.rglob("*.txt"):
    if path.is_file():
        # with_suffix changes only the extension
        new_filepath = path.with_suffix(".csv")
        path.rename(new_filepath)