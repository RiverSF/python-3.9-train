from aiohttp import web
from router import setup_routes


async def handle(request):
    return web.Response(text='123456')


if __name__ == '__main__':
    app = web.Application()
    setup_routes(app)
    web.run_app(app, host='127.0.0.1', port=80)
