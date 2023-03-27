import streamlit as st
import openai


def show_messages(text):
    messages_str = [
        f"{_['role']}: {_['content']}" for _ in st.session_state["messages"][1:]
    ]
    text.text_area("Messages", value=str("\n\n".join(messages_str)), height=400)

BASE_PROMPT = [{"role": "system", "content": "You are a helpful assistant."}];

if "messages" not in st.session_state:
    st.session_state["messages"] = BASE_PROMPT;

st.set_page_config(page_title="GPT-4 API Web App")

st.title("GPT-4 API Web App")

api_key = st.text_input("请输入您的 OpenAI API Key");
openai.api_key = api_key

prompt = st.text_input("请输入您想要提问的问题")

if st.button("生成回答"):
    if api_key.strip() == "":
        st.error("请输入您的 OpenAI API Key。")
    else:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4", messages=st.session_state["messages"]
            )
            message_response = response["choices"][0]["message"]["content"]
            st.session_state["messages"] += [
                {"role": "system", "content": message_response}
            ]
            st.write("GPT-4 的回答：", answer)
        except Exception as e:
            st.error(f"出现错误：{e}")
if st.button("Clear"):
    st.session_state["messages"] = BASE_PROMPT
text = st.empty()
show_messages(text)