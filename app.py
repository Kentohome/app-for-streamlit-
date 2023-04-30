import streamlit as st
import pandas as pd
import numpy as np
import sqlite3 
import hashlib


conn = sqlite3.connect('database.db')
c = conn.cursor()


import hashlib
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False
def create_user():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_user(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def main():
    st.title("ログイン機能テスト")
    menu = ["ホーム","ログイン","サインアップ"]
    choice = st.sidebar.selectbox("メニュー",menu)
    if choice == "ホーム":
        st.subheader("ホーム画面です")
    elif choice == "ログイン":
        st.subheader("ログイン画面です")
        username = st.sidebar.text_input("ユーザー名を入力してください")
        password = st.sidebar.text_input("パスワードを入力してください",type='password')
        if st.sidebar.checkbox("ログイン"):
            create_user()
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password,hashed_pswd))
            print('result',result)
            if result:
                st.success("{}さんでログインしました".format(username))      
            else:
                st.warning("ユーザー名かパスワードが間違っています")
            if result[0][2]:
                st.write(f'あなたの権限は{result[0][2]}です')
                st.subheader('折れ線グラフ')
                chart_data = pd.DataFrame(
                np.random.randn(7, 3),
                columns=['a', 'b', 'c'])
                st.line_chart(chart_data)
                st.dataframe(chart_data)
    elif choice == "サインアップ":
        st.subheader("新しいアカウントを作成します")
        new_user = st.text_input("ユーザー名を入力してください")
        new_password = st.text_input("パスワードを入力してください",type='password')
        if st.button("サインアップ"):
            create_user()
            add_user(new_user,make_hashes(new_password))
            st.success("アカウントの作成に成功しました")
            st.info("ログイン画面からログインしてください")
if __name__ == '__main__':
    main()