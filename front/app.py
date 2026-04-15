import streamlit as st
import requests
import pandas as pd

st.title("RC計算機能")
st.write("csvファイル形式でアップロードされた野球の打者成績に関してRCを計算してその結果を返します")

uploadfile = st.file_uploader("ファイルを選択してください", type="csv")

if uploadfile is not None:
    file = {'file': (uploadfile.name, uploadfile.getvalue(), "text/csv")}
    r = requests.post("http://127.0.0.1:8000/uploadfile", files=file)
    if r.status_code == 200:
        st.success("ファイルの読み込みに成功")
        data = r.json()
        df_res = pd.DataFrame(data)
    else:
        st.error("ファイルの読み込みに失敗")
