import os
from bs4 import BeautifulSoup

##########################################################

#FUNCTIONS

def week_func(soup):
    week = soup.find('span', {'id': 'leagueWeekNumber'})
    return week.text

############################################################
#DIRS

father_dir = os.path.dirname(os.getcwd())
dir_path = father_dir+'/downloads'
path_to_write = father_dir+'/all_odds'
count = 0

for file in os.listdir(dir_path):
    if file.endswith('html'):
        count = count + 1
        filename = dir_path+'/'+file
        w = ''
        soup = BeautifulSoup(open(filename), 'html.parser')
        odds = soup.findAll('td', {'style':'width:19%; text-align:center'})
        #mon = soup.find('span', {'style': 'padding:10px 0;'})
        mon = soup.find('span', {'id': 'idleague'})
        try:
            league = mon.text

        except:
            pass
        print('[**] Opening {}'.format(file))
        for odd in odds:


            ftcount = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for ftc in ftcount:
                fth = odd.findAll('label', {'for': 'Match_Result_' + str(ftc) + '_Home'})
                for ft0 in fth:
                    w += ft0.text + ','
                ftd = odd.findAll('label', {'for': 'Match_Result_' + str(ftc) + '_Draw'})
                for ft2 in ftd:
                    w += ft2.text + ','
                fta = odd.findAll('label', {'for': 'Match_Result_' + str(ftc) + '_Away'})
                for ft1 in fta:
                    w += ft1.text+'\n'

        league = league[-4:]
        name_file = path_to_write+'/'+league+'/'+week_func(soup)+'.csv'
        os.makedirs(os.path.dirname(name_file), exist_ok=True)
        with open(name_file, "w") as writer:
            writer.write(w)
print('[**] Numbers of pages crawled: {}'.format(count))


