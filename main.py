import pandas as pd
import csv

output_data = []

def process(dic_data):

    if 'as' in dic_data.keys() or 'bs' in dic_data.keys():
        for key in dic_data.keys():
            for item in dic_data[key]:
                temp = {}
                temp['name'] = key
                temp['price'] = float(item[0])
                temp['volumn'] = float(item[1])
                temp['timestamp'] = float(item[2])
                temp['updateType'] = ''
                temp['c'] = ''
                output_data.append(temp)
    else:
        c = ''
        if 'c' in dic_data.keys():
            c = dic_data['c']
        
        for key in dic_data.keys():
            if key == 'c':
                continue

            for item in dic_data[key]:
                length = len(item)
                temp = {}
                temp['name'] = key
                temp['price'] = float(item[0]) if length > 0 else 0
                temp['volumn'] = float(item[1]) if length > 1 else 0
                temp['timestamp'] = float(item[2]) if length > 2 else 0
                temp['updateType'] = item[3] if length > 3 else 0
                temp['c'] = c

                output_data.append(temp)

if __name__ == '__main__':

    file = open('csvData.csv', 'r')
    Lines = file.readlines()

    output_data = []
    for line in Lines:
        index = line.rfind('}')
        if index == -1:
            continue
        line = line[:index+1]
        line_dict = eval(line)
        process(line_dict)

    output_df = pd.DataFrame(output_data)
    output_df.to_csv('result.csv', sep='\t')

