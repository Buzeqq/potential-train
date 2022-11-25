import csv
import json
import logging


def get_element(p, keys: [str]):
    keys_len = len(keys)
    if keys_len == 0:
        return ''
    elif keys_len == 1:
        return p[keys[0]]
    elif keys_len == 2:
        if type(p[keys[0]]) is list:
            if type(p[keys[0]][0]) is dict:
                return p[keys[0]][0][keys[1]]
            else:
                logging.warning(f'not a dict! - {p[keys[0]][0]}')
                return ''
        else:
            return p[keys[0]][keys[1]]
    elif keys_len == 3:
        return p[keys[0]][keys[1]][keys[2]]


def parse_element(el):
    if type(el) is bool:
        el = int(el)
    if type(el) is list:
        el = '*'.join(el)
    return el


# parsing ../scrapper/data.json into csv file
def products_to_csv():
    logging.basicConfig(filename='logs.log', filemode='w+', level=logging.INFO, encoding='utf-8')
    with open('products_import.csv', 'w+') as csv_file,\
            open('../scrapper/data.json', 'r') as products_file,\
            open('data_labels.json', 'r') as labels_file:
        data_labels = json.load(labels_file)
        products = json.load(products_file)
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(list(data_labels.keys()))

        for p in products['data']:
            row = []
            for el_path in data_labels.values():
                el = get_element(p, el_path)
                el = parse_element(el)
                row.append(el)
            writer.writerow(row)


if __name__ == "__main__":
    products_to_csv()
