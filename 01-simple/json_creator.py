import json

### loading to .json
data = {
    ### model section
    "model_name": "gpt_oss_20b",
    "api_key": "Not_needed_in_LMstudio",
    "temperature": 0.5,
    "max_token": 1000,
    "timeout": 10,
    "max_retries": 3,
    "base_url": "http://127.0.0.1:1234",

}

with open("cfig.json", "w+") as f:
    json.dump(data, f, indent=4, )
