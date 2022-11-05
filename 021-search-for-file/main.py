from pathlib import Path

root_dir = Path("021-search-for-file")
search_term = "10"

for path in root_dir.rglob("*"):
    if search_term in path.stem:
        print(path.absolute())