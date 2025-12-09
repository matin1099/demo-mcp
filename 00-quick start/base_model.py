from langchain_openai import ChatOpenAI


def base_model():
    model = ChatOpenAI(
    model="qwen3",
    base_url="http://localhost:1234/v1",
    api_key="not-needed",
    timeout=10,
    max_tokens=1000
    )
    return model
