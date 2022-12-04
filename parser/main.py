import csv
import json
import random


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


def set_product_fields(csv_data, prod_data):
    csv_data['Show price'] = 1
    csv_data['Available for order'] = 1
    csv_data['Quantity'] = random.randint(0, 10)
    csv_data['Accessories'] = "accessories field test"
    csv_data['Low stock level'] = 2
    csv_data['Text when in stock'] = "Product available"
    csv_data['Text when backorder allowed'] = "Product out of stock"
    # available values: new, used, refurbished
    csv_data['Condition'] = "new"
    # available values: both, catalog, search, none
    csv_data['Visibility'] = "both"
    # 1: PL Standard Rate (23%)
    csv_data['Tax rules ID'] = 1
    # price tax excl. = price tax incl. / (1 + tax)
    csv_data['Price tax excluded'] = round(float(csv_data['Price tax excluded'].replace(',', '.')) / 1.23, 2)
    if csv_data['On sale']:
        csv_data['Discount amount'] = round(float(prod_data['price'].replace(',', '.')) - float(prod_data['final_price'].replace(',', '.')), 2)


def products_to_csv():
    with open('products_import.csv', 'w+', encoding='utf-8', newline='') as csv_file,\
            open('../scrapper/products.json', 'r', encoding='utf-8') as products_file,\
            open('products_labels.json', 'r') as labels_file:
        data_labels = json.load(labels_file)
        products = json.load(products_file)
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(list(data_labels.keys()))

        for p in products['data']:
            row = {}
            for key, el_path in data_labels.items():
                el = get_element(p, el_path)
                row[key] = parse_element(el)
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
