import os
import aiohttp
import json
import asyncio

async def f_p(s):
    url = f'https://jsonplaceholder.typicode.com/posts'
    async with s.get(url) as r:
        return await r.json()
async def d_and_s( output):
    async with aiohttp.ClientSession() as session:
        all_posts = await f_p(session)

        os.makedirs(output, exist_ok=True)

        for i, post in enumerate(all_posts):
            filename = os.path.join(output, f'{i + 1}.json')
            with open(filename, 'w') as file:
                json.dump(post, file, indent=2)
            print(f'Post {i + 1} saved to {filename}')


asyncio.run(d_and_s('j'))
