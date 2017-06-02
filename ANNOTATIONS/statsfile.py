"""
    Calculate statistics for records
"""


import csv


def statsdata():
    """
        Calculates statistics for recods in data.csv
        Returns num_hits / total_records, mapped to field index
        Index 0 and 6 should always be 1
    """
    with open('data.csv', 'r') as data:
        data_csv = csv.reader(data)
        
        # map counts to field index
        counter = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

        # perform counting increment for each line
        for line in data_csv:
            counter = {index:counter[index]+1 
                       if element else counter[index] 
                       for index,element in enumerate(line)}
        
        # modify by total counts
        max_count = counter[0]
        counter = {key: counter[key] / max_count for key in counter}

    return counter
    
if __name__ == '__main__':
    """
        Print the stat per field, labelled
        Debug purposes
    """  
    fields = ['Name', 'BLAST', 'Pfam', 'Prosite', 'KEGG', 'GO', 'Comments']
    labels = {fields[i]: i for i in range(7)}

    c = statsdata()

    for j in range(7):
        print(fields[j], c[labels[fields[j]]])
