import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup


#############################################################
#DIRS
father_dir = os.path.dirname(os.getcwd())
dir_path = father_dir+'/downloads'
path_to_write = father_dir+'/all_scores'

##############################################################
#FUNCTIONS

def week_func(soup):
    week = soup.find('span', {'id': 'leagueWeekNumber'})
    return week.text

#################################################################
##################################################################

count = 0

for file in os.listdir(dir_path):
    if file.endswith('html'):
        filename = dir_path+'/'+file
        count += 1
        print('[**] Opening {}'.format(file))
        soup = BeautifulSoup(open(filename), 'html.parser')

        odds = soup.findAll('td', {'style': 'width: 33%; text-align:center; background-color: #E1E3E6; padding: 7px'})
        #mon = soup.find('span', {'style': 'padding:10px 0;'})
        mon = soup.find('span', {'id': 'idleague'})
        try:
            league = mon.text
        except:
            pass

        for odd in odds:
            oddn = odd.findAll('tr')

            wr = str(oddn[0].text)[7:10].strip('\n')
            w = ''
            for i in oddn:
                w += i.text


            league = league[-4:]
            name_file = path_to_write + '/' + league + '/' + wr.strip(' ') + '.csv'
            os.makedirs(os.path.dirname(name_file), exist_ok=True)
            with open(name_file, "w") as writer:
                writer.write(w[65:].strip('\n'))
print('\n [**] Files crawled: {}'.format(count))