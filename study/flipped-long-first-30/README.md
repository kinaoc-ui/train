# 技術分析科目

本地離線科目網站，亦可以用 Streamlit Community Cloud 開一個 `https://*.streamlit.app` 網址。喺呢個 repo 嘅路徑係 `study/flipped-long-first-30/`。GitHub 網頁只會顯示檔案內容，唔會當網站跑；本 repo 未開 GitHub Pages，呢份改動亦唔會開 Pages。

## 離線靜態版

Clone 或下載之後，用瀏覽器打開 `study/flipped-long-first-30/index.html`（或進入資料夾後打開 `index.html`）即可，無需伺服器、無需上網（「觀看直播片段」連結除外）。

## Streamlit

教學內容同靜態版相同。第一屏係直播目錄，按日期揀一場；而家有 2026年11月4日《Flipped long》、2026年11月3日《Adding shorts again》，同 2026年11月2日《DRAM fat finger》，最新日期排前。入去之後先至係嗰一場嘅科目，按時間順序一齊列，唔分組。圖用呢個資料夾入面現有嘅註解圖同原畫面。`study_content.py` 用 `STREAMS` 加新日期；11月4日嘅科目仍然由 `FIRST_HALF` 同 `SECOND_HALF` 拼出，11月3日嘅科目喺 `stream_2026_11_03.py`，11月2日嘅科目喺 `stream_2026_11_02.py`。

本機（喺 repo 根目錄）：

```bash
pip install -r study/flipped-long-first-30/requirements.txt
streamlit run study/flipped-long-first-30/streamlit_app.py
```

需要 Python 3.11 或更新（`streamlit==1.67.0`）。

### Community Cloud（share.streamlit.io）

Deploy 時揀：

- Repository: `kinaoc-ui/train`
- Branch: `main`
- Main file path: `study/flipped-long-first-30/streamlit_app.py`
- Python dependencies: `study/flipped-long-first-30/requirements.txt`（同 entrypoint 同一個資料夾，Community Cloud 會用呢份）

App URL 由 Community Cloud 喺 deploy 時先定，空白 subdomain 會變成 `https://…streamlit.app`。唔使 secrets。免費版閒置一陣會瞓着，再開一次就會醒。

## 直播

- Martin Luk《Flipped long》，2026年11月4日（約 1:04:14）
- Martin Luk《Adding shorts again》，2026年11月3日（約 2:35:48）
- Martin Luk《DRAM fat finger》，2026年11月2日（約 2:23:38）
- 本站收錄呢三場入面有技術分析嘅段落
- 圖上中文註解係之後加上嘅讀圖說明，可用「原畫面」對返未加字嘅截圖
- 呢份係教育拆解，唔係投資建議

## 導覽

- `index.html` — 直播目錄。先揀日期，最新排前。
- `2026-11-04.html` — 2026年11月4日《Flipped long》嘅科目，按時間順序。
- `2026-11-03.html` — 2026年11月3日《Adding shorts again》嘅科目，按時間順序。
- `2026-11-02.html` — 2026年11月2日《DRAM fat finger》嘅科目，按時間順序。

## 科目（2026年11月4日，按時間）

1. `market-semis.html` — 大市同半導體檢查（03:18–03:42）
2. `crypto-ema.html` — 加密：undercutting rally（06:52–06:59）
3. `soxx-weekly.html` — 半導體淡倉同週線 50 EMA（07:59–08:11）
4. `mstr.html` — MSTR：等收市、兩邊都可以（08:43–09:13）
5. `market-condition.html` — 市況判斷：反彈仍在跌勢入面（22:43–24:19）
6. `gold-silver.html` — 平掉金銀淡倉 — 形態與位置（非預測）（27:37–29:38）
7. `fade-cover.html` — 回顧：淡倉本應喺今日低位多平一啲（31:06–32:37）
8. `gold-21.html` — 唔好喺日線第一次碰到 21 就淡黃金（33:29–35:29）
9. `crwd-thesis.html` — Crowd long：相對強勢同 undercut-reclaim（36:21–39:41）
10. `crwd-entry.html` — Crowd 入場：1 分鐘突破、回踩上升 9（43:59–45:25）
11. `coin-crypto.html` — COIN long 同加密：位置同市場動能（48:03–50:31）
12. `tsla.html` — Tesla：週線均線聚合同多年底（51:10–52:23）
13. `choppy-cover.html` — 市況仍然偏亂：短線淡倉或應平一啲（57:59–1:00:15，並附 1:02:23–1:03:58 收結）

## 科目（2026年11月3日，按時間）

