import asyncio
from views import index
from aiohttp import web


def setup_routes(app):
    app.router.add_get('/', index)
    app.add_routes([
        web.get('/demo', demo),
        web.get('/{name}', demo)
    ])


async def demo(request):
    await asyncio.sleep(1)
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)
