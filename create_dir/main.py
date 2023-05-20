import os
import sys

CWD = "/home/jhspaz988/Documents/python/100daysofcodingpythonchallenge"
CHILD_LIST = ["projects", "playground"]

os.chdir(CWD)


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


create_dir(sys.argv[1:])
