import streamlit as st
import requests
import pandas as pd
import os

st.title("RC計算機能")
st.write("csvファイル形式でアップロードされた野球の打者成績に関してRCを計算してその結果を返します")

uploadfile = st.file_uploader("ファイルを選択してください", type="csv")
API_URL = os.getenv("API_URL")

if uploadfile is not None:
    file = {'file': (uploadfile.name, uploadfile.getvalue(), "text/csv")}
    r = requests.post(API_URL, files=file)
    if r.status_code == 200:
        st.success("ファイルの読み込みに成功")
        data = r.json()
        df_res = pd.DataFrame(data)
        st.dataframe(df_res)
    else:
        st.error("ファイルの読み込みに失敗")
