from pathlib import Path
import zipfile

root_dir = Path("019-create-archive-from-files/files")
archive_path = root_dir / Path("archive.zip")

with zipfile.ZipFile(archive_path, "w") as zf:
    for path in root_dir.rglob("*.txt"):
        zf.write(path)

        # Delete the path (remove the file)
        path.unlink()