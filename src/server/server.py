from mcp.server.fastmcp import FastMCP

from tools import get_air_quality
from tools import get_weather
from tools import random_generator


mcp = FastMCP(name='air_server',host="127.0.0.1",port=8000)


@mcp.tool()
async def weather(city_name:str)-> dict:
     """return weather"""
     repoert = await get_weather(city_name)
     return repoert


@mcp.tool()
async def air_pollution(city_name:str)-> dict:
    """return air pollution"""
    report = await get_air_quality(city_name)
    return report

@mcp.tool()
async def generate_random(kind: str = "float",
                          a: int | float = 0,
                          b: int | float = 1,
                          seed: int = 1099):
    """generate random number"""
    random_number = await  random_generator(kind, a, b, seed)
    return random_number

if __name__ == "__main__":

    mcp.run(transport="streamable-http")

