import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="TikTokダッシュボード", layout="wide")
st.title("📱 TikTokトレンド動画ダッシュボード")

# 表示する動画データ（好きに増やせます）
data = pd.DataFrame({
    "タイトル": ["犬のお散歩", "NBAハイライト", "削除された動画", "非公開動画テスト"],
    "動画URL": [
        "https://www.tiktok.com/@scout2015/video/6718335390845095173",
        "https://www.tiktok.com/@nba/video/7228769842417272069",
        "https://www.tiktok.com/@someone/video/0000000000000000000",
        "https://www.tiktok.com/@privateuser/video/1111111111111111111"
    ]
})

st.subheader("🎥 TikTok動画一覧（自動埋め込み＋失敗時リンク）")

# 2列レイアウト
cols = st.columns(2)

for i, row in data.iterrows():
    with cols[i % 2]:
        st.markdown(f"**{row['タイトル']}**")

        try:
            # oEmbed APIでHTML埋め込み取得
            oembed_url = f"https://www.tiktok.com/oembed?url={row['動画URL']}"
            response = requests.get(oembed_url, timeout=5)
            if response.status_code == 200 and "html" in response.json():
                embed_html = response.json()["html"]
                st.components.v1.html(embed_html, height=600)
            else:
                raise Exception("埋め込み失敗")
        except:
            # 埋め込みできない場合はリンクカード式にフォールバック
            st.markdown(f"""
            <div style='
                border:1px solid #ddd;
                border-radius: 10px;
                padding: 16px;
                margin-bottom: 20px;
                text-align:center;
                background-color:#f9f9f9;
            '>
                <div style="font-size:50px;">🎬</div>
                <a href='{row["動画URL"]}' target='_blank' style='
                    font-size: 16px;
                    background-color:#fe2c55;
                    color: white;
                    padding: 8px 16px;
                    border-radius: 5px;
                    text-decoration: none;
                    font-weight: bold;
                    display: inline-block;
                    margin-top: 10px;
                '>TikTokで見る</a>
            </div>
            """, unsafe_allow_html=True)
