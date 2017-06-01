import csv

def statsdata():
    with open('data.csv', 'r') as data:
        data_csv = csv.reader(data)
        
        counter = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        for line in data_csv:
            counter = {index:counter[index]+1 
                       if element else counter[index] 
                       for index,element in enumerate(line)}
        
        max_count = counter[0]
        counter = {key: counter[key] / max_count for key in counter}
    return counter
    
    
       
