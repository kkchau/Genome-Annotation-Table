"""
    All data must be compiled into a single file for upload into fixture
    Files will be concatenated into CSV format
"""


import csv
import re
import pandas as pd


def concat_files():
    with open('to_read.txt', 'r') as files:
        filenames = [line.strip() for line in files.readlines()]

        open('data.csv', 'w').close()

        data_df = pd.DataFrame()

        all_df = []
        for f in filenames:
            ext = re.findall("\S*.([ct]sv)", f)[0]
            this_df = None

            if ext == 'tsv':
                this_df = pd.read_csv(f, index_col=None, header=0, sep='\t')
            elif ext == 'csv':
                this_df = pd.read_csv(f, index_col=None, header=0)

            if this_df is not None:
                all_df.append(this_df)

        data_df = pd.concat(all_df, ignore_index=True)
        data_df.to_csv('data.csv', index=False)


if __name__ == '__main__':
    concat_files2()
