import json
from pathlib import Path
from loguru import logger as log


config_file = Path(__file__).parent.parent / "config.json"


@log.catch
def load_config():
    log.trace("loading config file")
    if not config_file.exists():
        raise FileNotFoundError(f"Config file {config_file} not found")

    with open(config_file, "r") as f:
        config = json.load(f)
        log.success("config file loaded SUCCESSFULLY")
        return config


