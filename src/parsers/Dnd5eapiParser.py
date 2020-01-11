import asyncio
import json
from aiohttp import ClientSession
from typing import List
from model.DefaultClassBuilder import parse_to_default_class

dnd_5e_url = "http://www.dnd5eapi.co/"


# TODO: finish implementation. Parse information, check if exists in database or send to database (TinyDB)
async def get_monster_url_list() -> List[str]:
    url = "http://www.dnd5eapi.co/api/monsters/"
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            result = json.loads(response)
            count = result["count"]
            ret_val = []
            for i in range(1, count):
                base_url = "http://www.dnd5eapi.co"
                # url_suffix e.g. "/api/monsters/aboleth"
                url_suffix = result["results"][i]["url"]
                print(url_suffix + "\n")
                ret_val.append(base_url + url_suffix)
            return ret_val


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()


async def get_all_monsters():
    tasks = []
    monster_list = await get_monster_url_list()

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for monster_url in monster_list:
            task = asyncio.ensure_future(fetch(monster_url, session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        for response in responses:
            default_class = parse_to_default_class(json.loads(response))
            if default_class.class_name == "Adult Green Dragon":
                print(default_class.__dict__)
            # TODO: do something w this


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(get_all_monsters())
loop.run_until_complete(future)
