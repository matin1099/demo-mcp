from .geocode import city_to_coords
from typing import Any
from loguru import logger as log
from mcp.server.fastmcp import FastMCP
import httpx
import asyncio
import sys, os

### need to remove for product
mcp_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, mcp_dir)
from utils import config_manager


###


async def get_weather(city: str, ) -> dict:
    """return weather"""
    log.success(f"Getting {city}")
    coord = await city_to_coords(city)
    city_report = await weather_request(coord)
    return city_report


configs = config_manager.load_config()["tools"]["weather"]


async def weather_request(coords: tuple, ) -> dict:
    # send httpx to web and receive respond
    log.success(f"Sending {coords}")
    url = configs["url"].format(lat=coords[0], lon=coords[1])
    header = {"X-Api-Key": configs["secret"]}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=header)
        log.success(f"response {response}")
        response.raise_for_status()
        return response.json()
    dummy_response = {'cloud_pct': 75, 'temp': 8, 'feels_like': 6, 'humidity': 40, 'min_temp': 8, 'max_temp': 8,
                      'wind_speed': 4.02, 'wind_degrees': 240, 'sunrise': 1765942708, 'sunset': 1765977785}
    log.info(f"Sending DUMMY INFO")
    final_response = {'cloud_pct': 75, 'temp': 8, 'feels_like': 6, 'humidity': 40, 'min_temp': 8, 'max_temp': 8,
                      'wind_speed': 4.02, }
    return final_response
