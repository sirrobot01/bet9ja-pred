import os



father_dir = os.path.dirname(os.getcwd())
dir_path = father_dir+'/downloads'
path_to_read = father_dir+'/all_scores'
path_to_write = father_dir+'/real_scores'


for (folder, sub_folder, filename) in os.walk(path_to_read):
    if not folder.endswith('scores'):
        for files in os.listdir(folder):
            w = ''
            foo = open(folder+'/'+files, 'r')
            for line in foo.readlines():
                if len(line) > 4:
                    if int(line[3]) > int(line[5]):
                        w += '0\n'
                    elif int(line[3]) < int(line[5]):
                        w += '1\n'
                    else:
                        w += '2\n'
            name_file = path_to_write + '/' + folder[-4:]+'/'+files
            os.makedirs(os.path.dirname(name_file), exist_ok=True)
            with open(name_file, "a") as writer:
                writer.write(w.strip('\n'))

