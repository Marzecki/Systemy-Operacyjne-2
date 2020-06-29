import sys
import os

list_path = sys.argv[1]
head, tail= os.path.split(list_path)
output = ''

if(not os.path.isfile(list_path)):
    print('Nie ma takiego pliku')
else:
    with open(list_path, 'r') as infile:
        for line in infile:
            output += line
            newpath = os.path.join(head, line.strip())
            file = open(newpath, 'r')
            output += file.read() + '\n'

    with open(list_path, 'w') as outfile:
        outfile.write(output)