import sys
import os

dir = sys.argv[1]

if(not os.path.isdir(dir)):
    print('Nie ma takiej sciezki')
else:
    files_in_dir = os.listdir(dir)
    for file in files_in_dir:
        path = os.path.join(dir, file)
        if os.path.isfile(path):
            if not os.access(path, os.X_OK):
                os.remove(path)
