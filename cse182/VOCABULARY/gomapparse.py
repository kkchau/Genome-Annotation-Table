"""
    Parse the GO map files and return dictionaries
    Used to map terms to GO terms
"""


from collections import defaultdict


def pfam2go():
    """
        Parse the pfam2go file, mapping pfam terms to go terms
        Returns a dictionary of pfam term keys and go term values
    """
    go_map = defaultdict(list)

    # open map file
    with open('go_maps/pfam2go.txt', 'r') as pfam_file:
        for line in pfam_file:

            # skip descriptor
            if line[0] == '!':
                continue

            # process each line for relevant information
            pfam_id = line.partition(':')[2].strip().split()[0]
            go_id = line.partition(';')[2].strip().split()[0]
            go_name = line.partition('>')[2].strip().split(';')[0].partition(':')[2]

            # formatting
            go_full = go_id.strip() + '-' + go_name.strip()

            go_map[pfam_id].append(go_full)

    # formatting
    for key in go_map:
        go_map[key] = '|'.join(go_map[key])

    return go_map


def prosite2go():
    """
        Parse the prosite2go file, mapping pfam terms to go terms
        Returns a dictionary of pfam term keys and go term values
    """
    go_map = defaultdict(list)

    # open map file
    with open('go_maps/prosite2go.txt', 'r') as prosite_file:
        for line in prosite_file:

            # skip descriptor
            if line[0] == '!':
                continue

            # process each line for relevant information
            prosite_id = line.partition(':')[2].strip().split()[0]
            go_id = line.partition(';')[2].strip().split()[0]
            go_name = line.partition('>')[2].strip().split(';')[0].partition(':')[2]

            # formatting
            go_full = go_id.strip() + '-' + go_name.strip()

            go_map[prosite_id].append(go_full)

    # formatting
    for key in go_map:
        go_map[key] = '|'.join(go_map[key])

    return go_map


def main():
    print(prosite2go())


if __name__ == '__main__':
    main()

