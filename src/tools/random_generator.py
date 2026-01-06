from  loguru import logger as log
import random


async def random_generator(kind: str , a: int, b: int , seed: int ):
    """generate a random number between a and b based on seed"""
    log.info(f"Random generator: kind:\t{kind}, a=\t{a}, b=\t{b}, seed:\t{seed}")
    if kind.lower() == "float":
        return await rand_float(a,b,seed)
    else:
        return await rand_int(a,b,seed)


async def rand_float(a: int, b: int, seed: int ):
    random.seed(seed)
    rand = random.uniform(a, b)
    log.info(f"FLOAT generator:\t\tGENERATED:\t{rand} a=\t{a}, b=\t{b}, seed:\t{seed}")
    return rand

async def rand_int(a: int, b: int, seed: int ):
    random.seed(seed)
    rand = random.randint(a, b)
    log.info(f"integer generator:\t\tGENERATED:\t{rand} a=\t{a}, b=\t{b}, seed:\t{seed}")
    return rand