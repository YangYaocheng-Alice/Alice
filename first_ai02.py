from openai import OpenAI

with open("my-data/about_me.txt", "r", encoding="utf-8") as f:
    about_me = f.read()#这里是在读我在Alice文件里新放的文件夹，里面包含我的个人信息，这样就不用写在代码上了

client = OpenAI(
    api_key="你的Key",
    base_url="https://api.deepseek.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": about_me},#背景系统直接读上面的文件
        {"role": "user", "content": "你的提问"}
    ]
)

print(response.choices[0].message.content)