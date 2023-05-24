import os

# Clear Terminal
os.system('clear')

# Find current working directory or CWD
CWD = os.getcwd()
print(CWD)

# Find absolute path of current working directory or CWD
ROOT_DIR = os.path.dirname(CWD)
print(ROOT_DIR)

# Find absolute path of file
ABS_PATH = os.path.abspath(CWD)
print(ABS_PATH)

# Find relative path of file
REL_PATH = os.path.relpath(CWD)
print(REL_PATH)

# Change current working directory or CWD
os.chdir(ABS_PATH)
print(os.getcwd())

# Change current working directory or CWD to the path of current running .py
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
