from pathlib import Path

root_dir = Path("022-destroy-files-forever/files")

for path in root_dir.glob("*.csv"):
    with open(path, "wb") as file:
        # Produces empty binary file
        file.write(b"")
    # File deleted
    path.unlink()