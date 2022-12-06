import asyncio
import json
import time

import aiohttp

from scrapping_functions import scrap_categories, scrap_subpage, scrap_product_page


async def main():
    async with aiohttp.ClientSession() as session:
        categories = await scrap_categories(session)

        # mezczyzna/ubrania
        categories_to_scrap = categories[2]['children'][0]['children']

        subpages_tasks = []
        for item in categories_to_scrap:
            subpage_url = item['url']
            category_name = item['name']
            subpages_tasks.append(asyncio.create_task(scrap_subpage(session, subpage_url, category_name)))

        subpages_data = await asyncio.gather(*subpages_tasks)

        products_tasks = []
        for subpage, category in zip(subpages_data, categories_to_scrap):
            category_name = category['name']
            category_tasks = []
            for i, product in enumerate(subpage):
                product_url = product['url']
                category_tasks.append(asyncio.create_task(
                    scrap_product_page(session, product_url, f"{category_name}_{i}")
                ))
            products_tasks.append(asyncio.gather(*category_tasks))

        products_data = await asyncio.gather(*products_tasks)

        to_save = {'data': []}

        for products, subpages, category in zip(products_data, subpages_data, categories_to_scrap):
            category_copy = category.copy()
            category_copy.pop('children', None)
            for product, subpage in zip(products, subpages):
                product['category'] = category_copy
                product.pop('recommended', None)
                subpage['data'] = product
            to_save['data'].extend(subpages)

        with open('products.json', 'w', encoding='utf-8') as f:
            json.dump(to_save, f, indent=4, ensure_ascii=False)

        with open('categories.json', 'w', encoding='utf-8') as f:
            json.dump(categories[2]['children'][0], f, indent=4, ensure_ascii=False)

        print("Statistics:")
        print("Total products: ", len(to_save['data']))

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f"Time: {time.time() - start}")