import streamlit as st
import pandas as pd

st.set_page_config(page_title="TikTokダッシュボード", layout="wide")
st.title("📱 TikTokトレンド動画ダッシュボード")

# ✅ 埋め込み再生が確認できた公開動画のみを使用
data = pd.DataFrame({
    "タイトル": ["犬のお散歩", "NBAハイライト", "TikTok公式紹介"],
    "動画URL": [
        "https://www.tiktok.com/@scout2015/video/6718335390845095173",
        "https://www.tiktok.com/@nba/video/7228769842417272069",
        "https://www.tiktok.com/@tiktok/video/6807491984882765061"
    ]
})

st.subheader("▶️ TikTok動画ビューア（埋め込み再生）")

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
