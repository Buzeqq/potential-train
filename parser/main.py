import csv
import json
import random
from utils import cut_combinations


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


COLORS = {'czarny': 'Black', 'niebieski': 'Blue', 'kremowy': 'Beige', 'zielony': 'Green',
          'szary': 'Grey', 'czerwony': 'Red', 'pomarańczowy': 'Orange', 'żółty': 'Yellow',
          'brązowy': 'Brown', 'błękitny': 'Light Blue', 'różowy': 'Pink', 'fioletowy': 'Purple',
          'biały': 'White', 'khaki': 'Khaki', 'wielobarwny': 'Multicolor'}


def generate_combinations(prod_data, combination_writer):
    for pos, c in enumerate(prod_data['colorOptions']):
        if not c['isInStock']:
            continue
        row = {
            "Product ID": prod_data['id'],
            "Attribute": '',
            "Value": '',
            "Quantity": '',
            "Minimal quantity": 1,
            "Low stock level": 2,
            "Image URLs": "*".join([c['previewPhoto']])
        }
        attr = ":".join(["Color", "Drop-down list", str(pos + 1)])
        val = ":".join([COLORS[c['color']['name']], str(pos + 1)])
        for s in prod_data['sizes']:
            row['Attribute'] = attr + '*' + ":".join(["Size", "Drop-down list", str(pos + 1 + len(prod_data['colorOptions']))])
            row['Value'] = val + '*' + ":".join([s['sizeName'], str(pos + 1 + len(prod_data['colorOptions']))])
            row['Quantity'] = random.randint(1, 10)
            if s['stock']:
                combination_writer.writerow(list(row.values()))


def get_product_features(prod_data):
    if prod_data['data']['splitAdditionalDescription']['introductorySentence'] != "":
        features = ":".join(['produkt', prod_data['data']['splitAdditionalDescription']['introductorySentence'], '0', '0'])
    else:
        features = ":".join(['produkt', prod_data['name'], '0', '0'])
    features += "*" + ":".join(['materiał', prod_data['data']['material'], '1', '0'])
    if prod_data['data']['splitAdditionalDescription']['featuresInDescription'] is not None:
        features += "*" + ":".join(
                ['inne cechy produktu', '\n'.join(prod_data['data']['splitAdditionalDescription']['featuresInDescription']),
                 '2', '0'])
    return features


def set_product_fields(csv_data, prod_data):
    csv_data['Show price'] = 1
    csv_data['Available for order'] = 1
    csv_data['Quantity'] = random.randint(1, 10) if prod_data['colorOptions'][0]['isInStock'] else 0
    csv_data['Low stock level'] = 2
    csv_data['Text when in stock'] = "Product available"
    csv_data['Text when backorder allowed'] = "Product out of stock"
    # available values: both, catalog, search, none
    csv_data['Visibility'] = "both"
    # 1: PL Standard Rate (23%)
    csv_data['Tax rules ID'] = 1
    # price tax excl. = price tax incl. / (1 + tax)
    csv_data['Price tax excluded'] = round(float(csv_data['Price tax excluded'].replace(',', '.')) / 1.23, 2)
    if csv_data['On sale']:
        csv_data['Discount amount'] = round(float(prod_data['price'].replace(',', '.')) - float(prod_data['final_price'].replace(',', '.')), 2)
    csv_data['Feature'] = get_product_features(prod_data)


def products_to_csv():
    with open('products_import.csv', 'w+', encoding='utf-8', newline='') as products_csv,\
            open('combinations_import.csv', 'w+', encoding='utf-8', newline='') as combinations_csv,\
            open('../scrapper/products.json', 'r', encoding='utf-8') as products_file,\
            open('products_labels.json', 'r') as product_labels_file:
        product_labels = json.load(product_labels_file)
        products = json.load(products_file)
        writer = csv.writer(products_csv, delimiter=';')
        writer.writerow(list(product_labels.keys()))

        combination_writer = csv.writer(combinations_csv, delimiter=';')
        combination_writer.writerow(["Product ID", "Attribute", "Value", "Quantity", "Minimal quantity", "Low stock level", "Image URLs"])

        for p in products['data']:
            row = {}
            for key, el_path in product_labels.items():
                el = get_element(p, el_path)
                row[key] = parse_element(el)
            generate_combinations(p, combination_writer)
            set_product_fields(row, p)
            writer.writerow(list(row.values()))


def set_category_fields(csv_data, parent_category):
    csv_data["Root category"] = 0
    csv_data["Parent category"] = "Home" if parent_category is None else parent_category['name']


def parse_child_categories(writer: csv.writer, data_labels: dict, parent: dict):
    if 'children' not in parent or parent['level'] == 2:
        return
    for c in parent['children']:
        row = {}
        for key, el_path in data_labels.items():
            el = get_element(c, el_path)
            row[key] = parse_element(el)
        set_category_fields(row, parent)
        writer.writerow(list(row.values()))
        parse_child_categories(writer, data_labels, c)


def categories_to_csv():
    with open('categories_import.csv', 'w+', encoding='utf-8', newline='') as csv_file, \
            open('../scrapper/categories.json', 'r', encoding='utf-8') as cat_file, \
            open('categories_labels.json', 'r') as labels_file:
        data_labels = json.load(labels_file)
        categories = [json.load(cat_file)]
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(list(data_labels.keys()))

        for c in categories:
            row = {}
            for key, el_path in data_labels.items():
                el = get_element(c, el_path)
                row[key] = parse_element(el)
            set_category_fields(row, None)
            writer.writerow(list(row.values()))
            parse_child_categories(writer, data_labels, c)


if __name__ == "__main__":
    categories_to_csv()
    products_to_csv()
    cut_combinations()
