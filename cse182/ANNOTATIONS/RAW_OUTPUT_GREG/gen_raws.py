"""
    Combine raw alignment files into one alignment file per protein
"""


import os
import re


def read_write(directory, out_dir):
    """
        For each file in the directory, append to its corresponding raw 
        alignment file in the appropriate section
    """
    for filename in os.listdir(directory):
        raw_file = re.findall("([A-Za-z0-9]+)", filename)[0] + '.txt'
        raw_file = '../raw_aligns/{}/'.format(out_dir) + raw_file
        print(raw_file)

        # if file exists, append to it
        if os.path.isfile(raw_file):
            this_file = open(raw_file, 'a')
        else:
            this_file = open(raw_file, 'w')

        # write lines
        if directory=='BLAST' or directory=='Prosite':
            with open(directory + '/' + filename, 'r', encoding='ISO-8859-1') as source:
                for line in source:
                    this_file.write(line)
        else:
            with open(directory + '/' + filename, 'r') as source:
                for line in source:
                    this_file.write(line)

        this_file.close()

    return 0


if __name__ == '__main__':

    read_write('BLAST', 'BLAST')
    read_write('Pfam', 'Pfam')
    read_write('Prosite', 'Prosite')
    read_write('NucPloc', 'NucPloc')

