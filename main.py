import streamlit as st
import pandas as pd

st.set_page_config(page_title="TikTokダッシュボード", layout="wide")
st.title("📱 TikTokトレンド動画ダッシュボード")

data = pd.DataFrame({
    "タイトル": ["面白い猫", "ダンスチャレンジ", "バズレシピ"],
    "動画URL": [
        "https://www.tiktok.com/@catlover/video/7324922347829036290",
        "https://www.tiktok.com/@dancer123/video/7293874382734982816",
        "https://www.tiktok.com/@cookmania/video/7283847398273849238"
    ]
})

st.subheader("🎬 トレンド動画一覧")
st.dataframe(data)

# 一時的に埋め込みをオフにして表示確認
st.write("（TikTok埋め込み表示は一時的にオフにしています）")
