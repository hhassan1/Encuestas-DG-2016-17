from numpy import histogram
import csv
import sys
import json
import codecs

reload(sys)
sys.setdefaultencoding('utf8')

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

def main(input_file, output_file):    
    dataset = []
    with codecs.open(input_file, 'r', 'utf-8') as csv_file:
        reader = csv.reader(utf_8_encoder(csv_file), dialect='excel',delimiter=';')
        for question in reader:
            dataset.append(
                { 
                    'title' : question[0],
                    'data' : histogram([int(q) for q in question[1:]], bins = 6, range= (0,5))[0].tolist(),
                    'backgroundColor' : ['rgba(0, 0, 0, 0.2)', 'rgba(255, 0, 0, 0.2)', 'rgba(191, 64, 0, 0.2)', 'rgba(127, 127, 0, 0.2)', 'rgba(64, 191, 0, 0.2)', 'rgba(0, 255, 0, 0.2)'],
                    'borderColor' : ['rgba(0, 0, 0, 1)', 'rgba(255, 0, 0, 1)', 'rgba(191, 64, 0, 1)', 'rgba(127, 127, 0, 1)', 'rgba(64, 191, 0, 1)', 'rgba(0, 255, 0, 1)'],
                    'borderWidth' : 1
                })
    

    with codecs.open(output_file, 'w', 'utf-8') as json_file:
        json.dump(dataset, json_file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
