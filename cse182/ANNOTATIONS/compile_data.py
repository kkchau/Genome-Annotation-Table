"""
    All data must be compiled into a single file for upload into fixture
    Files will be concatenated into CSV format
"""


import csv
import re
import pandas as pd
import numpy as np


fields = [
    'Sequence',
    'BLAST',
    'Pfam',
    'Prosite',
    'KEGG Pathway',
    'NucPloc',
    'Gene Ontology',
    'Comments'
]

not_found = ['null', 'NULL', 'No Hits']


def concat_files():
    """
        Concatenate data files
    """
    with open('to_read.txt', 'r') as files:
        filenames = [line.strip() for line in files.readlines()]

        open('data.csv', 'w').close()

        data_df = pd.DataFrame()

        all_df = []
        for f in filenames:

            # skip these files
            if f[0] == '#':
                continue

            print(f)

            # check extension
            ext = re.findall("\S*.([ct]sv)", f)[0]
            this_df = None

            if ext == 'tsv':
                this_df = pd.read_csv(f, index_col=None, header=0, sep='\t')
            elif ext == 'csv':
                this_df = pd.read_csv(f, index_col=None, header=0)

            if this_df is not None:
                all_df.append(this_df)

        data_df = pd.concat(all_df, ignore_index=True)[fields]
        for item in not_found:
            data_df.replace(item, np.NaN, inplace=True)
        data_df.to_csv('data.csv', index=False)


if __name__ == '__main__':
    concat_files()
