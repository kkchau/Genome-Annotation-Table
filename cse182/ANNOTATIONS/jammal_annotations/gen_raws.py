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
        with open(directory + '/' + filename, 'r') as source:
            for line in source:
                this_file.write(line)

        this_file.close()

    return 0


if __name__ == '__main__':

    read_write('BLAST_files_raw', 'BLAST')
    read_write('Pfam_files_raw', 'Pfam')
    read_write('prosite_txt', 'Prosite')

