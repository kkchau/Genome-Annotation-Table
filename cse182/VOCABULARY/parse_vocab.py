"""
    Parse given datafile for keywords
    Convert keywords to standard GO terminology
"""


import pandas as pd
from collections import defaultdict


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


def main():
    """
        Main function to avoid global variables
    """
    synonyms = syn_gen('GOTERMS.txt')

    source_data = pd.read_csv('../ANNOTATIONS/data.csv', header=0)
    for index, record in source_data.iterrows():
        blast = str(record['BLAST']).strip().split()
        pfam = str(record['Pfam']).strip().split()
        prosite = str(record['Prosite']).strip().split()
        go_list = []
        for hit in [blast, pfam, prosite]:
            for word in hit:
                if word in synonyms:
                    go_list.append(synonyms[word])
        record['Gene Ontology'] = list(set(go_list))
    
    # print for now, debugging
    print(source_data)


if __name__ == '__main__':
    main()
