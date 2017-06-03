"""
    Standardization of vocabulary using a GO_SLIM file
    Constant-space parsing of Gene Ontology OBO-format file
    Appropriated from: https://techoverflow.net/2013/11/18/a-geneontology-obo-v1-4-parser-in-python/ 
"""

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
