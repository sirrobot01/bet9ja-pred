import os
import shutil
foo = open('03.csv', 'r')

father_dir = os.path.dirname(os.getcwd())
path = father_dir+'/scores'

w = ''
j = 'ab'
for i, lines in enumerate(foo):
    w += lines
    while w.count('\n') == 10:
        print(w)







