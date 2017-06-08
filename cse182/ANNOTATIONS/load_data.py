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
from compile_data import concat_files
from compile_data import collapse_data


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
        5: 'nuc',
        6: 'go',
        7: 'coment'         # still too lazy to fix typo
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


def main():
    parser = argparse.ArgumentParser(
        description="Create JSON fixture from 'data.txt'"
    )
    parser.add_argument(
        '--clear', action='store_true', help="Clear old data from database"
    )
    args = parser.parse_args()

    # clear database if clear flag is specified
    if args.clear:
        con = sqlite3.connect("../db.sqlite3")
        c = con.cursor()
        c.execute("DELETE FROM anno_table_annotation;")
        con.commit()

    # compile data together
    concat_files()
    # collapse_data()

    # create data file
    # with open('data.csv', 'r') as data:
    with open('data_full.csv', 'r') as data:
        data_csv = csv.reader(data)
        next(data_csv)                  # skip header
        with open('../anno_table/fixtures/annotations.json', 'w') as j:
            j.write(file_to_json(data_csv))

    subprocess.Popen([
        'python', '../manage.py', 'loaddata', 'annotations.json'
    ])


if __name__ == '__main__':
    main()
