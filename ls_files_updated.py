import os, time

_dir = os.getcwd()
files = (fle for rt, _, f in os.walk(_dir) for fle in f if (time.time() - os.stat(
    os.path.join(rt, fle)).st_mtime) < 300)

print(list(files))