from mcp.server.fastmcp import FastMCP

from tools import get_air_quality
from tools import get_weather

### need to remove for product
# mcp_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, mcp_dir)
# from utils import config_manager
# from tools.weather import get_weather
# from tools.air_quality import get_air_quality
###

mcp = FastMCP(name='weather')


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
    mcp.run(transport="sse")
