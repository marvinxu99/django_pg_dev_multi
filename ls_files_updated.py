import os, time, stat
from pathlib import Path
import shutil


# Define look back time
#LOOKBACK_TIME = 60 * 15    # 15 mins
#LOOKBACK_TIME = 60 * 60    # 60 mins
LOOKBACK_TIME = 60 * 60 * 3    # 3 hours

# Define the subfolders to be excluded
DIRS_TO_EXCLUDE = ['venv', '.git']
# Define the folders to be excluded
FILES_TO_EXCLUDE = ['settings.py', 'test_temp.py']
# Define file extension/type to be included
TYPES_TO_INCLUDE = ['.py', '.txt', ".html", ".po", ".mo"]

PATH_SOURCE = os.getcwd()
#PATH_TARGET1 = Path(PATH_SOURCE).parent.joinpath('django_pg_heroku')x
PATH_TARGET1 = os.path.join(Path(PATH_SOURCE).parent, 'django_pg_heroku')
PATH_TARGET2 = os.path.join(Path(PATH_SOURCE).parent, '2_django_pg_winn')

SDIRS_TO_EXCLUDE = list(map(lambda dir: os.path.join(PATH_SOURCE, dir), DIRS_TO_EXCLUDE))

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHT_PURPLE = '\033[94m'
    PURPLE = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_info(info):
    print(bcolors.GREEN + info + bcolors.ENDC)

# files = (fle for rt, _, f in os.walk(_dir) for fle in f if (time.time() - os.stat(
#     os.path.join(rt, fle)).st_mtime) < LOOKBACK_TIME)

# Based on the solution from StackOverflow.com
# https://stackoverflow.com/questions/18394147/
def run_fast_scandir(dir, ext):    # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir() and (f.path not in SDIRS_TO_EXCLUDE):
            subfolders.append(f.path)
        if f.is_file():
            if f.name in FILES_TO_EXCLUDE:
                continue
            if (os.path.splitext(f.name)[1].lower() in ext and (time.time() - os.stat(f).st_mtime) < LOOKBACK_TIME):
                files.append(f.path)

    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)

    return subfolders, files


if __name__ == "__main__":
    source_files = []

    _, source_files = run_fast_scandir(PATH_SOURCE, TYPES_TO_INCLUDE)

    print_info("Files to be exported:")
    for i in range(len(source_files)):
        print(source_files[i])

    print_info("Enter (1) 'X' to abort, or (2) any other key to continue:")
    proceed_ind = input()
    if proceed_ind == "X" or proceed_ind == "x":
        print_info("Aborted. No changes made.")
    else:       
        # Copying to django_pg_heroku
        print_info("Copying to " + PATH_TARGET1 + '...')
        for i in range(len(source_files)):
            # print(source_files[i])
            f_target1 = source_files[i].replace(PATH_SOURCE, PATH_TARGET1, 1)
            print(f_target1)
            if os.path.exists(f_target1):
                try:
                    os.remove(f_target1)
                except PermissionError as exc:
                    os.chmod(f_target1, os.stat.S_IWUSR)
                    os.remove(f_target1)
            shutil.copy(source_files[i], f_target1)           

        # Copying to django_pg_winn
        print_info("Copying to " + PATH_TARGET2 + '...')
        for i in range(len(source_files)):
            f_target2 = source_files[i].replace(PATH_SOURCE, PATH_TARGET2, 1)
            print(f_target2)
            if os.path.exists(f_target2):
                try:
                    os.remove(f_target2)
                except PermissionError as exc:
                    os.chmod(f_target2, stat.S_IWUSR)
                    os.remove(f_target2)
            shutil.copy(source_files[i], f_target2)




