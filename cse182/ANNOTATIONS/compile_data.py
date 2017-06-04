"""
    All data must be compiled into a single file for upload into fixture
    Files will be concatenated into CSV format
"""


import csv
import re


def read_tsv(tsv_file, header=False):
    """
        Reads given file object
        File must be TSV format
        If header = True, skip first line
        Returns generator object for TSV file
    """
    if header:
        next(tsv_file)
    for line in tsv_file:
        yield line.strip().split()


def read_csv(csv_file, header=False):
    """
        Reads given file object
        File must be in CSV format
        If header = True, skip first line
        Returns generator object for CSV file
    """
    csv_reader = csv.reader(csv_file)
    if header:
        next(csv_reader)
    for line in csv_reader:
        yield line


def concat_files(skips=[]):
    """
        Concatenate the files listed in 'to_read.txt'
        Parameter skips is the array of indexes for files which have headers
        Outputs the results into 'data.csv'
    """
    # read the list of filenames
    with open('to_read.txt', 'r') as files:
        filenames = [line.strip() for line in files.readlines()]

    # refresh final data file
    open('data.csv', 'w').close()

    # perform operation for the list of given filenames
    for i, f in enumerate(filenames):
        print(f)
        ext = re.findall("\S*.([ct]sv)", f)[0]

        partial = open(f, 'r')

        # append to final data file
        with open('data.csv', 'a') as data:
            data_out = csv.writer(data)

            if ext == 'tsv':
                records = read_tsv(partial, header=(i in skips))
            elif ext == 'csv':
                records = read_csv(partial, header=(i in skips))

            for rec in records:
                data_out.writerow(rec)

        partial.close()


if __name__ == '__main__':
    concat_files()
