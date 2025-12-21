import asyncio
import os
import sys
from time import sleep

import httpx
from loguru import logger as log

### need to remove for product
mcp_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, mcp_dir)
from utils import config_manager

###

config = config_manager.load_config()["tools"]["geocode"]


async def city_to_coords(city: str) -> dict:
    url = config["url"].format(city=city)
    headers = {"X-Api-key": config["secret"]}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        log.success(f"response {response}")
        response.raise_for_status()
        response_json = response.json()
        response_json = response_json[0]
        sleep(1.5)
        return (response_json["latitude"], response_json["longitude"])


async def main():
    report = await city_to_coords("tehran")
    print(report)
    print(type(report))


if __name__ == "__main__":
    asyncio.run(main())
