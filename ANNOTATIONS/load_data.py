"""
    Convert a given CSV file to JSON format to upload into sqlite3 database
    CSV file must have all appropriate fields for Annotation object
    Writes to fixture in anno_table django app
"""


import json
import csv
import argparse
import sqlite3


def csv_to_json(csv_file):
    """
        Convert CSV file object to JSON
        Returns list of JSON objects per record in CSV file object
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
    for record in csv_file:
        json_object = {'model': 'anno_table.annotation'}
        json_object['fields'] = {
            field[r]: element for r, element in enumerate(record)
        }

        json_annotations.append(json_object)

    return json.dumps(json_annotations)


def main():
    parser = argparse.ArgumentParser(description="Create JSON fixture")
    parser.add_argument('from_csv', help="CSV file to be read")
    parser.add_argument(
        '-c', '--clear', action='store_true', help="Clear old data from database"
    )

    args = parser.parse_args()

    if args.clear:
        con = sqlite3.connect("../cse182/db.sqlite3")
        c = con.cursor()
        c.execute("DELETE FROM anno_table_annotation;")
        con.commit()

    with open(args.from_csv, 'r') as csv_input:
        csv_reader = csv.reader(csv_input)
        with open('../cse182/anno_table/fixtures/annotations.json', 'w') as j:
            j.write(csv_to_json(csv_reader))


if __name__ == '__main__':
    main()
