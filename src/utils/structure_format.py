from dataclasses import dataclass

# We use a dataclass here, but Pydantic models are also supported.
@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    # A human_liked_response (always required)
    human_liked_response: str
    # Any interesting information about the weather or air if available
    air_conditions: str | None = None