import streamlit as st
import pandas as pd

st.set_page_config(page_title="TikTok再生保証ダッシュボード", layout="wide")
st.title("📱 TikTok再生保証ダッシュボード")

# ✅ 表示する動画リスト（ここに自由に動画を追加できます）
videos = [
    {
        "title": "Z世代向けダンス",
        "url": "https://sns-smovie.wata-material.workers.dev/video1.mp4"
    },
    {
        "title": "料理トレンド：夜食レシピ",
        "url": "https://sns-smovie.wata-material.workers.dev/video2.mp4"
    },
    {
        "title": "エンタメ系チャレンジ動画",
        "url": "https://sns-smovie.wata-material.workers.dev/video3.mp4"
    }
]

# ✅ 2列カード表示（タイトル＋動画）
cols = st.columns(2)
for i, video in enumerate(videos):
    with cols[i % 2]:
        st.markdown(f"### {video['title']}")
        st.video(video['url'])
