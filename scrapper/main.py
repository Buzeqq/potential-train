from bs4 import BeautifulSoup
import requests
import re
import json


def scrap(website_url, *, script_fragment, data_pattern, data_brackets):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    js_script = find_script(soup, script_fragment)
    return get_json_data(js_script, data_pattern, data_brackets)


def find_script(html, script):
    checker = lambda x: script in x.text
    return list(filter(checker, html.find_all('script')))[0]


def get_json_data(script, pattern, brackets):
    hmm = re.findall(pattern, script.text)[0]
    return json.loads('{' + f"\"data\": {brackets[0]}{hmm}{brackets[1]}" + '}')


if __name__ == '__main__':
    url = 'https://www.sinsay.com/pl/pl/mezczyzna/ubrania?page=5'

    data = scrap(url,
                 script_fragment='window.getCatalogData = function()',
                 data_pattern=r'products: \[(.+)\]',
                 data_brackets='[]'
                 )

    print("Main page scraped")

    for i, item in enumerate(data['data']):
        print(f"Scraping item {i + 1}/{len(data['data'])}")
        product_url = item['url']

        item.update(scrap(product_url,
                          script_fragment="window['getProductData'] = function()",
                          data_pattern=r'return \{(.+)\}',
                          data_brackets='{}'
                          )
                    )

    to_save = json.dumps(data, indent=4)
    with open('data.json', 'w') as f:
        f.write(to_save)
