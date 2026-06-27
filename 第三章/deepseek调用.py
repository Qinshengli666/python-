# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# 创建大模型交互         创建 DEEPSEEK_API_KEY 环境变量 保存key
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")
# 创建大模型交互 
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你叫小Q"},
        {"role": "user", "content": "给我讲个故事"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)