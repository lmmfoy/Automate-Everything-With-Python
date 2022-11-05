from pathlib import Path
import zipfile

root_dir = Path("020-extract-zip-files")
destination_path = Path("020-extract-zip-files/files")

for path in root_dir.rglob("*.zip"):
    print(path)
    with zipfile.ZipFile(path, "r") as zf:
        # Putting the files in different folders - stem gets only first part of file name, without suffix
        final_path = destination_path / Path(path.stem)
        # Path is where files should be extracted
        zf.extractall(path=final_path)