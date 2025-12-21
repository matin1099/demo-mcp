import httpx
from loguru import logger as log

from utils import config_manager
from .geocode import city_to_coords


async def get_air_quality(city: str) -> dict:
    """return air quality"""
    log.success(f"Getting {city}")
    coord = await city_to_coords(city)
    city_report = await air_quality_request(coord)
    return city_report


configs = config_manager.load_config()["tools"]["air_quality"]


async def air_quality_request(coords: tuple, ) -> dict:
    # send httpx to web and receive respond
    log.success(f"Sending {coords}")
    url = configs["url"].format(lat=coords[0], lon=coords[1])
    header = {"X-Api-Key": configs["secret"]}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=header)
        log.success(f"response {response}")
        response.raise_for_status()
        return response.json()
