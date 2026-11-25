# 《Flipped long》頭 30 分鐘 — 技術分析科目

本地離線科目網站，亦可以用 Streamlit Community Cloud 開一個 `https://*.streamlit.app` 網址。喺呢個 repo 嘅路徑係 `study/flipped-long-first-30/`。GitHub 網頁只會顯示檔案內容，唔會當網站跑；本 repo 未開 GitHub Pages，呢份改動亦唔會開 Pages。

## 離線靜態版

Clone 或下載之後，用瀏覽器打開 `study/flipped-long-first-30/index.html`（或進入資料夾後打開 `index.html`）即可，無需伺服器、無需上網（「觀看直播片段」連結除外）。

## Streamlit

教學內容同靜態版相同：科目目錄，加六科（大市同半導體、加密 EMA、SOXX 週線、MSTR、市況判斷、平掉金銀淡倉）。圖用呢個資料夾入面現有嘅註解圖同原畫面。後半段未收錄；之後可以加落 `study_content.py` 嘅 `SECOND_HALF`。

本機（喺 repo 根目錄）：

```bash
pip install -r study/flipped-long-first-30/requirements.txt
streamlit run study/flipped-long-first-30/streamlit_app.py
```

需要 Python 3.11 或更新（`streamlit==1.67.0`）。

### Community Cloud（share.streamlit.io）

Deploy 時揀：

- Repository: `kinaoc-ui/train`
- Branch: `cursor/flipped-long-first-30-study-2ca8`（呢個 PR 未 merge）。Merge 之後同一路徑會喺 `main`，可以改跟 `main`。
- Main file path: `study/flipped-long-first-30/streamlit_app.py`
- Python dependencies: `study/flipped-long-first-30/requirements.txt`（同 entrypoint 同一個資料夾，Community Cloud 會用呢份）

App URL 由 Community Cloud 喺 deploy 時先定，空白 subdomain 會變成 `https://…streamlit.app`。唔使 secrets。免費版閒置一陣會瞓着，再開一次就會醒。

## 直播

- Martin Luk《Flipped long》，2026年11月4日
- 本站只涵蓋開頭約 30 分鐘入面有技術分析嘅段落
- 圖上中文註解係之後加上嘅讀圖說明，可用「原畫面」對返未加字嘅截圖
- 呢份係教育拆解，唔係投資建議

## 科目（按時間）

1. `market-semis.html` — 大市同半導體檢查（03:18–03:42）
2. `crypto-ema.html` — 加密：undercutting rally（06:52–06:59）
3. `soxx-weekly.html` — 半導體淡倉同週線 50 EMA（07:59–08:11）
4. `mstr.html` — MSTR：等收市、兩邊都可以（08:43–09:13）
5. `market-condition.html` — 市況判斷：反彈仍在跌勢入面（22:43–24:19）
6. `gold-silver.html` — 平掉金銀淡倉 — 形態與位置（非預測）（27:37–29:38）

## 資料夾

- `index.html` — 靜態科目目錄（離線入口）
- `streamlit_app.py` — Community Cloud 入口
- `study_content.py` — Streamlit 用嘅科目內容；後半段加喺 `SECOND_HALF`
- `requirements.txt` — `streamlit==1.67.0`
- `.streamlit/config.toml` — 深色主題（跟 entrypoint，優先於 repo 根目錄設定）
- `styles.css`、`script.js` — 靜態版
- `images/` — 金銀科截圖；各新科目喺對應子資料夾，含註解圖同原畫面
- `fonts/` — Noto Sans CJK TC 子集（SIL Open Font License，見 `fonts/OFL.txt`）
