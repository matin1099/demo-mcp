from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime

@tool
def get_weather_for_location(city: str) -> str:
    """get weather for a given city"""
    return f"it is always sunnt in {city}"

@dataclass
class Context:
    """Custom runtime context schema"""
    user_id: str


@tool
def get_user_location(runtime:ToolRuntime[Context]) -> str:
    """Retrieve user information based on user ID."""
    user_id = runtime.context.user_id
    return "Florida" if user_id == 1 else "SF"
