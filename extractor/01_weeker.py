from bs4 import BeautifulSoup
import os
import shutil


father_dir = os.path.dirname(os.getcwd())
path = father_dir+'/downloads'

print('[++] Scanning through files.....')
count = 0
try:
    for file in os.listdir(path):

        if file.endswith('html'):
            w = ''
            count = 0
            soup = BeautifulSoup(open(path + '/' + file), 'html.parser')
            week = soup.find('span', {'id': 'leagueWeekNumber'})
            week = week.text
            if week == '01':
                count += 1
                shutil.copy(path +'/'+ file, father_dir+'/ones/'+ str(count) +file)
finally:
    print('Numbers of files copied: {}'.format(count))

