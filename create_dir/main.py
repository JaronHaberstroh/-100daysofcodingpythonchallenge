import os
import sys

ROOT = "/home/jhspaz988/Documents/100daysofcodingpythonchallenge"
CHILD_LIST = ["projects", "playground"]

os.chdir(ROOT)


def create_dir(days):
    for day in days:
        dir_name = f"day{day}"
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            print("file exists")
        else:
            for child in CHILD_LIST:
                os.mkdir(os.path.join(dir_name, child))
            with open(f"{dir_name}/.gitignore", "w") as file:
                file.write(
                    "playground/config.py\n"
                    "playground/__pycache__\n"
                    "projects/config.py\n"
                    "projects/__pycache__")


create_dir(sys.argv[1:])
