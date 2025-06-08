import streamlit as st

st.set_page_config(page_title="蔚之的 Streamlit 项目合集", layout="centered")

st.title("🌟 蔚之的 Streamlit 项目合集")
st.write("从0到1，女生自学编程的实践记录。")

st.markdown("## 🧭 项目目录")
st.markdown("""
| 项目名称 | 在线体验 | GitHub源码 | 简介 |
|----------|-----------|-------------|------|
| ✨ 星座生日助手 | [体验](https://star-sign-apper-avt8eedi7zvixprfee3ujz.streamlit.app/) | [源码](https://github.com/xuelengmei/star-sign-helper) | 输入生日或星座，查看信息 |
| 🧠 性格关键词匹配 | [体验](https://zodiac-keyword-matcher-6nuauhueclxrcrhakn2yjz.streamlit.app/) | [源码](https://github.com/xuelengmei/zodiac-keyword-matcher) | 输入关键词找对应星座 |
| 💰 小小记账本 | [体验](https://simple-expense-tracker-ighvertj3gb9s6ubeuj96h.streamlit.app/) | [源码](https://github.com/xuelengmei/simple-expense-tracker) | 自动统计收支和余额 |
| ⏳ 倒计时  |  [体验](https://countdown-fzwswua3ujzkavtrxnr2oy.streamlit.app/)  |  [源码](https://github.com/xuelengmei/countdown)  |  多页面，多记录，可删除  |
""", unsafe_allow_html=True)


st.markdown("## 📮 联系我")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("**💬 知乎**")
    st.markdown("[蔚之（编程小白版）](https://www.zhihu.com/people/--60-78-49-55)")
with col2:
    st.markdown("**☁️ GitHub**")
    st.markdown("[🌟 蔚之的项目合集主页](https://github.com/xuelengmei/streamlit-projects)")

with col3:
    st.markdown("**☁️ Streamlit Cloud**")
    st.markdown("[🌟蔚之的项目合集主页](https://app-projects-2aks65rdn9xhklwwvirdo6.streamlit.app/)")
with col4:
    st.markdown("**🎀 小红书**")
    st.markdown("注册中，敬请期待~")