1. `igv-qqq.html` — 軟件轉弱同廣度憂慮（06:07–09:11）
2. `lite-stage.html` — LITE 階段三轉四（09:29–10:04）
3. `iwm-emas.html` — Russell 喺均線附近（11:31–11:39）
4. `soxx-weekly-50.html` — 半導體週線 50 EMA 支持（12:58–13:16）
5. `oil-cover.html` — 原油小時 9 EMA cover（13:50–14:14）
6. `sk-hynix.html` — SK Hynix 淡倉同指數延伸（20:30–21:56，其後 28:06、34:43–35:10、1:08:44–1:11:22）
7. `mstr-short.html` — MSTR 都可以係淡，但有少少向下延伸（23:30–24:14）
8. `be-gap.html` — BE 行向未補缺口、稍高過下降 9（25:23–25:36）
9. `axti-snapback.html` — AXTI 大陰線後急彈（1:16:57–1:19:14）
10. `aehr-thesis.html` — AEHR 今日太強，更好淡嘅位置（1:20:54–1:21:57）
11. `uvxy-risk.html` — UVXY 急升後淡倉風險（1:40:10–1:41:50）
12. `pltr-longs.html` — Palantir 有人睇杯柄，但佢而家唔想做多（1:45:52–1:46:40）
13. `qqq-hhhl.html` — 即使創新高都可以喺阻力／日線 9 附近淡（2:06:28–2:07:52）
14. `soxs-earnings.html` — SOXS 同業績風險（2:08:14–2:10:25）
15. `aehr-entry.html` — AEHR 入場拆解（2:11:11–2:18:41）
16. `spcx.html` — SPCX／太空股淡倉結構（2:19:29–2:21:40）
17. `avwap.html` — Anchor VWAP 跨週期，SK Hynix IPO 為例（2:21:58–2:28:50）
18. `sndk-coin.html` — 平倉：SNDK 同 COIN，淡倉傾向喺弱勢／低開平（2:29:51–2:31:49）

## 科目（2026年11月2日，按時間）

1. `leader-scan.html` — 週末 leader scan 同領先板塊（05:08–15:17）
2. `crwd-potential.html` — Tesla、Crowd 做多要等大市再延伸（16:05–17:58）
3. `soxx-gap-ups.html` — 半導體淡倉：三日裂口入下降均線（21:15–23:31）
4. `soxx-thursday.html` — 週四半導體淡倉：等彈入缺口同小時 9（23:37–27:38）
5. `usoil-cover.html` — 原油急跌：已到 21，等反彈再走（28:28–30:22）
6. `goog-indices.html` — GOOG 超賣，但指數未夠延伸（33:00–36:56）
7. `why-this-dip.html` — 點解今次同早前回調唔同（37:35–49:12）
8. `profit-taking.html` — 平倉：COIN、半導體同 memory（49:35–51:05）
9. `weekly-50-shorts.html` — 仲在週線 50 之上，淡倉唔想擺太長（52:47–56:13）
10. `dram-fat-finger.html` — DRAM fat finger：誤用賣出止蝕（1:00:26–1:06:18）
11. `sedg-fslr.html` — 太陽能：較想淡近週線 9（1:07:27–1:08:18）
12. `spcx-swing.html` — SPCX 或會擺耐少少，但仍怕 V 型反彈（1:10:12–1:11:41）
13. `xag-xau.html` — 金銀：銀已到週線 150，金仍在上面（1:12:10–1:14:32）
14. `defensive-extended.html` — 防守板塊向上有少少延伸（1:16:53–1:17:57）
15. `uvxy-aggressive.html` — UVXY 理論上可做多，但太進取（1:19:32–1:19:48）
16. `tsla-fcp.html` — Tesla 多年底：要等回落到匯合均線（1:20:16–1:21:28）
17. `nvda-weekly-50.html` — NVDA 偏弱，做多要小心週線 50（1:27:01–1:28:54）
18. `btc-hold-21.html` — Bitcoin：守得住週線 21 先考慮做多（1:52:34–1:54:13）
19. `lite-failed.html` — LITE：失敗突破後行向 150 之下（2:08:31–2:09:32）
20. `afrm-breakout.html` — AFRM：日線同週線突破都整齊（2:10:27–2:10:43）
21. `hold-shorts.html` — 強彈入未補缺口，但仍會持有淡倉（2:17:20–2:18:26）
22. `usoil-exit.html` — 原油：或等小時 9 反抽，否則彈就賣（2:18:29–2:19:54）
23. `hynix-bounce.html` — SK hynix 可淡，但大市已有少少延伸（2:20:25–2:23:28）

## 資料夾

- `index.html` — 直播目錄（離線入口，先揀日期）
- `2026-11-04.html` — 2026年11月4日《Flipped long》嘅科目目錄
- `2026-11-03.html` — 2026年11月3日《Adding shorts again》嘅科目目錄
- `2026-11-02.html` — 2026年11月2日《DRAM fat finger》嘅科目目錄
- `streamlit_app.py` — Community Cloud 入口
- `study_content.py` — Streamlit 用嘅科目內容。`STREAMS` 係日期目錄（最新排前）；11月4日科目由 `FIRST_HALF` 同 `SECOND_HALF` 拼成一條時間順序，11月3日科目喺 `stream_2026_11_03.py`，11月2日科目喺 `stream_2026_11_02.py`
- `stream_2026_11_03.py` — 2026年11月3日《Adding shorts again》嘅科目內容
- `stream_2026_11_02.py` — 2026年11月2日《DRAM fat finger》嘅科目內容
- `requirements.txt` — `streamlit==1.67.0`
- `.streamlit/config.toml` — 深色主題（跟 entrypoint，優先於 repo 根目錄設定）
- `styles.css`、`script.js` — 靜態版
- `images/` — 各科目喺對應子資料夾，含註解圖同原畫面
- `fonts/` — Noto Sans CJK TC 子集（SIL Open Font License，見 `fonts/OFL.txt`）
