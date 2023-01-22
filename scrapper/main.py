import time
import json
import asyncio
import aiohttp

from scrapping_functions import scrap_main_page, scrap_product_page


async def main():
    async with aiohttp.ClientSession() as session:
        data = await scrap_main_page(session)

        tasks = []
        for i, item in enumerate(data):
            product_url = item['url']

            tasks.append(asyncio.ensure_future(scrap_product_page(session, product_url, i)))

        products = await asyncio.gather(*tasks)

        for product_data, item in zip(products, data):
            item['data'] = product_data

    to_save = {"data": data}
    to_save = json.dumps(to_save, indent=4)
    with open('data.json', 'w') as f:
        f.write(to_save)

    print("Statistics:")
    print("Total products: ", len(data))


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print("Time elapsed: {:.2f}s".format(time.time() - start_time))


