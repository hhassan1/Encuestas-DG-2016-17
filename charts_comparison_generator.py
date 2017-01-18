from numpy import mean
import csv
import sys
import json
import codecs

reload(sys)
sys.setdefaultencoding('utf8')

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

def main(input_file_1, input_file_2, output_file):
    dataset = []
    file_1_means = []
    labels = []
    file_2_means = []
    with codecs.open(input_file_1, 'r', 'utf-8') as csv_file_1:
        reader_1 = csv.reader(utf_8_encoder(csv_file_1), dialect='excel',delimiter=';')
        for question in reader_1:
            labels.append(question[0])
            file_1_means.append(mean([float(q) for q in question[1:]]))
    with codecs.open(input_file_2, 'r', 'utf-8') as csv_file_2:
        reader_2 = csv.reader(utf_8_encoder(csv_file_2), dialect='excel',delimiter=';')
        for question in reader_2:
            file_2_means.append(mean([float(q) for q in question[1:]]))
    dataset.append(
        { 
            'labels' : labels,
            'data': file_1_means,
            'backgroundColor' : 'rgba(255, 140, 0, 0.2)',
            'borderColor' : 'rgba(255, 140, 0, 1)',
            'borderWidth' : 1
        })
    dataset.append(
        { 
            'labels' : labels,
            'data': file_2_means,
            'backgroundColor' : 'rgba(0, 140, 255, 0.2)',
            'borderColor' : 'rgba(0, 140, 255, 1)',
            'borderWidth' : 1
        })
    with codecs.open(output_file, 'w', 'utf-8') as json_file:
        json.dump(dataset, json_file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
