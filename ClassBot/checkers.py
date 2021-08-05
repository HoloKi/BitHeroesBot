import uuid
import json
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import logging
import asyncio

USER = hex(uuid.getnode())

'''
Discord Implementation to count user
'''


async def foo():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(
            'https://discord.com/api/webhooks/870586161620484146/jdALZsGh3qe51e9J5fT8YPxIhYVsXCcdiaJBHZ4vKAbwBfdzKveqpxWYTqP-Ow81kg6i',
            adapter=AsyncWebhookAdapter(session))
        await webhook.send(f'{USER} is using the bot with version {VERSION}', username=USER)


def check():
    f = open('data.json', "r")
    data = json.loads(f.read())
    a = int(data['yes'])
    logging.debug(f"a = {a}")
    f.close()
    if a == 0:
        loop = asyncio.get_event_loop()
        cazzo = loop.run_until_complete(foo())
        loop.close()
        data['yes'] = 1
        f = open('data.json', 'w')
        # data = json.loads(f.read())
        json.dump(data, f)
        f.close()
    else:
        f.close()
