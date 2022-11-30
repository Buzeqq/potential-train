import csv
import json


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


def products_to_csv():
    with open('products_import.csv', 'w+', encoding='utf-8', newline='') as csv_file,\
            open('../scrapper/products.json', 'r', encoding='utf-8') as products_file,\
            open('products_labels.json', 'r') as labels_file:
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


def parse_child_categories(writer: csv.writer, data_labels: dict, parent: dict):
    if 'children' not in parent:
        return
    for c in parent['children']:
        row = []
        for key, el_path in data_labels.items():
            if key == "Root category":
                el = 0
            elif key == "Parent category":
                el = parent['name']
            else:
                el = get_element(c, el_path)
                el = parse_element(el)
            row.append(el)
        writer.writerow(row)
        parse_child_categories(writer, data_labels, c)


def categories_to_csv():
    with open('categories_import.csv', 'w+', encoding='utf-8', newline='') as csv_file, \
            open('../scrapper/categories.json', 'r', encoding='utf-8') as cat_file, \
            open('categories_labels.json', 'r') as labels_file:
        data_labels = json.load(labels_file)
        categories = json.load(cat_file)
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(list(data_labels.keys()))

        for c in categories:
            row = []
            for key, el_path in data_labels.items():
                if key == "Root category":
                    el = 1 if not c['level'] else 0
                else:
                    el = get_element(c, el_path)
                    el = parse_element(el)
                row.append(el)
            writer.writerow(row)
            parse_child_categories(writer, data_labels, c)


if __name__ == "__main__":
    categories_to_csv()
    products_to_csv()
