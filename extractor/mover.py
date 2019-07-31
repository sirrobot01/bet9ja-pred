import os
import shutil
from bs4 import BeautifulSoup



father_dir = os.path.dirname(os.getcwd())
dir_path = father_dir+'/downloads'
path_to_write = father_dir+'/segmented'

print('[+] Copying files......')
count = 0
try:
    for file in os.listdir(dir_path):
        if file.endswith('html'):
            filename = dir_path+'/'+file
            soup = BeautifulSoup(open(filename), 'html.parser')
            mon = soup.find('span', {'style': 'padding:10px 0;'})
            try:
                league = mon.text
            except:
                pass
            league = league[-4:]
            name_file = path_to_write + '/' + league+'/'+file
            os.makedirs(os.path.dirname(name_file), exist_ok=True)
            shutil.copy(dir_path+'/'+file, path_to_write+'/'+league+'/'+file)
            count = count+1
finally:
    print('[**] Total files copied: {}'.format(count))


