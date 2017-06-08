"""
    Get top 20 most frequent GO terms into text file
"""


import csv
import re


all_go = {}

with open('../ANNOTATIONS/data_full.csv', 'r') as data:
    data_csv = csv.reader(data)
    for record in data_csv:
        if not record[6]:
            continue
        this_go = re.findall("(GO:[0-9]+)", record[6])
        print(this_go)
        for go in this_go:
            if go not in all_go:
                all_go[go] = 0
            all_go[go] += 1

with open('freq_go.tsv', 'w') as go_freq:
    most_freq = []
    for i in range(20):
        next_max = max(all_go, key=lambda key: all_go[key])
        most_freq.append((next_max, all_go[next_max]))
        del all_go[next_max]
    go_freq.write('\n'.join(['\t'.join([m[0], str(m[1])]) for m in most_freq]))
