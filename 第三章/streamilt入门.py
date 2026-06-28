import streamlit as st

# 标题

st.title("streamlit入门演示")

st.header("一级标题")

st.subheader("二级标题")


#段落

st.write('1222222333333333333444444444555555555555')

# 图片
st.image("第三章/resources/111.png")

    # # 音频
    # st.audio("")
    #
    # # 视频
    # st.video("")
# log
st.logo('第三章/resources/111.png')

# 表格

st_data = {

    '姓名': ['张三','李四','王五'],
    '性别': ['男','女','男'],
    '分数': ['100','100','100']
}

st.table(st_data)


# 输入框

text = st.text_input("输入")

st.write("输入的是：" ,text)