import asyncio

from aiohttp import web
from webargs import fields
from webargs.aiohttpparser import use_kwargs, parser

# Demonstrate basic implementation of args
hello_args = {"name": fields.Str(missing="World")}

# Demonstrate how to use default values
# And how to specify type for arguments.
age_args = {"age": fields.Integer(required=True),
            "number": fields.Integer(missing=1)}

# No decorator
async def hello(request):
    args = await parser.parse(hello_args, request)
    return web.Response(body="Hello, {}".format(args['name']).encode("utf-8"))

# Decorator with coroutine
@asyncio.coroutine
@use_kwargs(hello_args)
def coro_hello(request, name):
    return web.Response(body="Hello, {}".format(name).encode("utf-8"))

# Decorator with async def
@use_kwargs(hello_args)
async def async_hello(request, name):
    return web.Response(body="Hello, {}".format(name).encode("utf-8"))


@asyncio.coroutine
@use_kwargs(age_args)
def coro_age(request, age, number):
    magic_number = age * number
    return web.Response(body="You're age * number is {}".format(magic_number).encode("utf-8"))

app = web.Application()
app.add_routes([web.get('/hello', hello),
                web.get('/async_hello', async_hello),
                web.get('/coro_hello', coro_hello),
                web.get('/coro_age', coro_age)])

web.run_app(app)