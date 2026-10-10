from openai import OpenAI

client = OpenAI(
    api_key="你的Key",
    base_url="https://api.deepseek.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你的基本信息，目标，针对这个目标你的境况，回答深度或格式等要求"},
        {"role": "user", "content": "你的提问"}
    ]
)

print(response.choices[0].message.content)