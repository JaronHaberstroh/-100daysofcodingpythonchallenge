import os

CWD = "/home/jhspaz988/Documents/python/#100daysofcodingpythonchallenge"
CHILD_LIST = ["projects", "playground"]

os.chdir(CWD)


def create_dir(day):
    dir_name = f"day{day}"
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        print("file exists")
    else:
        for child in CHILD_LIST:
            os.mkdir(os.path.join(dir_name, child))


for day in range(1, 100 + 1):
    create_dir(day)
