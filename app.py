import streamlit as st

st.title("私の初めてのWebアプリ")

# ユーザー入力を受け取る
name = st.text_input("お名前を教えてください")

# スライダーを作る
age = st.slider("年齢", 0, 100, 25)

# ボタンを押した時の動作
if st.button("挨拶する"):
    st.write(f"こんにちは、{name}さん！{age}歳なんですね。")
