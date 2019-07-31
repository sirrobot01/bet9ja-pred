import os

father_dir = os.path.dirname(os.getcwd())

odd_path = father_dir+'/all_odds'
score_path = father_dir+'/real_scores'
data = open(father_dir+'/data'+'/'+'data.csv', 'a')

w = ''
for (folder1, sub_folder1, filename1),(folder2, sub_folder2, filename2)  in  zip(os.walk(score_path), os.walk(score_path)):
    if len(sub_folder1) or len(sub_folder2) > 2:
        for fl in sub_folder1:
            for files in os.listdir(odd_path+'/'+fl):
                foo1 = open(odd_path+'/'+fl+'/'+files)
                foo2 = open(score_path+'/'+fl+'/'+files)
                for line1, line2 in zip(foo1.readlines(), foo2.readlines()):
                    w += '\n'+line1.strip('\n')+','+line2.strip('\n')

data.write(w.strip('\n'))



