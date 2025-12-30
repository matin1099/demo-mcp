from mcp.server.fastmcp import FastMCP

from tools import get_air_quality
from tools import get_weather


mcp = FastMCP(name='air_server',)


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



if __name__ == "__main__":
    # log.info("Starting server")
    # resp = asyncio.run(get_weather("TehRAn"))
    # print(resp)
    mcp.run(transport="streamable-http",)
    # mcp.run(transport="stdio",)
