"""
    Parse given datafile for keywords
    Convert keywords to standard GO terminology
"""


import pandas as pd
from goparse import goParse


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
    
    source_data.to_csv('aaa.csv', index=False)


if __name__ == '__main__':
    main()
