"""
    Convert a given CSV file to JSON format to upload into sqlite3 database
    CSV file must have all appropriate fields for Annotation object
    Writes to fixture in anno_table django app
    REMEMBER TO LOAD DATA: python manage.py loaddata annotations.json
        ^ handled by main function
"""


import json
import csv
import argparse
import sqlite3
import re
import subprocess
from compile_data import read_tsv
from compile_data import read_csv
from compile_data import concat_files


def file_to_json(anno_file, tsv=False):
    """
        Convert file object to JSON
        Returns list of JSON objects per record in file object
    """

    json_annotations = []

    # proper indexing
    field = {
        0: 'name',
        1: 'blast',
        2: 'pfam',
        3: 'prosite',
        4: 'kegg',
        5: 'go',
        6: 'coment'         # still too lazy to fix typo
    }

    # convert each record to JSON object
    for record in anno_file:
        if tsv:
            record = record.strip().split()
        json_object = {'model': 'anno_table.annotation'}
        json_object['fields'] = {
            field[r]: element for r, element in enumerate(record)
        }

        json_annotations.append(json_object)

    return json.dumps(json_annotations)


def single_file_test():
    parser = argparse.ArgumentParser(description="Create JSON fixture")
    parser.add_argument(
        'from_file', help="File to be read"
    )
    parser.add_argument(
        '--clear', action='store_true', help="Clear old data from database"
    )
    parser.add_argument(
        '--header', action='store_true', help="Skip header"
    )

    args = parser.parse_args()

    if args.clear:
        con = sqlite3.connect("../cse182/db.sqlite3")
        c = con.cursor()
        c.execute("DELETE FROM anno_table_annotation;")
        con.commit()

    if re.findall("\.(csv)$", args.from_file):
        with open(args.from_file, 'r') as csv_input:
            csv_reader = csv.reader(csv_input)
            if args.header:
                next(csv_reader)
            with open('../cse182/anno_table/fixtures/annotations.json', 'w') as j:
                j.write(file_to_json(csv_reader))

    elif re.findall("\.(tsv)$", args.from_file):
        with open(args.from_file, 'r') as tsv_input:
            if args.header:
                next(tsv_reader)
            with open('../cse182/anno_table/fixtures/annotations.json', 'w') as j:
                j.write(file_to_json(tsv_input, tsv=True))


def main():
    parser = argparse.ArgumentParser(
        description="Create JSON fixture from 'data.txt'"
    )
    parser.add_argument(
        '--clear', action='store_true', help="Clear old data from database"
    )
    parser.add_argument(
        '--header', nargs='+', type=int, help="File index that has headers"
    )

    args = parser.parse_args()

    if args.clear:
        con = sqlite3.connect("../cse182/db.sqlite3")
        c = con.cursor()
        c.execute("DELETE FROM anno_table_annotation;")
        con.commit()

    skip_head = args.header if args.header else []
    concat_files(skip_head)

    with open('data.csv', 'r') as data:
        data_csv = csv.reader(data)
        with open('../cse182/anno_table/fixtures/annotations.json', 'w') as j:
            j.write(file_to_json(data_csv))

    subprocess.Popen([
        'python', '../cse182/manage.py', 'loaddata', 'annotations.json'
    ])


if __name__ == '__main__':
    main()
