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

mcp = FastMCP(name='weather')


@mcp.tool()
async def get_weather(city: str, coard:tuple=None) -> dict:
    """return weather"""
    log.success(f"Getting {city}")
    coord = await city_to_coords(city)
    city_report = weather_request(coord)
    return city_report


async def city_to_coords(city: str) -> dict:
    log.success(f"Converting {city} to coords")
    if city.lower() == "tehran":
        return await weather_request((35.7219, 51.3347))
    if city.lower() == "tabriz":
        return await weather_request((38.0792, 46.2887))
    if city.lower() == "texas":
        return await weather_request((31.9686, 99.9018))
    if city.lower() == "florida":
        return await weather_request((27.6648, 81.5158))
    else:
        log.critical(f"Unknown city: {city}")
        raise Exception(f"unkown city:{city}")


configs = config_manager.load_config()["tools"]["weather"]


async def weather_request(coords: tuple, api_key=api_key) -> dict:
    # send httpx to web and receive respond
    log.success(f"Sending {coords}")
    url = configs["url"].format(lat=coords[0], lon=coords[1])
    header = {"X-Api-Key": configs["secret"]}
    # async with httpx.AsyncClient() as client:
    #     response = await client.get(url, headers=header)
    #     log.success(f"response {response}")
    #     response.raise_for_status()
    #     return response.json()
    dummy_response = {'cloud_pct': 75, 'temp': 8, 'feels_like': 6, 'humidity': 40, 'min_temp': 8, 'max_temp': 8,
                      'wind_speed': 4.02, 'wind_degrees': 240, 'sunrise': 1765942708, 'sunset': 1765977785}
    log.info(f"Sending DUMMY INFO")
    final_response = {'cloud_pct': 75, 'temp': 8, 'feels_like': 6, 'humidity': 40, 'min_temp': 8, 'max_temp': 8,
                      'wind_speed': 4.02, }
    return configs


# @mcp.tool
# async def get_air_quality(city: str, coord: tuple=None) -> dict:
#     """return air quality of given city"""
#     if coord == None:
#         coord = await city_to_coords(city)
#     quality_report = await
#
#     log.success(f"Getting {city}")
#
# async def quality_request(coord: tuple) -> dict:
#     pass
#

if __name__ == "__main__":
    # log.info("Starting server")
    # resp = asyncio.run(get_weather("TehRAn"))
    # print(resp)
    mcp.run(transport="sse")
