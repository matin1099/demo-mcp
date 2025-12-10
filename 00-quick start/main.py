from agentic_model import agent_model
from tools import Context


config = {"configurable": {"thread_id": "1"}}

messages_dict = {"messages": [
    {"role":
         "user",
     "content":
         "what is the weather outside in Florida?"}  # import your text
]
}

# print(agent_model.invoke(messages_dict,
#                    config=config,
#                    context=Context(user_id="1")))

for chunk in agent_model.stream(messages_dict,
        config=config,
        context=Context(user_id="1")
        , stream_mode="values"):
    # Each chunk contains the full state at that point
    latest_message = chunk["messages"][-1]
    if latest_message.content:
        print(f"Agent: {latest_message.content}")
    elif latest_message.tool_calls:
        print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")