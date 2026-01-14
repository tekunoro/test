import streamlit as st
import random

# タイトル
st.title("デジタル自動販売機")

# 画像の準備（GitHub上の画像フォルダのパスに合わせてください）
# ※あらかじめGitHubに「image」フォルダを作って画像を入れておく必要があります
COLA = "image/コーラ.png"
TEA = "image/お茶.png"
BEER = "image/ビール.png"
MYSTERY = "image/謎かん.png"

# ボタンを横に並べるための設定
col1, col2, col3, col4 = st.columns(4)

# 初期化（飲み物が出てくる場所を空にする）
if "drink" not in st.session_state:
    st.session_state.drink = None

# 各ボタンの動作
with col1:
    st.image("image/コーラ_縦.png", caption="コーラ")
    if st.button("買う", key="btn1"):
        st.session_state.drink = COLA

with col2:
    st.image("image/お茶_縦.png", caption="お茶")
    if st.button("買う", key="btn2"):
        st.session_state.drink = TEA

with col3:
    st.image("image/ビール_縦.png", caption="ビール")
    if st.button("買う", key="btn3"):
        st.session_state.drink = BEER

with col4:
    st.image(MYSTERY, caption="お楽しみ")
    if st.button("買う", key="btn4"):
        st.session_state.drink = random.choice([COLA, TEA, BEER])

# 取り出し口の表示
st.write("---")
st.subheader("取り出し口")
if st.session_state.drink:
    st.image(st.session_state.drink, width=200)
    st.success("ガシャコン！お買い上げありがとうございます！")
