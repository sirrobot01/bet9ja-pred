import os

father_dir = os.path.dirname(os.getcwd())
dir = father_dir+'/pre_data'
old_data = open(father_dir+'/data/data.csv','a')

try:
    for file in os.listdir(dir):
        with open(dir+'/'+file, 'r') as f:
            for line in f.readlines():
                old_data.write(line)
finally:
    for file in os.listdir(dir):
        os.remove(dir+'/'+file)


