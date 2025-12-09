from agentic_model import agent
from tools import Context
agent = agent
config = {"configurable": {"thread_id": "1"}}

messages_dict = {"messages":                    [
                        {"role":
                          "user",
                         "content":
                          "what is the weather outside?"} # import your text
                     ]
                }

print(agent.invoke(messages_dict,
                   config=config,
                   context=Context(user_id="1") ))

