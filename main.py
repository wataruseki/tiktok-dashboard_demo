import streamlit as st
import pandas as pd

st.set_page_config(page_title="TikTokダッシュボード", layout="wide")
st.title("📱 TikTokトレンド動画ダッシュボード")

# 動画データ
data = pd.DataFrame({
    "タイトル": ["面白い猫", "ダンスチャレンジ", "バズレシピ"],
    "動画URL": [
        "https://www.tiktok.com/@catlover/video/7324922347829036290",
        "https://www.tiktok.com/@dancer123/video/7293874382734982816",
        "https://www.tiktok.com/@cookmania/video/7283847398273849238"
    ]
})

# 表示タイトル
st.subheader("▶️ TikTok動画ビューア（埋め込み再生）")

# 動画埋め込みループ
for i, row in data.iterrows():
    st.markdown(f"### {row['タイトル']}")
    video_id = row["動画URL"].split("/")[-1]
    st.markdown(f"""
        <iframe src="https://www.tiktok.com/embed/v2/{video_id}"
                width="325" height="575" frameborder="0"
                allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
        <br><br>
    """, unsafe_allow_html=True)
