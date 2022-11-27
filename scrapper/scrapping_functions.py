import asyncio
import json
import platform
import re

from bs4 import BeautifulSoup

# cuz windows
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def scrap(session, website_url, *, script_fragment, data_pattern, data_brackets, **kwargs):
    async with session.get(website_url) as request:
        if request.status != 200:
            raise Exception("Status code is not 200")
        print(f"Scraping {kwargs['page_number'] if 'page_number' in kwargs else 'main'} page")
        soup = BeautifulSoup(await request.text(), 'html.parser')
        js_script = await find_script(soup, script_fragment)
        data = await get_json_data(js_script, data_pattern, data_brackets)
    return data


async def find_script(html, script):
    checker = lambda x: script in x.text
    return list(filter(checker, html.find_all('script')))[0]


async def get_json_data(script, pattern, brackets):
    hmm = re.findall(pattern, script.text)[0]
    return json.loads(f"{brackets[0]}{hmm}{brackets[1]}")


async def scrap_main_page(session):
    url = 'https://www.sinsay.com/pl/pl/mezczyzna/ubrania?page=5'
    return await scrap(session, url,
                       script_fragment='window.getCatalogData = function()',
                       data_pattern=r'products: \[(.+)\]',
                       data_brackets='[]'
                       )


async def scrap_categories(session):
    url = 'https://www.sinsay.com/pl/pl/mezczyzna/ubrania'
    return await scrap(session, url,
                       script_fragment='if (!window.getHeaderData) {',
                       data_pattern=r'"tree":\[(.+)\]',
                       data_brackets='[]'
                       )


async def scrap_subpage(session, url, category=None):
    return await scrap(session, url,
                       script_fragment='window.getCatalogData = function()',
                       data_pattern=r'products: \[(.+)\]',
                       data_brackets='[]',
                       page_number=category
                       )


async def scrap_product_page(session, product_url, i):
    return await scrap(session, product_url,
                       script_fragment="window['getProductData'] = function()",
                       data_pattern=r'return \{(.+)\}',
                       data_brackets='{}',
                       page_number=i
                       )
