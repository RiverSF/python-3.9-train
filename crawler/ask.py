import asks
import anyio
import curio
import trio

async def worker(s, url):
    r = await s.get(url)
    print(r.text)

async def main(url_list):
    s = asks.Session(connections=30)
    for url in url_list:
        await curio.spawn(worker(s, url))