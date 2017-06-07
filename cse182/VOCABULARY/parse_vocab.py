"""
    Parse given datafile for keywords
    Convert keywords to standard GO terminology
"""


import pandas as pd
import re
from collections import defaultdict
from gomapparse import pfam2go
from gomapparse import prosite2go


pfam_map = pfam2go()
prosite_map = prosite2go()


def processGoTerm(goTerm):
    """
        Process passed goTerm defaultdict object into manageable dictionary
        with collapsed single-item lists
    """
    proc = dict(goTerm)
    for key, value in proc.items():
        if len(value) == 0:
            proc[key] = value[0]        # collapse single-item lists
    return proc


def goParse(filename):
    """
        Parse the given GO file for term objects
        Generates Gene Onotology terms
    """
    with open(filename, 'r') as infile:
        currentGoTerm = None
        for line in infile:

            line = line.strip()
            if not line: continue       # skip empty lines

            # goTerm defaultdict
            if line == '[Term]':
                if currentGoTerm: 
                    yield processGoTerm(currentGoTerm)
                currentGoTerm = defaultdict(list)

            elif line == '[Typedef]':
                currentGoTerm = None

            # try to parse goTerm entry
            else:
                if currentGoTerm is None: 
                    continue

                # add information
                key, sep, value = line.partition(':')
                currentGoTerm[key].append(value.strip())

        if currentGoTerm is not None:
            yield processGoTerm(currentGoTerm)


def syn_gen(filename):
    """
        Create a dictionary mapping terms to standard GO terms
        TODO: Format synonyms
        TODO: Format GO term
    """
    syn_dict = {}
    for record in goParse('GOTERMS.txt'):
        name = record['name'][0]
        go_id = record['id'][0]

        # some terms don't have synonyms
        if 'synonym' in record:
            for s in record['synonym']:
                # NEED TO CONFIRM FORMATTING
                s = s.strip().split('\"')[1]
                syn_dict[s] = go_id + '-' + name

        # the term is its own synonym
        syn_dict[name] = go_id + '-' + name
    return syn_dict


def parse_gaspedal():
    """
        Parse team Gas Pedal's keyword table for standardizing GO terms
    """
    with open('keywords_gaspedal.tsv', 'r') as keywords:
        header = next(keywords)
        with open('keywords_gaspedal_go.tsv', 'w') as go_key:
            go_key.write(header)
            for record in keywords:
                record = record.strip().split('\t')

                go = []

                # get term ids for each field
                pfam_id = re.findall("(PF[0-9]+)", record[2])
                pfam_id = pfam_id[0] if pfam_id else None
                prosite_id = re.findall("(PR[0-9]+)", record[3])
                prosite_id = prosite_id[0] if prosite_id else None

                if pfam_id and pfam_id in pfam_map:
                    go.append(pfam_map[pfam_id])
                if prosite_id and prosite_id in prosite_map:
                    go.append(prosite_map[prosite_id])

                if record[5] == 'NULL' and go:
                    record[5] = ';'.join(list(set(go)))
                elif record[5] == 'NULL' and not go:
                    pass
                else:
                    if go:
                        record[5] += ' > ' + ';'.join(list(set(go)))

                go_key.write('\t'.join(record) + '\n')
    return 0


def parse_jem():
    """
        Parse team JEM's keyword table for standardizing GO terms
    """
    pass


def parse_tripla():
    """
        Parse team Triple A's keyword table for standardizing GO terms
    """
    pass


def parse_jkt():
    """
        Parse team JKT's keyword table for standardizing GO terms
    """
    pass


def main():
    parse_gaspedal()


if __name__ == '__main__':
    main()
