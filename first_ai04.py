# ============================================
# 第1天：跑通基础
# ============================================

from openai import OpenAI  # 把工具包拿进来用

# ============================================
# 第4天新加：读你的"记忆本"
# 为什么加：让 AI 认识你，不用每次手写背景
# ============================================

# 读 about_me.txt，存到 about_me 变量里
with open("my-data/about_me.txt", "r", encoding="utf-8") as f:
    about_me = f.read()

# 读 habits.txt，存到 habits 变量里（新加）
with open("my-data/habits.txt", "r", encoding="utf-8") as f:
    habits = f.read()

# 读 learning_log.txt，存到 learning_log 变量里（新加）
with open("my-data/learning_log.txt", "r", encoding="utf-8") as f:
    learning_log = f.read()

# 读 thoughts.txt，存到 thoughts 变量里（新加）
with open("my-data/thoughts.txt", "r", encoding="utf-8") as f:
    thoughts = f.read()
# 第6天新加：读 recent.txt，让 AI 知道最近发生了什么
with open("my-data/recents.txt", "r", encoding="utf-8") as f:
    recents = f.read()

# ============================================
# 第1天：建电话线
# ============================================

client = OpenAI(
    api_key="你的Key",           # 你的钥匙
    base_url="https://api.deepseek.com/v1"     # 打给 DeepSeek
)

# ============================================
# 第4天改：把四个文件拼起来，塞进 system
# 为什么改：以前只读 about_me，现在读全四个，AI 更懂你
# ============================================

response = client.chat.completions.create(
    model="deepseek-chat",  # 选模型
    messages=[
        # system 是背景，把五个文件的内容拼起来
        {"role": "system", "content": about_me + habits + learning_log + thoughts + recents},
        # user 是问题
        {"role": "user", "content": "我计划半年明天投入2小时学习AI，目标是做成一个能监督我的行为、主动提出改进建议的AI，提高生活质量和工作效率，这现实吗？"}
    ]
)

# ============================================
# 第1天：把回答打印出来
# ============================================

print(response.choices[0].message.content)