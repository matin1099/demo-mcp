from typing import Any
from loguru import logger as log
from mcp.server.fastmcp import FastMCP
import httpx
import asyncio

mcp = FastMCP(name='weather')
api_key = "Dwn0f2RGKABTOir+LWXttw==bjwpcCBKz0pYCVDY"

@mcp.tool()
async def get_weather(city: str) -> dict:
    log.success(f"Getting {city}")
    city_report = await city_to_coords(city)
    return city_report


async def city_to_coords(city: str) -> dict:
    log.success(f"Converting {city} to coords")
    if city.lower() == "tehran":
        return await send_request((35.7219, 51.3347))
    if city.lower() == "tabriz":
        return await send_request((38.0792, 46.2887))
    if city.lower() == "texas":
        return await send_request((31.9686, 99.9018))
    if city.lower() == "florida":
        return await send_request((27.6648, 81.5158))
    else:
        log.critical(f"Unknown city: {city}")
        raise Exception(f"unkown city:{city}")


async def send_request(coords: tuple, api_key=api_key) -> dict:
    # send httpx to web and receive respond
    log.success(f"Sending {coords}")
    url = f"https://api.api-ninjas.com/v1/weather?lat={str(coords[0])}&lon={str(coords[1])}"
    header = {"X-Api-Key": api_key}
    # async with httpx.AsyncClient() as client:
    #     response = await client.get(url, headers=header)
    #     log.success(f"response {response}")
    #     response.raise_for_status()
    #     return response.json()
    dummy_response = {'cloud_pct': 75, 'temp': 8, 'feels_like': 6, 'humidity': 40, 'min_temp': 8, 'max_temp': 8,
                      'wind_speed': 4.02, 'wind_degrees': 240, 'sunrise': 1765942708, 'sunset': 1765977785}
    log.info(f"Sending DUMMY INFO")
    return dummy_response

if __name__ == "__main__":
    # log.info("Starting server")
    # resp = asyncio.run(get_weather("TehRAn"))
    # print(resp)
    mcp.run(transport="sse")