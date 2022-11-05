from pathlib import Path
from datetime import datetime

path = Path("016-add-created-date-to-filenames/files")

for path in path.glob("**/*"):
    if path.is_file():
        created_date = datetime.fromtimestamp(path.stat().st_ctime)
        created_date_string = created_date.strftime("%Y-%m-%d-%H:%M:%S")
        new_filename = created_date_string + "-" + path.name
        new_filepath = path.with_name(new_filename)
        print(path)
        print(new_filepath)
        path.rename(new_filepath)
