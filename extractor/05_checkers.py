import os

father_dir = os.path.dirname(os.getcwd())

odd_path = father_dir+'/all_odds'
score_path = father_dir+'/real_scores'


for (folder2, sub_folder2, filename2) in  os.walk(score_path):
    if not folder2.endswith('scores'):
        for files in os.listdir(folder2):
            if '\n' in files:
                os.rename(folder2+'/'+files, folder2+'/'+files.replace('\n',''))
for (folder2, sub_folder2, filename2) in  os.walk(odd_path):
    if not folder2.endswith('odds'):
        for files in os.listdir(folder2):
            if files.startswith('0'):
                os.rename(folder2+'/'+files, folder2+'/'+files.replace('0',''))

for (folder, sub_folder, filename), (folder2, sub_folder2, filename2) in zip(os.walk(odd_path), os.walk(score_path)):
    if len(sub_folder) or len(sub_folder2) > 2:
        for folders, folders2 in zip(sub_folder, sub_folder2):
            if folders not in sub_folder2:
                for file in os.listdir(score_path + '/' + folders2):
                    os.remove(score_path + '/' + folders2 + '/' + file)
                os.removedirs(score_path + '/' + folders2)
            if folders2 not in sub_folder:
                for file in os.listdir(score_path + '/' + folders2):
                    os.remove(score_path + '/' + folders2+'/'+file)
                os.removedirs(score_path + '/' + folders2)

for (folder, sub_folder, filename), (folder2, sub_folder2, filename2) in zip(os.walk(odd_path),
                                                                                 os.walk(score_path)):
    if len(sub_folder) or len(sub_folder2) > 2:
        for fl in sub_folder:
            for files in os.listdir(score_path+'/'+fl):
                if files not in os.listdir(odd_path+'/'+fl):
                    os.remove(score_path+'/'+fl+'/'+files)
            for files in os.listdir(odd_path+'/'+fl):
                if files not in os.listdir(score_path+'/'+fl):
                    os.remove(odd_path+'/'+fl+'/'+files)



