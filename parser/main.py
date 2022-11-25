import csv
import json
import logging


def get_element(p, keys: [str]):
    if not keys:
        return ''
    for key in keys:
        if isinstance(p, list):
            p = p[0]
        p = p[key]
    return p


def parse_element(el):
    if type(el) is bool:
        el = int(el)
    if type(el) is list:
        el = '*'.join(el)
    return el


# parsing ../scrapper/data.json into csv file
def products_to_csv():
    logging.basicConfig(filename='logs.log', filemode='w+', level=logging.INFO, encoding='utf-8')
    with open('products_import.csv', 'w+', encoding='utf-8', newline='') as csv_file,\
            open('../scrapper/products.json', 'r', encoding='utf-8') as products_file,\
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
