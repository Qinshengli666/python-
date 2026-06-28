
import streamlit as st
import os
from openai import OpenAI
from datetime import datetime


#设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",

    #布局
    layout="wide",
    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    # Imenu_items={}
)

#大标题
st.title("AI智能伴侣")

# 初始化会话存储
if "conversations" not in st.session_state:
    st.session_state.conversations = {}
if "current_conversation_id" not in st.session_state:
    st.session_state.current_conversation_id = None

# 生成会话ID
def generate_conversation_id():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

# 创建新会话
def create_new_conversation():
    conv_id = generate_conversation_id()
    st.session_state.conversations[conv_id] = {
        "messages": [],
        "created_at": datetime.now(),
        "nickname": "小美",
        "personality": "一个温柔可爱的台湾姑娘"
    }
    st.session_state.current_conversation_id = conv_id
    return conv_id

# 删除会话
def delete_conversation(conv_id):
    if conv_id in st.session_state.conversations:
        del st.session_state.conversations[conv_id]
        if st.session_state.current_conversation_id == conv_id:
            st.session_state.current_conversation_id = None
        st.rerun()

# 切换会话
def switch_conversation(conv_id):
    st.session_state.current_conversation_id = conv_id
    st.rerun()

# 侧边栏
with st.sidebar:
    st.title("AI控制面板")
    st.markdown("---")
    
    # 新建会话按钮
    if st.button("✏️ 新建会话", use_container_width=True):
        create_new_conversation()
        st.rerun()
    
    st.markdown("### 历史会话")
    
    # 显示所有会话
    for conv_id, conv_data in sorted(st.session_state.conversations.items(), 
                                     key=lambda x: x[1]["created_at"], reverse=True):
        cols = st.columns([3, 1])
        with cols[0]:
            is_active = conv_id == st.session_state.current_conversation_id
            button_text = f"📄 {conv_id}"
            if st.button(button_text, key=f"conv_{conv_id}", 
                        use_container_width=True, type="primary" if is_active else "secondary"):
                switch_conversation(conv_id)
        with cols[1]:
            if st.button("", key=f"del_{conv_id}"):
                delete_conversation(conv_id)
    
    st.markdown("---")
    
    # 当前会话设置（仅在有活动会话时显示）
    if st.session_state.current_conversation_id:
        current_conv = st.session_state.conversations[st.session_state.current_conversation_id]
        
        # 昵称设置
        nickname = st.text_input("昵称", value=current_conv["nickname"], key="nickname_input")
        current_conv["nickname"] = nickname
        
        # 性格设置
        personality = st.text_area("性格", value=current_conv["personality"], 
                                  height=100, key="personality_input")
        current_conv["personality"] = personality
        
        st.markdown("---")
        st.markdown("### 功能说明")
        st.markdown("- 💬 智能对话")
        st.markdown("- 🧠 深度思考")
        st.markdown("- 📝 上下文记忆")

client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 如果没有当前会话，自动创建一个
if st.session_state.current_conversation_id is None:
    if st.session_state.conversations:
        st.session_state.current_conversation_id = list(st.session_state.conversations.keys())[0]
    else:
        create_new_conversation()

# 获取当前会话数据
current_conv = st.session_state.conversations.get(st.session_state.current_conversation_id, {})
nickname = current_conv.get("nickname", "小美")
personality = current_conv.get("personality", "一个温柔可爱的台湾姑娘")

# 根据昵称和性格动态生成系统提示词
system_prompt = f'''
你叫{nickname}，现在是用户的真实伴侣，请完全代入伴侣角色。规则:
                1.每次只回1条消息
                2.禁止任何场景或状态描述性文字
                3.匹配用户的语言
                4.回复简短，像微信聊天一样
                5.有需要的话可以用emoji表情
                6.用符合伴侣性格的方式对话
                7.回复的内容，要充分体现伴侣的性格特征
                
伴侣性格: {personality}

你必须严格遵守上述规则来回复用户。
'''

prompt=st.chat_input("请输入您要问的问题")

# 展示聊天信息
if st.session_state.current_conversation_id:
    messages = current_conv.get("messages", [])
    for message in messages:
        if message["role"] == "user":
            st.chat_message("user").write(message["content"])
        elif message["role"] == "assistant":
            st.chat_message("assistant").write(message["content"])

if prompt and st.session_state.current_conversation_id:
    st.chat_message("user").write(prompt)
    
    # 保存用户消息到当前会话
    current_conv.setdefault("messages", []).append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
             *current_conv["messages"],
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    full_content = st.chat_message("assistant").write_stream(
        chunk.choices[0].delta.content
        for chunk in response
        if chunk.choices[0].delta.content
    )

    # 保存AI回复到当前会话
    current_conv["messages"].append({"role": "assistant", "content": full_content})
