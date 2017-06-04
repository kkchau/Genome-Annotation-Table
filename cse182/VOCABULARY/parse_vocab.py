"""
    Parse given datafile for keywords
    Convert keywords to standard GO terminology
"""


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


if __name__ == '__main__':
    main()
