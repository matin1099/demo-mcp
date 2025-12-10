from langchain_openai import ChatOpenAI


def create_base_model():
    model = ChatOpenAI(
    model="gpt-oss-20b",
    base_url="http://localhost:1234/v1",
    api_key="not-needed",
    timeout=10,
    max_tokens=1000
    )
    return model
