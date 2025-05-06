import streamlit as st
import pandas as pd

st.set_page_config(page_title="TikTokダッシュボード", layout="wide")
st.title("📱 TikTokトレンド動画ダッシュボード")

# 任意の動画URLとタイトル（埋め込みできない動画も含んでOK）
data = pd.DataFrame({
    "タイトル": ["犬のお散歩", "NBAハイライト", "削除された動画", "非公開動画テスト"],
    "動画URL": [
        "https://www.tiktok.com/@scout2015/video/6718335390845095173",
        "https://www.tiktok.com/@nba/video/7228769842417272069",
        "https://www.tiktok.com/@someone/video/0000000000000000000",
        "https://www.tiktok.com/@privateuser/video/1111111111111111111"
    ]
})

st.subheader("🎞 一覧から動画を確認（リンク＋サムネイル風UI）")

# TikTok動画リンクをカード風に表示
cols = st.columns(2)

for i, row in data.iterrows():
    with cols[i % 2]:
        st.markdown(f"**{row['タイトル']}**")

        # TikTok動画URLから動画IDを抽出
        video_id = row["動画URL"].split("/")[-1]

        # サムネイル画像は取得不可なため、代替でロゴ＋リンクに
        st.markdown(f"""
        <div style='
            border:1px solid #ddd;
            border-radius: 10px;
            padding: 16px;
            margin-bottom: 20px;
            text-align:center;
            background-color:#fafafa;
        '>
            <img src='https://upload.wikimedia.org/wikipedia/commons/0/09/TikTok_logo.svg' width='60'><br><br>
            <a href='{row["動画URL"]}' target='_blank' style='
                font-size: 16px;
                background-color:#fe2c55;
                color: white;
                padding: 8px 16px;
                border-radius: 5px;
                text-decoration: none;
                font-weight: bold;
            '>TikTokで見る</a>
        </div>
        """, unsafe_allow_html=True)
