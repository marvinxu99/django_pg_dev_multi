import os, time
from pathlib import Path

# Define look back time
#LOOKBACK_TIME = 300    # 5 mins
LOOKBACK_TIME = 3600    # 60 mins

# Define the folders to be excluded
DIRS_TO_EXCLUDE = ['venv', '.git']

PATH_SOURCE = os.getcwd()
PATH_TARGET1 = Path(PATH_SOURCE).parent.joinpath('django_pg_heroku')
PATH_TARGET2 = os.path.join(Path(PATH_SOURCE).parent, 'django_pg_winn')


sdirs_to_exclude = list(map(lambda dir: os.path.join(PATH_SOURCE, dir), DIRS_TO_EXCLUDE))



source_files = []

# files = (fle for rt, _, f in os.walk(_dir) for fle in f if (time.time() - os.stat(
#     os.path.join(rt, fle)).st_mtime) < LOOKBACK_TIME)

# Based on the solution from StackOverflow.com
# https://stackoverflow.com/questions/18394147/
def run_fast_scandir(dir, ext):    # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir() and (f.path not in sdirs_to_exclude):
            subfolders.append(f.path)
        if f.is_file():
            #if os.path.splitext(f.name)[1].lower() in ext:
            if (time.time() - os.stat(f).st_mtime) < LOOKBACK_TIME:
                files.append(f.path)

    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)

    return subfolders, files

source_folders, source_files = run_fast_scandir(PATH_SOURCE, [".txt"])

print(list(source_files))
# print(sdirs_to_exclude)
# print(PATH_TARGET1)
# print(PATH_TARGET2)


