import os
import shutil


father_dir = os.path.dirname(os.getcwd())
path_to_read = father_dir+'/real_scores'

for (folder, sub_folder, filename) in os.walk(path_to_read):
    if not folder.endswith('real_scores'):
        for file in os.listdir(folder):
            reader = open(folder+'/'+file, 'r')
            i = 0
            for i, item in enumerate(reader.readlines()):
                print(item)
                i += 1
                if i > 9:
                    break

