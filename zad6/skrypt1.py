import sys
import os

dir = sys.argv[1]

if(not os.path.isdir(dir)):
    print('Nie ma takiej sciezki')
else:
    files_in_dir = os.listdir(dir)
    old_files = [file for file in files_in_dir if file.endswith(".old")]
    for file in old_files:
        path = os.path.join(dir, file)
        if os.access(path, os.W_OK):
            os.remove(path)
    files_in_dir = os.listdir(dir)
    for file in files_in_dir:
        path = os.path.join(dir, file)
        if os.path.isfile(path):
            if os.access(path, os.W_OK):
                os.rename(path, path+'.old')

    