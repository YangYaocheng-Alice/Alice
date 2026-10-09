from openai import OpenAI

client = OpenAI(
    api_key="你的Key",
    base_url="https://api.deepseek.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "把你想问的替换这段字，别删引号"}
    ]
)

print(response.choices[0].message.content)