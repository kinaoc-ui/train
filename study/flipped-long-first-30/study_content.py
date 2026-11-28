"""Teaching content for the study app.

Text is copied from the static HTML pages in this folder. Do not add fill
prices, size, or P&L. FIRST_HALF is the opening 30 minutes of the 4 Nov 2026
stream. SECOND_HALF is 30:00 through the end of that stream. The 3 Nov 2026
stream lives in stream_2026_11_03.py, and the 2 Nov 2026 stream lives in
stream_2026_11_02.py, and the 28 Oct 2026 stream lives in stream_2026_10_28.py, and the 27 Oct 2026 stream lives in stream_2026_10_27.py. All five are listed in STREAMS, newest first. Each
subject uses the same keys.
"""

from __future__ import annotations

from pathlib import Path

from stream_2026_11_02 import STREAM as STREAM_2026_11_02
from stream_2026_11_03 import STREAM as STREAM_2026_11_03
from stream_2026_10_28 import STREAM as STREAM_2026_10_28
from stream_2026_10_27 import STREAM as STREAM_2026_10_27

YOUTUBE = "https://www.youtube.com/watch?v=NUT6d6Hvbmw"

HOME = {
    "id": "home",
    "eyebrow": "直播目錄",
    "title": "技術分析科目",
    "subtitle": "先揀一場直播",
    "meta": "Martin Luk",
    "summary_kicker": "概要",
    "summary_title": "按直播日期入去",
    "summary": [
        "先揀一場直播嘅日期，再睇嗰一場嘅科目。科目按時間順序排。而家收錄 2026年11月4日《Flipped long》、2026年11月3日《Adding shorts again》、2026年11月2日《DRAM fat finger》、2026年10月28日《SOXX short》，同 2026年10月27日《Strong bounce》。之後再加其他直播，只會喺呢度多一個日期，唔會把所有科目一次過列晒出嚟。",
    ],
    "notes_title": "注意事項",
    "notes": [
        "每場直播嘅圖上中文註解係之後加上嘅讀圖說明，唔係直播畫面原本已有嘅字。「原話」係英文轉寫，再附粵語對譯；「點樣讀」係說明，兩者分開。",
        "畫面睇唔到成交價、倉位大細或者損益，所以各科都唔寫死呢啲數字。",
    ],
}


FIRST_HALF: list[dict] = [
    {
        "id": "market-semis",
        "pager_name": "大市同半導體檢查",
        "when": "03:18–03:42",
        "nav": "大市同半導體檢查",
        "eyebrow": "科目一",
        "title": "大市同半導體檢查",
        "subtitle": "計劃做 long 之前，先睇市場同弱勢板塊",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 03:18–03:42",
        "watch_label": "由 03:18 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=198s",
        "summary_kicker": "概要",
        "summary_title": "計劃做 long 之前，先睇大市同弱勢板塊",
        "summary": [
            "呢一段由 03:18 開始。佢先話今日有啲趕，計劃咗一啲 potential longs，跟住結論係半導體仍然好弱。畫面先後出現 QQQ 日線同 SOXX 日線；中間佢快速翻過其他品種，但有分析意思嘅，係呢兩幅日線。",
            "圖上嘅中文註解係之後加上嘅讀圖說明，唔係直播畫面原本已有嘅字。以下「原話」同「點樣讀」分開。",
        ],
        "card": "計劃做 potential longs 之前，先睇 QQQ 日線，再睇 SOXX。佢嘅結論係半導體仍然好弱。",
        "charts": [
            {
                "anchor": "chart-qqq",
                "toc": "QQQ 日線",
                "kicker": "圖一",
                "title": "QQQ 日線：先睇大市",
                "time": "直播 03:22",
                "annotated": "images/market-semis/01_qqq_daily_0322.jpg",
                "source": "images/market-semis/src_qqq_daily_0322.jpg",
                "caption": "圖一 · QQQ 日線 · 直播 03:22。註解標示先睇大市，以及最新呢段只係反彈、仍在下跌均線之下。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 QQQ 日線圖：標示計劃做 long 之前先睇大市，大結構仍然偏跌；以及最新反彈仍在下跌均線之下。",
                "alt_source": "直播原畫面：QQQ 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "03:18–03:42 · 機器轉寫，標點為閱讀而加",
                                "en": "Today is a little bit of rush. I did plan some potential longs today. It looks like the semis is still remains like remains pretty weak. I don't know I",
                            }
                        ],
                        "yc": "今日有啲趕。我本來計劃咗今日做一啲 potential longs。睇落半導體仍然好弱。我唔知呀。",
                        "note": "「I did plan some potential longs today」出現嗰陣，畫面主要係 QQQ 日線。講 semis 仍然弱嗰陣，主要係 SOXX 日線，見下圖。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "呢一步係先睇大市。QQQ 日線高點愈嚟愈低，均線向下，最新呢段升只係反彈，價格仍在下跌均線之下。",
                            "呢啲結構觀察係讀圖說明，唔係佢逐句講出 lower highs。原話只係話計劃咗 longs，同半導體仍然弱。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-soxx",
                "toc": "SOXX 日線",
                "kicker": "圖二",
                "title": "SOXX 日線：半導體仍然好弱",
                "time": "直播 03:30",
                "annotated": "images/market-semis/02_soxx_daily_0330.jpg",
                "source": "images/market-semis/src_soxx_daily_0330.jpg",
                "caption": "圖二 · SOXX 日線 · 直播 03:30。註解標示半導體仍然好弱，以及右面呢段彈起未算轉強。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 SOXX 日線圖：標示高點愈嚟愈低、均線向下，以及最近反彈仍在均線之下、未算板塊轉強。",
                "alt_source": "直播原畫面：SOXX 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "同一段對白 · 畫面約 03:25–03:37 多次回到 SOXX",
                                "en": "It looks like the semis is still remains like remains pretty weak.",
                            }
                        ],
                        "yc": "睇落半導體仍然好弱。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "SOXX 日線同 QQQ 一樣，大結構偏弱：高點愈嚟愈低，均線向下。右面有一段彈起，但仍然喺均線之下。",
                            "佢冇講「單一次較低時間框架嘅 bounce 唔等於轉勢」呢句口訣。呢幅日線要學嘅係：有彈起，唔等於弱勢板塊已經轉強。呢句係讀圖說明，唔係原話。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "03:18 前後佢話 today is a little bit of rush，畫面確實快速翻過 BTC、HYPE、SOL 等，之後先較多次停喺 QQQ 同 SOXX。本頁只收有分析意思嘅兩幅日線，唔做翻圖圖冊。",
            "畫面睇唔到成交價、倉位大細或者損益，所以唔寫死呢啲數字。",
        ],
    },
    {
        "id": "crypto-ema",
        "pager_name": "加密 undercutting rally",
        "when": "06:52–06:59",
        "nav": "加密：undercutting rally",
        "eyebrow": "科目二",
        "title": "加密：undercutting rally",
        "subtitle": "週線 21，同埋日線 150 EMA",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 06:52–06:59",
        "watch_label": "由 06:52 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=412s",
        "summary_kicker": "概要",
        "summary_title": "佢鍾意呢段加密嘅 undercutting rally",
        "summary": [
            "06:52 至 06:59，佢話好鍾意呢段 cryptos 嘅 undercutting rally：週線 21，同埋日線 150 EMA。講呢句之前大約 06:40–06:47 畫面係 BTCUSDT.P 週線；講緊嗰陣已經切到日線。本頁用呢兩幅圖一齊讀。",
            "圖例只顯示均線數值，冇寫 21 或者 150 呢啲週期。所以註解會指住 undercut、rally，同較慢均線嘅位置，但唔會標死邊一條線就一定係 21 或者 150。",
        ],
        "card": "佢鍾意呢段加密嘅 undercutting rally：週線 21，同埋日線 150 EMA。畫面用 BTCUSDT.P 週線同日線。",
        "charts": [
            {
                "anchor": "chart-weekly",
                "toc": "週線",
                "kicker": "圖一",
                "title": "BTCUSDT.P 週線：undercut 之後嘅 rally",
                "time": "直播 06:46",
                "annotated": "images/crypto-ema/01_btcusdt_weekly_0646.jpg",
                "source": "images/crypto-ema/src_btcusdt_weekly_0646.jpg",
                "caption": "圖一 · BTCUSDT.P 週線 · 直播 06:46。註解標示 undercut 嘅低位，以及之後升返均線附近嘅 rally；佢講 weekly 21。 點圖可放大。",
                "alt_annotated": "加咗註解嘅比特幣週線圖：標示低過前低嘅 undercut，以及之後升返均線附近嘅 rally。",
                "alt_source": "直播原畫面：BTCUSDT.P 週線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "06:52–06:59 · 機器轉寫，標點為閱讀而加",
                                "en": "I really like this cryptos undercutting rally on the weekly 21 and so also the daily 150 EMA.",
                            }
                        ],
                        "yc": "我好鍾意呢段加密嘅 undercutting rally，喺週線 21，同埋日線 150 EMA。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "週線見到價格低過前低（undercut），之後先有一段升返均線附近嘅 rally。呢個就係佢講「undercutting rally on the weekly 21」嗰陣，畫面先出示嘅結構。",
                            "圖例冇寫均線週期，所以本頁唔會指住某一條顏色就肯定係 21。重點係位置同形態：undercut 之後再升返均線附近。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-daily",
                "toc": "日線",
                "kicker": "圖二",
                "title": "BTCUSDT.P 日線：同樣有下探再彈",
                "time": "直播 06:52",
                "annotated": "images/crypto-ema/02_btcusdt_daily_0652.jpg",
                "source": "images/crypto-ema/src_btcusdt_daily_0652.jpg",
                "caption": "圖二 · BTCUSDT.P 日線 · 直播 06:52。註解標示下探再彈，以及較慢均線一帶；圖例冇寫 150 週期，故此唔標死。 點圖可放大。",
                "alt_annotated": "加咗註解嘅比特幣日線圖：標示下探再彈，以及較慢均線一帶，並註明圖例冇寫 150 週期。",
                "alt_source": "直播原畫面：BTCUSDT.P 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "同一句對白 · 06:52 前後已切到日線",
                                "en": "…and so also the daily 150 EMA.",
                            }
                        ],
                        "yc": "……同埋日線 150 EMA。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "日線見到價格由高位回落，靠近較慢嘅黃線之後再彈。佢將呢段同「daily 150 EMA」一齊講。",
                            "黃線走勢較慢，數值亦接近圖例入面較低嗰條 Crypto EMA，有可能就係佢講嘅 150，但圖例冇寫週期，本頁唔當已經核實。讀呢幅圖時，重點仍然係位置：下探到較慢均線一帶再彈。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "呢一句好短，而且冇講倉位或者買賣價，本頁只拆佢指住嘅形態同均線位置。",
            "06:15 附近曾經出現 ETH 1 小時，09:00 附近亦有加密週線，但呢句對白對應嘅畫面係 BTC 週線同日線。",
        ],
    },
    {
        "id": "soxx-weekly",
        "pager_name": "週線 50 EMA",
        "when": "07:59–08:11",
        "nav": "半導體淡倉同週線 50 EMA",
        "eyebrow": "科目三",
        "title": "半導體淡倉同週線 50 EMA",
        "subtitle": "位置條件，唔係寫死嘅觸發價",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 07:59–08:11",
        "watch_label": "由 07:59 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=479s",
        "summary_kicker": "概要",
        "summary_title": "想 cover，但條件寫喺週線 50 EMA",
        "summary": [
            "07:59 至 08:11，佢話諗住 cover 自己嘅 semi short，但加咗一個條件：如果再伸延多一點、再喺週線 50 EMA 下面多一點。講呢句嗰陣，畫面係 SOXX 週線。價格就喺一條較慢嘅黃線附近，圖例數值 456.35 同呢條黃線對得上；但本頁唔會寫死觸發價，因為畫面冇見到落單票，句子亦冇講完「如果真係伸延」之後會點。",
        ],
        "card": "想 cover semi short，但加咗一個條件：如果再喺週線 50 EMA 下面伸延多一點。唔寫死觸發價。",
        "charts": [
            {
                "anchor": "chart-weekly",
                "toc": "SOXX 週線",
                "kicker": "圖一",
                "title": "SOXX 週線：50 EMA 就喺呢附近",
                "time": "直播 08:05",
                "annotated": "images/soxx-weekly/01_soxx_weekly_0805.jpg",
                "source": "images/soxx-weekly/src_soxx_weekly_0805.jpg",
                "caption": "圖一 · SOXX 週線 · 直播 08:05。註解標示週線 50 EMA 附近，以及「如果再向下伸延多一點」呢個條件位置。唔寫死觸發價。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 SOXX 週線圖：黃線附近標為週線 50 EMA，並指出若再向下伸延多一點嘅條件位置。",
                "alt_source": "直播原畫面：SOXX 週線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "07:59–08:11 · 機器轉寫，標點為閱讀而加；YouTube 自動字幕誤作 50-year may",
                                "en": "I think I will cover my semi short but if it it's going a little bit extended like a little bit more below the one the 50 EMA on the weekly",
                            }
                        ],
                        "yc": "我諗我會 cover 我嘅半導體淡倉，但如果佢再伸延多一點，再喺週線 50 EMA 下面多一點……",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "讀呢幅圖，先對位置：當時價格就喺黃線附近。圖例冇印「50」呢個字，但 456.35 呢個數值同黃線位置吻合，又係佢講緊 weekly 50 EMA 嗰陣嘅畫面，所以註解先標「就喺呢附近」。呢個係位置對讀，唔係已經核實嘅設定表。",
                            "原話係一個條件句，而且轉寫到 weekly 就停，冇清楚講如果真係再跌穿會點。所以唔好補寫觸發價、倉位或者一定會 cover。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "講呢句之前，畫面曾經出現 SOXS（3 倍淡半導體 ETF）同 SOXX 日線，但對白明確講嘅係週線 50 EMA，所以主圖用 08:05 嘅 SOXX 週線。",
            "畫面睇唔到成交價、倉位大細或者損益，所以唔寫死呢啲數字。",
        ],
    },
    {
        "id": "mstr",
        "pager_name": "MSTR",
        "when": "08:43–09:13",
        "nav": "MSTR：等收市、兩邊都可以",
        "eyebrow": "科目四",
        "title": "MSTR：等收市、兩邊都可以",
        "subtitle": "似 pullback short，但未決定今日一定要做",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 08:43–09:13",
        "watch_label": "由 08:43 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=523s",
        "summary_kicker": "概要",
        "summary_title": "似 pullback short，但今日可以兩邊都行",
        "summary": [
            "08:43 開始，畫面係 MSTR 日線。佢話而家睇落似 pullback short，多過 long；但隨即話唔肯定，想等收市，或者今日先唔做。08:46 切到 1 小時圖，之後先講 really can go both way。YouTube 自動字幕把 MSTR 誤聽成 MSTL，本頁按 Whisper 同畫面更正。",
        ],
        "card": "而家睇落似 pullback short，多過 long；但唔肯定，想等收市，或者今日先唔做。亦話 really can go both way。",
        "charts": [
            {
                "anchor": "chart-daily",
                "toc": "日線",
                "kicker": "圖一 · 主圖",
                "title": "MSTR 日線：彈升入均線附近",
                "time": "直播 08:43",
                "annotated": "images/mstr/01_mstr_daily_0843.jpg",
                "source": "images/mstr/src_mstr_daily_0843.jpg",
                "caption": "圖一 · MSTR 日線 · 直播 08:43。註解標示彈升入均線附近，似 pullback short 多過 long；但佢唔肯定，想等收市。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 MSTR 日線圖：標示彈升入均線附近，以及佢唔肯定、想等收市。",
                "alt_source": "直播原畫面：MSTR 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "08:43–09:03 · 機器轉寫，標點為閱讀而加",
                                "en": "MSTR right now looks like a pullback short instead of a long I I'm not sure I think maybe we need to wait for the close maybe not today",
                            }
                        ],
                        "yc": "MSTR 而家睇落似 pullback short，而唔係 long。我唔肯定，或者要等收市，今日可能先唔做。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "日線見到價格由低位彈升，靠近均線。佢將呢個位置讀成偏 pullback short，而唔係當做 long。",
                            "重點係後面嗰句保留：唔肯定，想等收市，或者今日先唔做。呢科要學嘅係「位置可以咁讀，但未收市可以先唔做」，唔好寫成已經落實嘅淡倉。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-1h",
                "toc": "1 小時",
                "kicker": "圖二",
                "title": "MSTR 1 小時：講緊嗰陣切到呢個週期",
                "time": "直播 08:46",
                "annotated": "images/mstr/02_mstr_1h_0846.jpg",
                "source": "images/mstr/src_mstr_1h_0846.jpg",
                "caption": "圖二 · MSTR 1 小時 · 直播 08:46。講緊嗰陣切到 1 小時，彈升靠近均線；稍後原話說 really can go both way。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 MSTR 一小時圖：標示講緊嗰陣切到 1 小時，彈升靠近均線，原話說兩邊都可以。",
                "alt_source": "直播原畫面：MSTR 一小時圖，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "08:46 已切 1 小時 · 09:10–09:13",
                                "en": "really can go both way I",
                            }
                        ],
                        "yc": "真係兩邊都可以行。",
                        "note": "「wait for the close / maybe not today」係喺日線開始講；切到 1 小時之後，先補呢句 both way。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "1 小時圖把日線嗰段彈升放大，價格靠近均線。呢幅圖適合用來理解點解佢會話兩邊都可以：向上未完，或者呢度先行回。",
                            "唔好把 1 小時圖讀成另外一個已經決定咗嘅方向。佢自己都話唔肯定。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "08:49 之後畫面開始翻加密品種，但對白仍然收束緊 MSTR 呢段。本頁唔把之後嘅翻圖算入呢科。",
            "畫面睇唔到成交價、倉位大細或者損益，所以唔寫死呢啲數字。",
        ],
    },
    {
        "id": "market-condition",
        "pager_name": "市況判斷",
        "when": "22:43–24:19",
        "nav": "市況判斷：反彈仍在跌勢入面",
        "eyebrow": "科目五",
        "title": "市況判斷：反彈仍在跌勢入面",
        "subtitle": "唔好喺 long 邊做得太進取，仲留住一啲淡倉",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 22:43–24:19",
        "watch_label": "由 22:43 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=1363s",
        "summary_kicker": "概要",
        "summary_title": "呢段可以只係跌勢入面嘅反彈",
        "summary": [
            "22:43 佢話今日交易就講到呢度；22:53 話而家只係管理倉位。之後喺 23:31 至 24:19，用 QQQ 日線做市況判斷：仍然係 choppy market，呢段可以只係另一段跌勢／調整入面嘅 bounce。所以唔會喺 long 邊做得太進取，仲留住一啲淡倉；又話或者而家可以同時做 long 同 short，睇下點。",
            "由 09:13 到 22:43 大約 13 分鐘幾乎冇對白，畫面主要係翻睇唔同股票。呢段只當作管理同覆盤，唔另外做成圖冊。23:35 嘅 QQQ 日線，就係佢講「bounce within the downtrend」嗰陣嘅主圖。",
        ],
        "card": "今日交易講完，之後係管理倉位。市況仍然 choppy，呢段可以只係跌勢／調整入面嘅 bounce；唔好喺 long 邊做得太進取，仲留住一啲淡倉。",
        "charts": [
            {
                "anchor": "chart-qqq",
                "toc": "QQQ 日線",
                "kicker": "圖一 · 主圖",
                "title": "QQQ 日線：bounce 可以仍在跌勢入面",
                "time": "直播 23:35",
                "annotated": "images/market-condition/01_qqq_daily_2335.jpg",
                "source": "images/market-condition/src_qqq_daily_2335.jpg",
                "caption": "圖一 · QQQ 日線 · 直播 23:35。註解標示大結構仍然偏跌，以及最新呢段可以只係跌勢／調整入面嘅反彈。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 QQQ 日線圖：標示高點回落、均線向下，以及右面呢段可以只係反彈，唔好當已經轉勢。",
                "alt_source": "直播原畫面：QQQ 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "22:43–23:00 · 機器轉寫，標點為閱讀而加",
                                "en": "I think um that's all that's it for my trading today. Now it's just going to manage my positions I",
                            }
                        ],
                        "yc": "我諗今日嘅交易就講到呢度。而家只係管理倉位。",
                    },
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "23:31–24:19 · 機器轉寫，標點為閱讀而加",
                                "en": "I would assume this is a this is still a choppy market and this is this could be the only the bounce of a of another downtrend of another um I mean a bounce within the within the downtrend within the correction. So I I won't like go super crazy on the long side and that's why I'm keeping some of the shorts. Maybe maybe it this is the time to go both long and short at the same time and see how how it goes um",
                            }
                        ],
                        "yc": "我當呢個仍然係一個 choppy 嘅市場。呢段可以只係另一段跌勢、另一段調整入面嘅反彈。所以我唔會喺 long 邊做得太進取，亦都因為咁先留住一啲淡倉。或者而家可以同時做 long 同 short，睇下點。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "23:31 開始講呢段市況嗰陣，畫面主要停喺 QQQ 日線。高點已經回落，均線向下，右面有一組彈起，但仍然喺下跌結構入面。呢幅圖就係「bounce within the downtrend within the correction」最直接嘅位置。",
                            "跟住呢個判斷嘅管理態度係：唔好喺 long 邊做得太進取，仲留住一啲淡倉；甚至兩邊一齊做，再睇後續。呢啲係倉位管理原則，畫面仍然睇唔到具體倉位或者損益，所以唔寫死數字。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "講緊呢段期間，畫面亦短暫切過 SPY 同其他股票，但市況判斷嘅主圖係 QQQ 日線。",
            "23:44 佢曾經把 QQQ 日線再拉遠睇更長歷史；本頁用 23:35 呢幅較清楚見到近期跌勢同反彈嘅圖做主圖。",
            "講完呢段之後，大約 26:15 開始轉去 XAUUSD，就係下一科「平掉金銀淡倉」。",
        ],
    },
    {
        "id": "gold-silver",
        "pager_name": "平掉金銀淡倉",
        "when": "27:37–29:38",
        "nav": "平掉金銀淡倉 — 形態與位置（非預測）",
        "eyebrow": "科目",
        "title": "平掉金銀淡倉",
        "subtitle": "形態與位置（非預測）",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 27:37–29:38 · 全程重播約 1:04:14",
        "watch_label": "由 27:37 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=1657s",
        "summary_kicker": "概要",
        "summary_title": "佢唔係預測黃金見底",
        "summary": [
            "佢唔係話「黃金見底所以要平」，而係指住圖上嘅位置，用形態同時間解釋點解已經 cover 金銀淡倉。雖然仲叫呢段做跌勢，但已經有向上突破；然後先平淡倉。重點係位置同形態，唔係預測後面一定升。",
            "呢個科目只涵蓋直播《Flipped long》（2026年11月4日）開頭 30 分鐘入面，大約 27:37 至 29:38 呢一段。畫面主要係 XAUUSD，之後先轉 GLD 15 分鐘。白銀雖然有講到，但呢一段冇單獨出示白銀圖。",
            "讀圖次序係：先用日線確認大結構仍然係跌勢；放大到 1 小時圖，指住大概喺邊啲 K 線 cover，並用 failed bear flag／VCP、波動收縮再擴張、同輕微 downside extension 解釋；再喺 15 分鐘圖睇清楚收縮完、未大升之前嗰段；最後用 GLD 15 分鐘更正時間——起初以為係 pre-market，隨即改口話係 overnight session，指住「probably around around here」。",
            "圖上嘅中文註解係之後加上嘅讀圖說明，方便 review；唔係直播畫面原本已有嘅字。可用每幅圖嘅「原畫面」掣，或者上面「全部顯示原畫面」，對返未加字嘅截圖。以下「原話」係英文轉寫原文，再附忠實粵語對譯；「點樣讀」係我哋嘅說明，兩者分開。",
        ],
        "card": "用位置同形態解釋點解已經 cover，而唔係預測黃金見底。呢科係原本已經完成嘅主科目。",
        "charts": [
            {
                "anchor": "chart-daily",
                "toc": "日線",
                "kicker": "圖一",
                "title": "XAUUSD 日線：確認仍然係跌勢",
                "time": "直播 27:37",
                "annotated": "images/01_xauusd_daily_2737.jpg",
                "source": "images/src_2737.jpg",
                "caption": "XAUUSD 日線，直播 27:37。註解標示「仍然喺跌勢入面：日線高點愈嚟愈低，均線向下」，同「最新呢段係反彈，未當已經轉升浪」。點圖可放大。",
                "alt_annotated": "加咗註解嘅 XAUUSD 日線圖：左邊標示仍然喺跌勢入面，日線高點愈嚟愈低、均線向下；右邊標示最新呢段係反彈，未當已經轉升浪。",
                "alt_source": "直播原畫面：XAUUSD 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "27:37 起 · 機器轉寫",
                                "en": "For gold and silver shorts I covered it at around this candle or this candle right here.",
                            }
                        ],
                        "yc": "金同銀嘅淡倉，我大概喺呢一根或者呢一根 K 線嗰度 cover 咗。",
                        "note": "呢一句喺日線仲喺畫面嗰陣已經開始講；「this candle or this candle right here」主要係放大到 1 小時圖之後先指住具體位置，完整對白見圖二。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "呢一步係用日線確認大結構仍然係跌勢：高點愈嚟愈低、均線向下。最新呢段升，係當反彈來讀，未當已經轉升浪。",
                            "呢啲結構觀察係讀圖說明，唔係佢喺呢一段逐句講出「lower highs」或者「均線向下」。原話稍後先講 「it's in a downtrend」。呢步係定位置，唔係宣布見底。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-1h",
                "toc": "1 小時",
                "kicker": "圖二 · 主圖",
                "title": "XAUUSD 1 小時：指住位置，用形態解釋點解平",
                "time": "直播 27:48",
                "annotated": "images/02_xauusd_1h_2748.jpg",
                "source": "images/src_2748.jpg",
                "caption": "XAUUSD 1 小時，直播 27:48。呢段嘅主圖。註解依佢講嘅意思標示五點：大結構仲係跌勢；輕微 downside extension；波動收縮，形態似 failed bear flag 或 VCP；向上突破／波動擴張；以及「大約喺呢一兩根 K 線 cover」——只係指位置，畫面冇見到成交價。",
                "alt_annotated": "加咗註解嘅 XAUUSD 一小時圖，按次序標示：大結構仲係跌勢、輕微向下延伸、波動收縮（形態似 failed bear flag 或 VCP）、向上突破同波動擴張，以及大約喺呢一兩根 K 線 cover。",
                "alt_source": "直播原畫面：XAUUSD 一小時圖，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "27:37–28:34 · 機器轉寫，標點為閱讀而加，用字按轉寫",
                                "en": "For gold and silver shorts I I covered it at around this candle or or this candle right here. So it I kind of feels like yeah it looks like a a failed bear flag or like a VCP, but it's um it's in it's in a downtrend but like it's breaking out to the upside. And it's just like that volatility contraction and then the expansion I together with like a little bit extension to the downside, so I just cover them.",
                            }
                        ],
                        "yc": "金同銀嘅淡倉，我大概喺呢一根或者呢一根 K 線嗰度 cover 咗。感覺上好似一個 failed bear flag，或者好似 VCP，但係佢仲喺跌勢入面，只不過已經向上突破。就係嗰種波動收縮之後再擴張，再加一點向下延伸，所以我就 cover 咗。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "佢指住大約呢一兩根 K 線，作為已經 cover 嘅位置。形態聽落似 failed bear flag 或者 VCP。雖然仲喺跌勢，但已經有 upward breakout。解釋係波動收縮之後再擴張，再加一點 downside extension，所以先平。",
                            "要抓住嘅係位置同形態，而唔係預測後面一定繼續升。呢 30 分鐘畫面冇見到落單票或者損益，所以唔應該寫死成交價同倉位大細。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-15m",
                "toc": "15 分鐘",
                "kicker": "圖三",
                "title": "XAUUSD 15 分鐘：收縮完、未大升之前",
                "time": "直播 28:12",
                "annotated": "images/03_xauusd_15m_2812.jpg",
                "source": "images/src_2812.jpg",
                "caption": "XAUUSD 15 分鐘，直播 28:12。游標指住收縮完、未大升之前嗰段；之後先有急升擴張。點圖可放大。",
                "alt_annotated": "加咗註解嘅 XAUUSD 15 分鐘圖：左邊標示波動收縮再擴張，游標指住收縮完、未大升之前嗰段；右邊標示之後先有向上擴張。",
                "alt_source": "直播原畫面：XAUUSD 15 分鐘圖，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "同一段對白 · 28:12 前後畫面",
                                "en": "And it's just like that volatility contraction and then the expansion.",
                            }
                        ],
                        "yc": "就係嗰種波動收縮，然後再擴張。",
                        "note": "呢幅 15 分鐘圖係用來睇清楚收縮同之後擴張嘅位置，並唔係另開一段新對白。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "15 分鐘圖睇得更清楚：游標喺收縮完成、大升之前嘅位置；之後先有急升擴張。",
                            "讀呢幅圖時，要分清「佢指住嘅位置」同「之後先出現嘅升浪」，唔好倒果為因，當成預先預測見底。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-gld",
                "toc": "GLD 15 分鐘",
                "kicker": "圖四",
                "title": "GLD 15 分鐘：更正為 overnight session",
                "time": "直播 28:57",
                "annotated": "images/04_gld_15m_2857.jpg",
                "source": "images/src_2857.jpg",
                "caption": "GLD 15 分鐘，直播 28:57。用來對 overnight 時間位置。註解標示更正時間為 overnight session，以及「probably around around here」所指附近；右邊急升係之後先出現嘅擴張。呢幅唔係用來寫死成交價。",
                "alt_annotated": "加咗註解嘅 GLD 15 分鐘圖：標示更正時間為 overnight session，以及 probably around around here 所指附近；右邊急升標為之後先出現嘅擴張。",
                "alt_source": "直播原畫面：GLD 15 分鐘圖，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "28:34 前後",
                                "en": "I think pre-market or even no I think it during the overnight section.",
                            },
                            {
                                "meta": "28:57–29:00",
                                "en": "probably around around here",
                            },
                        ],
                        "yc": "我以為係 pre-market，或者甚至——唔係，我想係 overnight session 嘅時候。大概喺呢附近。",
                        "note": "機器轉寫作 “overnight section”；按語境應為 overnight session。29:28–29:38 仲有一句 “um just a second”，並無補充呢個分析。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "佢起初以為係 pre-market，隨即更正係 overnight session，再喺 GLD 15 分鐘指住「probably around around here」。",
                            "GLD 有常規交易時段底色，所以呢幅圖係用來對時間，唔係另開一個白銀嘅個案，亦唔應用來寫死成交價。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "呢一段冇單獨出示白銀圖。佢有講 gold and silver shorts，但畫面只見 XAUUSD，之後先轉 GLD。",
            "呢 30 分鐘畫面冇見到落單票、成交價、倉位大細或者損益，所以本頁唔寫死呢啲數字。",
            "原話來自機器轉寫（faster-whisper，並對照 YouTube 自動字幕），並非逐字人工校對。轉寫本身註明 “overnight section” 按語境應為 overnight session。",
            "本頁只拆金銀淡倉呢一段（約 27:37–29:38），冇混入其他系統或者規則。",
        ],
    },
]

# 30:00 through the end of the 4 Nov 2026 stream. Text is copied from
# the static pages in this folder. Each subject uses the same keys as
# FIRST_HALF. Do not add fill prices, size, or P&L.
SECOND_HALF: list[dict] = [
    {
        "id": "fade-cover",
        "pager_name": "淡倉回顧",
        "when": "31:06–32:37",
        "nav": "回顧：淡倉本應喺今日低位多平一啲",
        "eyebrow": "科目七",
        "title": "回顧：淡倉本應喺今日低位多平一啲",
        "subtitle": "BE 大約打和、Qs 朝早行入週線 50 EMA、半導體低過週一低位同週線 50",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 31:06–32:37",
        "watch_label": "由 31:06 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=1866s",
        "summary_kicker": "概要",
        "summary_title": "今日低位本來可以多 cover 一啲",
        "summary": [
            "31:06 開始，佢回顧今日嘅 fade：市場由低位反彈之後，覺得自己至少應該喺今日低位／早段急跌入面 cover 多一啲淡倉。之後用 BE、QQQ 週線同 SOXX 日線／週線，解釋佢覺得嗰度已經係頗強嘅潛在支持，本應「向強勢賣出少少、向弱勢 cover 少少」。呢科係回顧同自我改進，唔係新開嘅淡倉教學。",
        ],
        "card": "BE pre-market 大約打和就 cover。朝早 Qs 行入週線 50 EMA；半導體低過週一低位同週線 50 EMA。本應向強勢賣出少少、向弱勢 cover 少少。",
        "charts": [
            {
                "anchor": "chart-be",
                "toc": "BE 日線",
                "kicker": "圖一",
                "title": "BE 日線：pre-market 大約打和就 cover",
                "time": "直播 31:10",
                "annotated": "images/fade-cover/01_be_daily_3110.jpg",
                "source": "images/fade-cover/src_be_daily_3110.jpg",
                "caption": "圖一 · BE（Bloom Energy）日線 · 直播 31:10。佢話 pre-market 大約打和就 cover；畫面睇唔到成交價。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 BE 日線圖：標示佢話 pre-market 大約打和就 cover，並註明畫面睇唔到成交價。",
                "alt_source": "直播原畫面：BE 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "31:06–31:15 · 機器轉寫，標點為閱讀而加",
                                "en": "Okay, and BE, I also covered it at the, I think at pre-market, I think around break even.",
                            },
                        ],
                        "yc": "OK，BE 我都 cover 咗，我諗係 pre-market，大約打和附近。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "畫面確認係 Bloom Energy（BE）日線。呢度只係一個佢講過嘅例子：大約打和就平咗。游標喺最近幾支 K 附近，但畫面冇成交票，所以唔寫死打和價或者倉位。",
                            "BE 唔單獨成科，只係呢段「今日低位本應多平一啲」嘅一個例子。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-qqq",
                "toc": "QQQ 週線",
                "kicker": "圖二",
                "title": "QQQ 週線：朝早行入 50 EMA 附近",
                "time": "直播 31:58",
                "annotated": "images/fade-cover/02_qqq_weekly_3158.jpg",
                "source": "images/fade-cover/src_qqq_weekly_3158.jpg",
                "caption": "圖二 · QQQ 週線 · 直播 31:58。佢話朝早 Qs 行入 50 EMA；註解只標黃線附近嘅位置，因為圖例冇印周期。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 QQQ 週線圖：標示朝早行入 50 EMA 附近，以及呢支週線低位向呢條均線靠近。",
                "alt_source": "直播原畫面：QQQ 週線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "31:19–32:08 · 機器轉寫，標點為閱讀而加",
                                "en": "As the market's starting to bounce from the lows. Actually, I think I should have covered some, at least some, into the lows of today's fade, like the earlier crash, earlier dip because of, I think, the election, and it's actually heading into the Qs at the 50 EMA at the morning,",
                            },
                        ],
                        "yc": "市場開始由低位反彈。其實我覺得自己至少應該喺今日 fade 嘅低位 cover 一啲，即係早段嗰輪急跌／回調（佢覺得同選舉有關）。而朝早 Qs 其實係行入 50 EMA。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "講緊「Qs at the 50 EMA in the morning」嗰陣，畫面已經係 QQQ 週線。圖例黃線約 671.73，冇印周期；註解只標「佢口中嘅 50 EMA 就喺呢附近」。呢支週線低位向呢條線靠近，但唔等於已經精確打中一個寫死嘅價位。",
                            "前半句係自我回顧：低位本應至少 cover 一啲，而唔係預測大市一定繼續彈。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-soxx-d",
                "toc": "SOXX 日線",
                "kicker": "圖三",
                "title": "SOXX 日線：游標指住週一低位",
                "time": "直播 32:08",
                "annotated": "images/fade-cover/03_soxx_daily_3208.jpg",
                "source": "images/fade-cover/src_soxx_daily_3208.jpg",
                "caption": "圖三 · SOXX 日線 · 直播 32:08。日期軸確認高大陰線係週一 02/11/2026；游標指住週一低位。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 SOXX 日線圖：標示週一呢支大陰線，以及游標指住週一低位。",
                "alt_source": "直播原畫面：SOXX 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "32:07–32:10",
                                "en": "and the semis is also below Monday's candle low",
                            },
                        ],
                        "yc": "半導體亦低過週一呢支 K 嘅低位。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "日期軸標示嗰支高大陰線係 Mon 02/11/2026，游標亦指住呢支嘅低位。呢句要小心讀：週二、週三嘅實體其實略高過週一低位，並非最後收市已經清楚跌穿。本頁只記錄佢口中嘅讀法，同游標指住邊度，唔把「而家收市已經低過週一低位」寫死。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-soxx-w",
                "toc": "SOXX 週線",
                "kicker": "圖四",
                "title": "SOXX 週線：亦低過週線 50 EMA",
                "time": "直播 32:11",
                "annotated": "images/fade-cover/04_soxx_weekly_3211.jpg",
                "source": "images/fade-cover/src_soxx_weekly_3211.jpg",
                "caption": "圖四 · SOXX 週線 · 直播 32:11。最後一支已經低過黃線一帶；佢當呢帶係頗強嘅潛在支持。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 SOXX 週線圖：標示週線 50 EMA 附近，以及收市已經低過呢條線。",
                "alt_source": "直播原畫面：SOXX 週線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "32:08–32:37 · 機器轉寫，標點為閱讀而加。'should have' 按 YouTube 字幕，Whisper v2 聽到 you'd have",
                                "en": "so it's also below the weekly 50 EMA. I yeah I consider that is a pretty strong potential support. [I] should have like sell something to strength, like cover something to weakness, at least some. But that's, I think, yeah, I think I can, I should, I can improve next time.",
                            },
                        ],
                        "yc": "所以亦低過週線 50 EMA。我覺得呢個係頗強嘅潛在支持。本應向強勢賣出少少，向弱勢 cover 少少，至少一啲。但係，我想下次可以改進。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "切到週線之後，最後一支已經低過黃線一帶。圖例同樣冇印周期，只按佢口中「weekly 50 EMA」標位置。佢把呢帶讀成頗強嘅潛在支持，所以覺得今日低位本來可以多平一啲，而唔係叫人而家先至去追 cover。",
                            "「sell something to strength / cover something to weakness」係管理淡倉嘅回顧原則，本頁唔寫成新開倉或者已經執行嘅單。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "圖上中文註解係之後加上嘅學習說明，唔係直播畫面原本已有嘅字。可用「原畫面」對返未加字嘅截圖。",
            "畫面睇唔到成交價、倉位大細或者損益，所以本頁唔寫死呢啲數字。",
            "圖例多數只有顏色同數值，冇印均線周期。本頁唔會把某條彩線寫死成某個周期；如果佢有講周期，只標「佢口中嘅位置就喺呢附近」。",
            "原話來自機器轉寫（faster-whisper large-v3-turbo，並對照 YouTube 自動英文字幕），並非逐字人工校對。標點為閱讀而加。",
            "32:15 之後有一段靜音翻圖（NQ、RTY、AXTI、SK Hynix 等），冇再講分析，唔算入呢科。",
            "本頁只拆呢段淡倉回顧（約 31:06–32:37），冇混入其他系統或者規則。",
        ],
    },
    {
        "id": "gold-21",
        "pager_name": "唔好第一次碰到 21 就淡黃金",
        "when": "33:29–35:29",
        "nav": "唔好喺日線第一次碰到 21 就淡黃金",
        "eyebrow": "科目八",
        "title": "唔好喺日線第一次碰到 21 就淡黃金",
        "subtitle": "等 21 附近整固；由 9 底下伸延強勢升上來嘅第一支，唔適宜即淡",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 33:29–35:29",
        "watch_label": "由 33:29 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=2009s",
        "summary_kicker": "概要",
        "summary_title": "第一次碰到 21，唔等於可以即淡",
        "summary": [
            "有觀眾問：日線黃金已經回調到 21 EMA，會唔會考慮做淡？佢明確話「對我嚟講一定唔會」。如果要淡，都想等 21 附近整固幾日，而唔係喺第一支推入 21 嘅 K 就淡——因為呢支係由下面、9 EMA 底下嘅 downside extension 強勢升上來。之後佢話 50 EMA 可能係更好嘅淡位，但已經太遲；市場需要多啲時間整固，先決定下一個方向同 range expansion。講「好強嘅反彈」嗰陣，畫面仍然係黃金，唔係 QQQ。",
        ],
        "card": "想淡就等 21 附近整固，而唔係第一支由 9 底下伸延升上來嘅 K 就淡。50 EMA 可能更好，但已經太遲；呢段係好強嘅反彈。",
        "charts": [
            {
                "anchor": "chart-first",
                "toc": "第一次推入 21",
                "kicker": "圖一 · 主圖",
                "title": "XAUUSD 日線：第一支推入 21，唔好即淡",
                "time": "直播 34:15",
                "annotated": "images/gold-21/01_xauusd_daily_3415.jpg",
                "source": "images/gold-21/src_xauusd_daily_3415.jpg",
                "caption": "圖一 · XAUUSD 日線 · 直播 34:15。第一支綠色推入紫色均線一帶；低位曾經喺青線底下。 點圖可放大。",
                "alt_annotated": "加咗註解嘅黃金日線圖：標示第一支推入 21 嘅 K，以及由 9 EMA 底下強勢突破。",
                "alt_source": "直播原畫面：XAUUSD 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "33:27–34:21 · 觀眾問題按 YouTube 字幕（Whisper 把 gold 聽成 goal）。標點為閱讀而加",
                                "en": "On daily time frame gold is having pulled back to 21 EMA, would you consider that short entry? Like for me definitely not. Like if I would like to short, I think if I have to, I would wait for maybe a couple of days' consolidation near the 21, instead of shorting at the first candle pushing into the 21, given like this is a really strong candle, this breaking out from way down here like below the 9 EMA, and then just from a downside extension.",
                            },
                        ],
                        "yc": "日線黃金已經回調到 21 EMA，會唔會考慮呢個淡倉入場？對我嚟講一定唔會。如果我要淡，都會等 21 附近或者整固幾日，而唔係喺第一支推入 21 嘅 K 就淡。因為呢支其實係好強嘅 K，由好下面、9 EMA 底下，即係 downside extension 升上來。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "圖例紫色約 4065.8、青色約 4003.6，冇印周期。高位約 4051 已經碰到紫色一帶，低位 3919 曾經低過青線。註解按佢口中「21 / 9」標位置，唔把彩線周期寫死喺圖例上。",
                            "要學嘅係：碰到均線唔等於即刻反向開倉；呢支係由伸延低位強勢升上來嘅第一支，所以佢寧願等整固。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-50",
                "toc": "拉遠：50 EMA 同強勢反彈",
                "kicker": "圖二",
                "title": "拉遠之後：50 EMA 可能更好，但已經太遲",
                "time": "直播 35:28",
                "annotated": "images/gold-21/02_xauusd_daily_3528.jpg",
                "source": "images/gold-21/src_xauusd_daily_3528.jpg",
                "caption": "圖二 · XAUUSD 日線（拉遠）· 直播 35:28。黃線仍在上面；最後一支已經係好強嘅反彈 K。 點圖可放大。",
                "alt_annotated": "加咗註解嘅黃金日線拉遠圖：標示 50 EMA 仍在上面，以及呢支已經係好強嘅反彈。",
                "alt_source": "直播原畫面：XAUUSD 日線拉遠，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "35:01–35:29 · Whisper 兩次都係 50 EMA；YouTube 自動字幕寫成 15 year maybe。按畫面同 Whisper",
                                "en": "Right now I think the 50 EMA would be the better one to short, but I think it's too late. I think the market needs a little bit more time to consolidate and then to decide the next direction, the next range expansion. I think right now we are getting in a pretty strong bounce.",
                            },
                        ],
                        "yc": "而家我覺得 50 EMA 會係更好嘅淡位，但我覺得已經太遲。市場需要多啲時間去整固，然後先決定下一個方向、下一次 range expansion。我覺得而家我哋係處於一波頗強嘅反彈入面。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "35:00–35:06 畫面喺黃金日線同週線之間切換，之後拉遠日線；到 35:29 講完「pretty strong bounce」仍然未切到 QQQ。所以「好強嘅反彈」係講緊黃金／呢段市況，唔好誤用成 35:30 嘅其他品種圖。",
                            "YouTube 自動字幕把「50 EMA」聽成「15 year maybe」。兩個 Whisper 版本都係 50 EMA，而拉遠日線上面仍然見到黃線。本頁跟 Whisper 同畫面，並把字幕分歧寫喺附註。",
                            "「更好嘅淡位」後面立刻係「太遲」，唔好把呢句讀成而家先至去淡 50 EMA。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "圖上中文註解係之後加上嘅學習說明，唔係直播畫面原本已有嘅字。可用「原畫面」對返未加字嘅截圖。",
            "畫面睇唔到成交價、倉位大細或者損益，所以本頁唔寫死呢啲數字。",
            "圖例多數只有顏色同數值，冇印均線周期。本頁唔會把某條彩線寫死成某個周期；如果佢有講周期，只標「佢口中嘅位置就喺呢附近」。",
            "原話來自機器轉寫（faster-whisper large-v3-turbo，並對照 YouTube 自動英文字幕），並非逐字人工校對。標點為閱讀而加。 呢段「50 EMA」同 YouTube「15 year maybe」唔一致，本頁按 Whisper 同拉遠日線跟 50 EMA。",
            "35:29 之後畫面先轉天然氣／YM 等，唔算入呢科。",
            "本頁只拆黃金呢條問答（約 33:29–35:29），冇混入其他系統或者規則。",
        ],
    },
    {
        "id": "crwd-thesis",
        "pager_name": "Crowd long 論證",
        "when": "36:21–39:41",
        "nav": "Crowd long：相對強勢同 undercut-reclaim",
        "eyebrow": "科目九",
        "title": "Crowd long：相對強勢、early flush 同 undercut-reclaim",
        "subtitle": "軟件／資安相對較強；今日 50 EMA 支持，週線 9 EMA 支持",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 36:21–39:41",
        "watch_label": "由 36:21 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=2181s",
        "summary_kicker": "概要",
        "summary_title": "計劃由想淡，轉做 bounce / mean reversion long",
        "summary": [
            "觀眾問 Crowd long 同 Coin long。Crowd 呢段，佢話而家係自己觀察範圍入面其中一隻最強嘅名字。今日早段 flush 之後 reclaim，計劃已經轉做向上嘅 bounce／mean reversion，而唔係喺呢次 shake out 或者 undercut-reclaim 之後仲想淡。軟件相對其他科技較強，資安由十月初大市轉弱以嚟整過底；Fortinet 差，OKTA 較好睇，Crowd 係當中最強。今日有 50 EMA 支持，週線有 9 EMA 支持。",
        ],
        "card": "早段 flush 後計劃轉做 bounce／mean reversion long。軟件／資安相對較強；OKTA 較好睇，Crowd 最強。今日 50 EMA 支持，週線 9 EMA 支持。",
        "charts": [
            {
                "anchor": "chart-crwd-d",
                "toc": "CRWD 日線",
                "kicker": "圖一 · 主圖",
                "title": "CRWD 日線：今日 50 EMA 支持，下探後 reclaim",
                "time": "直播 38:44",
                "annotated": "images/crwd/01_crwd_daily_3844.jpg",
                "source": "images/crwd/src_crwd_daily_3844.jpg",
                "caption": "圖一 · CRWD 日線 · 直播 38:44。黃線約 241.17；低位 237.21 下探後收 246 收回。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 CRWD 日線圖：標示今日 50 EMA 支持，以及 undercut 再收回。",
                "alt_source": "直播原畫面：CRWD 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "36:21–36:53 · 'mean reversion' 按 YouTube 字幕；Whisper 聽到 mini version。標點為閱讀而加",
                                "en": "Can you explain your Crowd long and Coin long? Crowd, one of the strongest name right now in the universe. So like after today's early flush and then they reclaim, my plan is kind of shifted towards the bounce, like the mean reversion on the long side, instead of trying to short after this shake out or like the undercut and reclaim.",
                            },
                        ],
                        "yc": "可唔可以解釋吓你嘅 Crowd long 同 Coin long？Crowd 而家係我呢個觀察範圍入面其中一隻最強嘅名字。今日早段 flush 之後佢哋 reclaim，我嘅計劃已經偏向做 bounce，即係 long 邊嘅 mean reversion，而唔係喺呢次 shake out 或者 undercut 再 reclaim 之後仲想淡。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "日線低位 237.21 曾經低過黃線（約 241.17），收市約 246 已經收回。圖例冇印周期；註解按佢後一句「today we got the 50 EMA support」標呢條黃線位置。呢幅圖同時解釋點解計劃會轉：undercut 之後已經 reclaim，唔再當淡倉 setup。",
                            "YouTube 字幕係 early flash，Whisper 係 early flush。本頁用 flush，因為語境係早段下殺再收回。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-okta",
                "toc": "OKTA 對照",
                "kicker": "圖二",
                "title": "OKTA：較好睇嘅軟件名，只用嚟對照",
                "time": "直播 38:12",
                "annotated": "images/crwd/02_okta_daily_3812.jpg",
                "source": "images/crwd/src_okta_daily_3812.jpg",
                "caption": "圖二 · OKTA 日線 · 直播 38:12。佢用來對照「較好睇嘅軟件名」；真正最強仍然係 Crowd。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 OKTA 日線圖：標示較好睇嘅軟件名，只用嚟對照。",
                "alt_source": "直播原畫面：OKTA 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "37:12–38:16 · 機器轉寫，標點為閱讀而加",
                                "en": "So I would like to pick one in the software sector, which is comparatively stronger than the other tech stocks, and among the software names, I think the cyber securities are getting a decent base. Since early October, when the market is starting to decline, I think the cybers are doing fine. Some are definitely, Fortinets are doing bad, but we got some better looking names like this, OKTA.",
                            },
                        ],
                        "yc": "所以我想喺軟件板塊揀一隻，相對其他科技股比較強。軟件入面，我覺得資安最近有一個幾像樣嘅底。由十月初大市開始跌以嚟，我覺得資安都仲可以。有啲當然差，Fortinet 就做得差，但亦有較好睇嘅名字，例如 OKTA。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "OKTA 只係對照，唔係呢段嘅主交易。佢隨即話細價資安／雲安全有啲做得好，但冇放入自己觀察名單；之後先指 Crowd 先至係最強。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-crwd-w",
                "toc": "CRWD 週線",
                "kicker": "圖三",
                "title": "CRWD 週線：9 EMA 支持",
                "time": "直播 38:47",
                "annotated": "images/crwd/03_crwd_weekly_3847.jpg",
                "source": "images/crwd/src_crwd_weekly_3847.jpg",
                "caption": "圖三 · CRWD 週線 · 直播 38:47。畫面只出現約兩三秒；價格喺最快呢條青線上面。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 CRWD 週線圖：標示週線 9 EMA 支持，以及而家喺呢條線上面。",
                "alt_source": "直播原畫面：CRWD 週線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "38:37–39:41 · 機器轉寫，標點為閱讀而加",
                                "en": "And among all those names Crowd is the strongest. So and today we got the 50 EMA supports, the weekly 9 EMA supports.",
                            },
                        ],
                        "yc": "喺呢啲名字入面，Crowd 係最強。而且今日我哋有 50 EMA 支持，週線有 9 EMA 支持。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "週線只停留約兩三秒（約 38:47–38:49），38:50 已經開始切走，所以本頁用 38:47，唔用 38:50。圖例同樣冇印周期，只標「佢口中嘅週線 9 EMA 就喺呢條最快青線附近」。",
                            "「今日 50 EMA 支持」主要仍然要對返圖一日線：低位下探黃線後收回。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "圖上中文註解係之後加上嘅學習說明，唔係直播畫面原本已有嘅字。可用「原畫面」對返未加字嘅截圖。",
            "畫面睇唔到成交價、倉位大細或者損益，所以本頁唔寫死呢啲數字。",
            "圖例多數只有顏色同數值，冇印均線周期。本頁唔會把某條彩線寫死成某個周期；如果佢有講周期，只標「佢口中嘅位置就喺呢附近」。",
            "原話來自機器轉寫（faster-whisper large-v3-turbo，並對照 YouTube 自動英文字幕），並非逐字人工校對。標點為閱讀而加。 「mean reversion」按 YouTube；Whisper 聽到 mini version。",
            "39:41 之後佢同 chat 講「I'm selling Crowd / Crowd looks bearish」，自己解釋係想試吓有冇 algo 讀緊直播，並話 easily proven that's not true、just test it out in the market。呢段係玩笑／測試，唔係淡倉方法，所以唔獨立成科，亦唔當成短線賣出教學。",
            "本頁只拆 Crowd long 論證（約 36:21–39:41），Coin long 見下一科之後嘅科目十一。冇混入其他系統或者規則。",
        ],
    },
    {
        "id": "crwd-entry",
        "pager_name": "Crowd 入場",
        "when": "43:59–45:25",
        "nav": "Crowd 入場：1 分鐘突破、回踩上升 9",
        "eyebrow": "科目十",
        "title": "Crowd 入場：最好係 1 分鐘低位突破",
        "subtitle": "錯過之後，等 1 分鐘收市高過 9 EMA，再等回踩上升緊嘅 9",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 43:59–45:25",
        "watch_label": "由 43:59 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=2639s",
        "summary_kicker": "概要",
        "summary_title": "自己都覺得買得遲少少",
        "summary": [
            "觀眾問點解 Crowd 未見任何週期最終支持都買。佢話自己其實買得遲少少：最好嘅入場係 1 分鐘低位突破，但太快，錯過咗。如果錯過第一次，多數會等 1 分鐘收市高過 9 EMA；但呢支收市太強，已經離開 low of day 一段。然後就等回踩上升緊嘅 9 EMA——游標指住「呢度，或者呢度都可以係入場」。佢鍾意呢段 undercut 再 rally，並話價錢 undercutting 50 EMA 之後而家彈返上。",
        ],
        "card": "最好入場係 1 分鐘低位突破，但太快錯過。之後等收市高過 9 EMA；呢支太強，再等回踩上升緊嘅 9。鍾意 undercut 50 EMA 再 rally。",
        "charts": [
            {
                "anchor": "chart-break",
                "toc": "1 分鐘低位突破",
                "kicker": "圖一",
                "title": "CRWD 1 分鐘：最好嘅入場係低位突破，但太快",
                "time": "直播 44:15",
                "annotated": "images/crwd/04_crwd_1m_4415.jpg",
                "source": "images/crwd/src_crwd_1m_4415.jpg",
                "caption": "圖一 · CRWD 1 分鐘 · 直播 44:15。標示早段 flush 低位，以及隨後第一輪 1 分鐘突破。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 CRWD 一分鐘圖：標示最好嘅入場係 1 分鐘低位突破，以及早段 flush 低位。",
                "alt_source": "直播原畫面：CRWD 1 分鐘，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "44:07–44:25 · 機器轉寫，標點為閱讀而加",
                                "en": "Honestly I'm buying a little bit too late. I think the best entry is definitely the one minute breakouts down here, but yeah it's just too fast and I just missed it.",
                            },
                        ],
                        "yc": "老實說我買得遲少少。我覺得最好嘅入場肯定係呢度下面嘅 1 分鐘突破，但係太快，我錯過咗。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "圖上標咗早段 flush 嘅 low of day，同隨後第一輪向上突破。呢句重點係「最好嘅位置已經錯過」，唔好把後嚟嘅入場讀成最理想點。",
                            "畫面仍然睇唔到成交價，所以唔寫死佢實際買喺邊度。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-pull",
                "toc": "回踩上升 9 EMA",
                "kicker": "圖二 · 主圖",
                "title": "錯過之後：等收市高過 9，再等回踩",
                "time": "直播 45:05",
                "annotated": "images/crwd/05_crwd_1m_4505.jpg",
                "source": "images/crwd/src_crwd_1m_4505.jpg",
                "caption": "圖二 · CRWD 1 分鐘 · 直播 45:05。游標指住回踩上升均線嘅位置；較早一支收市已經離開低位一段。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 CRWD 一分鐘圖：標示回踩上升緊嘅 9 EMA，以及呢支收市高過 9 但太強。",
                "alt_source": "直播原畫面：CRWD 1 分鐘，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "44:27–45:25 · 後半「50 EMA」按 YouTube 同日線圖；Whisper v2 聽到 15 EMA。標點為閱讀而加",
                                "en": "Most of the time, if I miss the first, like the one minute breakout entry point, then maybe I will wait for one minute close above the 9 EMA. And then this close is too strong, it's already a little bit extended from the low of day. And then I just wait for the pullback into the rising 9 EMA. So actually maybe like in here or maybe even here, I think this could be also an entry. And I just like this undercutting rally on the Crowd. I know it's undercutting the 50 EMA and now it's rallying back.",
                            },
                        ],
                        "yc": "多數時候，如果我錯過第一次、即係嗰個 1 分鐘突破入場，之後或者會等 1 分鐘收市高過 9 EMA。但呢支收市太強，已經離開今日低位一段，有少少伸延。然後我就等回踩上升緊嘅 9 EMA。所以其實或者呢度，甚至呢度，我覺得都可以係一個入場。我只係鍾意 Crowd 呢段 undercut 再 rally。我知佢 undercutting 50 EMA，而家彈返上。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "游標喺回踩上升均線嘅位置。原話「maybe like in here or maybe even here」係兩個相近嘅回踩位置，註解指住游標所在；另一個「甚至呢度」只係口頭補充，唔好把附近每支 K 都寫成已經確認嘅入場點。",
                            "「呢支收市太強」係指第一輪突破入面、已經離開 low of day 嘅那支強勢收市，之後先至等回踩。如果覺得註解點同你睇嘅那支不完全重疊，請切返原畫面核對。",
                            "「undercutting the 50 EMA」要對返科目九嘅日線：低位曾經低過黃線後收回。Whisper v2 呢句聽到 15 EMA，YouTube 同日線都支持 50 EMA，本頁用 50。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "圖上中文註解係之後加上嘅學習說明，唔係直播畫面原本已有嘅字。可用「原畫面」對返未加字嘅截圖。",
            "畫面睇唔到成交價、倉位大細或者損益，所以本頁唔寫死呢啲數字。",
            "圖例多數只有顏色同數值，冇印均線周期。本頁唔會把某條彩線寫死成某個周期；如果佢有講周期，只標「佢口中嘅位置就喺呢附近」。 1 分鐘圖同樣冇印周期。",
            "原話來自機器轉寫（faster-whisper large-v3-turbo，並對照 YouTube 自動英文字幕），並非逐字人工校對。標點為閱讀而加。",
            "45:25 之後佢補「no matter what I just have to get in」，然後先轉去講 Coin。45:45–47:45 附近有 SPCE 等靜音翻圖，唔算入呢科。",
            "本頁只拆 Crowd 入場讀法（約 43:59–45:25），冇混入其他系統或者規則。",
        ],
    },
    {
        "id": "coin-crypto",
        "pager_name": "COIN long 同加密",
        "when": "48:03–50:31",
        "nav": "COIN long 同加密：位置同市場動能",
        "eyebrow": "科目十一",
        "title": "COIN long 同加密：150 EMA reclaim、週線 21、失敗跌穿",
        "subtitle": "形態沒有市場動態同價格行為咁重要；唔寫死入場價",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 48:03–50:31",
        "watch_label": "由 48:03 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=2883s",
        "summary_kicker": "概要",
        "summary_title": "加密先講位置，再講點解入 COIN",
        "summary": [
            "48:03 開始答 Coin long。佢先用比特幣解釋：主要係 150 EMA reclaim，同之前講過、回調期間停過一段嘅週線 21；覺得 21 對加密好重要，甚至有機會由呢度做多月反彈。COIN 方面，佢鍾意靠近大約兩年半嘅大支持，而且向下降伸延之後，想跌穿但失敗；話昨日係好嘅 reclaim，今日再加加密本身嘅力量，所以喺呢段日内區間入場。Micro MSTR 或者 BMNR 佢都有想過，但移動太快、太伸延。最後強調：有時形態沒那麼重要，理解市場動態同讀價格行為更加緊要。",
        ],
        "card": "150 EMA reclaim、週線 21 對加密重要。COIN 靠近兩年半支持，失敗跌穿後喺日内區間入場。形態沒有市場動態同價格行為咁重要。",
        "charts": [
            {
                "anchor": "chart-btc-d",
                "toc": "BTC 日線",
                "kicker": "圖一",
                "title": "BTC 日線：150 EMA reclaim（佢口中嘅位置）",
                "time": "直播 48:13",
                "annotated": "images/coin-crypto/01_btc_daily_4813.jpg",
                "source": "images/coin-crypto/src_btc_daily_4813.jpg",
                "caption": "圖一 · BTCUSDT.P 日線 · 直播 48:13。價格彈返右邊呢帶均線；圖例冇印周期，唔把某條線寫死成 150。 點圖可放大。",
                "alt_annotated": "加咗註解嘅比特幣日線圖：標示佢口中嘅 150 EMA reclaim 就喺呢帶均線位置。",
                "alt_source": "直播原畫面：BTCUSDT.P 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "48:03–48:18 · 機器轉寫，標點為閱讀而加",
                                "en": "And crypto's Coin. I think it's mainly on the 150 EMA reclaim.",
                            },
                        ],
                        "yc": "至於加密嘅 Coin。我覺得主要係 150 EMA reclaim。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "呢句係喺比特幣日線上講。圖例冇印周期，右邊係一堆收緊嘅均線，價格剛彈返呢帶。註解只標位置，唔把黃線或者灰線寫死成 150。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-btc-w",
                "toc": "BTC 週線",
                "kicker": "圖二",
                "title": "BTC 週線：21 好重要，回調時停過一段",
                "time": "直播 48:19",
                "annotated": "images/coin-crypto/02_btc_weekly_4819.jpg",
                "source": "images/coin-crypto/src_btc_weekly_4819.jpg",
                "caption": "圖二 · BTCUSDT.P 週線 · 直播 48:19。游標指住均線堆疊一帶；佢話週線 21 對加密好重要。 點圖可放大。",
                "alt_annotated": "加咗註解嘅比特幣週線圖：標示佢口中嘅週線 21 附近，以及游標指住呢一帶。",
                "alt_source": "直播原畫面：BTCUSDT.P 週線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "48:18–48:54 · 'stopped' 按 YouTube；Whisper v2 聽到 stocked。'hottest theme' 按 Whisper；YouTube 係 hottest thing",
                                "en": "The weekly 21 that I mentioned that it stopped for quite a while, like earlier during this pullback. I think the 21 EMA is pretty important for the cryptos, and I think cryptos could get a multi-month rally from here. I think [it] will become one of the hottest theme in the next bull run if we are getting one.",
                            },
                        ],
                        "yc": "我之前講過嘅週線 21，回調期間喺呢度停過一段時間。我覺得 21 EMA 對加密好重要，而且加密有機會由呢度做一段多月嘅反彈。如果下一輪牛市真係出現，我覺得佢可能成為其中一個最熱嘅主題。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "游標指住週線均線堆疊一帶。同樣只按口中「weekly 21」標位置。多月反彈同「hottest theme」係佢當時嘅看法，不是已經發生嘅結果，亦唔係買賣指示。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-coin-w",
                "toc": "COIN 週線",
                "kicker": "圖三",
                "title": "COIN 週線：大約兩年半嘅大支持",
                "time": "直播 49:15",
                "annotated": "images/coin-crypto/03_coin_weekly_4915.jpg",
                "source": "images/coin-crypto/src_coin_weekly_4915.jpg",
                "caption": "圖三 · COIN 週線 · 直播 49:15。虛線水平大約兩年半支持；價格由下面伸延後彈返呢度。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 COIN 週線圖：標示大約兩年半嘅大支持，以及最近呢帶嘅反彈。",
                "alt_source": "直播原畫面：COIN 週線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "48:54–49:27 · 機器轉寫，標點為閱讀而加",
                                "en": "And Coin, what I do like is it's near this huge support level for like two and a half years and getting extended to the downside.",
                            },
                        ],
                        "yc": "而 Coin，我鍾意嘅係佢靠近呢個大約兩年半嘅大支持，而且向下降已經有少少伸延。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "虛線水平就係佢講嘅「huge support」。價格由下面伸延之後彈返呢條線附近。呢句係位置觀察，唔等於支持一定守得住，亦唔寫成目標價。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-coin-d",
                "toc": "COIN 日線",
                "kicker": "圖四 · 主圖",
                "title": "COIN 日線：想跌穿但失敗，昨日好嘅 reclaim",
                "time": "直播 49:36",
                "annotated": "images/coin-crypto/04_coin_daily_4936.jpg",
                "source": "images/coin-crypto/src_coin_daily_4936.jpg",
                "caption": "圖四 · COIN 日線 · 直播 49:36。游標指住下探低位；今日呢支強勢收回。COIN 日線只在講 failed breakdown 時出現。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 COIN 日線圖：標示想跌穿但失敗嘅低位，以及今日呢支強勢收回。",
                "alt_source": "直播原畫面：COIN 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "49:28–49:47 · 機器轉寫，標點為閱讀而加",
                                "en": "Trying to break down but failed. Yesterday we tried and yesterday is a good reclaim. And today together with the actual cryptos strength, I think that's why I enter it at this intraday range.",
                            },
                        ],
                        "yc": "想跌穿但失敗。昨日試過，而昨日係一個好嘅 reclaim。今日再連同加密本身嘅力量，我覺得所以先至喺呢段日内區間入場。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "「enter it at this intraday range」後一句先切到 5 分鐘。日線呢度用嚟解釋 failed breakdown 同 reclaim；唔好把日線最後一支嘅收市價寫成入場價。49:00 附近畫面仲係比特幣，COIN 日線大約 49:06 先出現，本頁用講 failed breakdown 嗰秒（49:36）。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-coin-5m",
                "toc": "COIN 5 分鐘",
                "kicker": "圖五",
                "title": "COIN 5 分鐘：今日入場嘅日内區間",
                "time": "直播 49:50",
                "annotated": "images/coin-crypto/05_coin_5m_4950.jpg",
                "source": "images/coin-crypto/src_coin_5m_4950.jpg",
                "caption": "圖五 · COIN 5 分鐘 · 直播 49:50。游標指住今日呢段日内區間；畫面睇唔到成交價。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 COIN 五分鐘圖：標示今日入場嘅日内區間，以及早段下探再急升收回。",
                "alt_source": "直播原畫面：COIN 5 分鐘，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "49:48–50:53 · 'BMNR' 按畫面（BitMine）；YouTube 聽到 BM and Apple。標點為閱讀而加",
                                "en": "That's why I enter it at this intraday range. I'm also thinking like taking the micro MSTR or even like BMNR, but they are like moving too fast and a little bit too extended. Sometimes the pattern just doesn't really matter that much. Like I don't think there's a particular pattern right here. But I think understanding the market dynamics and also reading the price actions is pretty important.",
                            },
                        ],
                        "yc": "所以我喺呢段日内區間入場。我亦有想過做 micro MSTR，甚至 BMNR，但佢哋移動得太快，亦有少少太伸延。有時形態其實沒有咁重要，我唔覺得呢度有一個特定形態。但係理解市場動態，同埋讀價格行為，我覺得好重要。",
                        "note": "約 56:16 佢回到加密，補咗一句（當時畫面係 BTC 日線，本頁唔另外出圖，避免同圖一重複）：Let's see whether the cryptos can hold above this 50 EMA and like gradually trailing this rising 9 EMA to the upside. We're not completely out of the woods yet.\n譯：睇吓加密可唔可以守喺呢條 50 EMA 上面，然後慢慢沿住呢條上升緊嘅 9 EMA 向上移。我哋都仲未完全脫險。原畫面備份喺 images/coin-crypto/src_btc_daily_5616.jpg。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "游標指住 5 分鐘呢段區間。畫面仍然睇唔到成交價，只知佢話入喺呢段區間，唔寫死填單價。",
                            "Micro MSTR 同 BMNR 佢只係「有想過」，隨即話太快、太伸延，本頁冇當佢已經做咗呢兩隻，亦冇單獨出圖。YouTube 把後者聽成「BM and Apple」；當時畫面見到 MSTR 再見到 BMNR（BitMine），冇把 Apple 做成圖。呢點有字幕不確定，寫喺附註。",
                            "最後兩句係呢科想學嘅重點：形態沒有市場動態同價格行為咁重要。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "圖上中文註解係之後加上嘅學習說明，唔係直播畫面原本已有嘅字。可用「原畫面」對返未加字嘅截圖。",
            "畫面睇唔到成交價、倉位大細或者損益，所以本頁唔寫死呢啲數字。",
            "圖例多數只有顏色同數值，冇印均線周期。本頁唔會把某條彩線寫死成某個周期；如果佢有講周期，只標「佢口中嘅位置就喺呢附近」。",
            "原話來自機器轉寫（faster-whisper large-v3-turbo，並對照 YouTube 自動英文字幕），並非逐字人工校對。標點為閱讀而加。 「stopped」按 YouTube；「hottest theme」按 Whisper（YouTube 為 hottest thing）。",
            "YouTube 把「BMNR」聽成「BM and Apple」。畫面支持 BMNR；Apple 只列作字幕不確定，唔做圖。",
            "本頁只拆 Coin long 同加密呢段（約 48:03–50:31，並附 56:16 補充），冇混入其他系統或者規則。",
        ],
    },
    {
        "id": "tsla",
        "pager_name": "Tesla",
        "when": "51:10–52:23",
        "nav": "Tesla：週線均線聚合同多年底",
        "eyebrow": "科目十二",
        "title": "Tesla：週線均線聚合、多年底，同相對強勢",
        "subtitle": "亦提到日線 50／150 EMA、前高同未補缺口；覺得本應再大啲倉，但冇講數字",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 51:10–52:23",
        "watch_label": "由 51:10 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=3070s",
        "summary_kicker": "概要",
        "summary_title": "星期一講過嘅計劃，佢覺得做得好",
        "summary": [
            "51:10 開始講 Tesla：星期一已經提過，計劃完整執行。佢覺得呢段係近期其中一筆最好嘅交易。理由包括：週線均線聚合、多年底／VCP 類型、大市弱勢時仍然有相對強勢；以及日線 50、150 EMA、前高、未補嘅缺口。之後話自己本應 size 再大啲，但畫面冇倉位數字，本頁亦不發明。",
        ],
        "card": "週線均線聚合、多年底／VCP 類型、弱市相對強勢；亦有日線 50／150 EMA、前高同未補缺口。話本應再大啲倉，但冇講數字。",
        "charts": [
            {
                "anchor": "chart-w",
                "toc": "TSLA 週線",
                "kicker": "圖一 · 主圖",
                "title": "TSLA 週線：均線聚合同多年底",
                "time": "直播 51:30",
                "annotated": "images/tsla/01_tsla_weekly_5130.jpg",
                "source": "images/tsla/src_tsla_weekly_5130.jpg",
                "caption": "圖一 · TSLA 週線 · 直播 51:30。呢一秒游標喺空白處，所以註解指中間嘅均線聚合、多年底，同右邊近期位置。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 TSLA 週線圖：標示週線均線聚合、多年底／VCP 類型，以及近期位置。",
                "alt_source": "直播原畫面：TSLA 週線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "51:10–51:41 · 機器轉寫，標點為閱讀而加。'base' 按語境；兩個轉寫都出現 type basis / type of type bases",
                                "en": "Tesla is the one I mentioned on Monday. We got the plan fully worked out. I think this is one of the best trades I've ever made in a while. We mentioned this weekly EMA convergence, multi-year base, VCP type base, and relative strength during the market weakness,",
                            },
                        ],
                        "yc": "Tesla 就係我星期一提過嗰隻。我哋把計劃完整執行咗。我覺得呢段係近期我做過最好嘅交易之一。我哋提過呢個週線均線聚合、多年底、VCP 類型嘅底，同埋大市弱勢時嘅相對強勢。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "51:30 游標停喺圖中偏右嘅空白處，並唔指住結構，所以註解冇跟游標。均線聚合指中間幾條線曾經收得很近嘅位置；多年底／VCP 類型指左邊同中間嗰段長時間整固；近期位置指右邊已經離開底嘅價格。",
                            "「最好嘅交易之一」係事後感受，本頁只用來理解佢點讀結構，唔當成績證明，亦冇損益數字。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-d",
                "toc": "TSLA 日線",
                "kicker": "圖二",
                "title": "TSLA 日線：50／150 EMA 一帶",
                "time": "直播 51:48",
                "annotated": "images/tsla/02_tsla_daily_5148.jpg",
                "source": "images/tsla/src_tsla_daily_5148.jpg",
                "caption": "圖二 · TSLA 日線 · 直播 51:48。標示右邊呢堆均線位置同而家價格；前高同未補缺口請對住原畫面一齊睇。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 TSLA 日線圖：標示日線 50／150 EMA 一帶，以及而家喺均線之上。",
                "alt_source": "直播原畫面：TSLA 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "51:42–52:23 · 機器轉寫，標點為閱讀而加",
                                "en": "also the daily 50 150 EMA, previous swing high, also this unfilled gap level. I just, I should have sized bigger, but I think it is what it is. I think this one is a really good opportunity.",
                            },
                        ],
                        "yc": "亦有日線 50、150 EMA，前高，同埋呢個未補嘅缺口位置。我只係，我本應 size 再大啲，但係都係咁。我覺得呢個係一個好好嘅機會。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "圖例冇印周期，註解只標右邊呢堆均線同而家價格。前高同未補缺口喺日線上要仔細對，本頁唔強行加箭嘴，避免指錯位置；請切返原畫面一齊睇。",
                            "「should have sized bigger」只有這句，畫面冇倉位或者損益，所以完全唔寫數字。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "圖上中文註解係之後加上嘅學習說明，唔係直播畫面原本已有嘅字。可用「原畫面」對返未加字嘅截圖。",
            "畫面睇唔到成交價、倉位大細或者損益，所以本頁唔寫死呢啲數字。",
            "圖例多數只有顏色同數值，冇印均線周期。本頁唔會把某條彩線寫死成某個周期；如果佢有講周期，只標「佢口中嘅位置就喺呢附近」。",
            "原話來自機器轉寫（faster-whisper large-v3-turbo，並對照 YouTube 自動英文字幕），並非逐字人工校對。標點為閱讀而加。",
            "52:25 之後轉去問書、新聞，佢回應「stick to the charts」，唔再講圖，所以唔算入呢科。",
            "本頁只拆 Tesla 呢段（約 51:10–52:23），冇混入其他系統或者規則。",
        ],
    },
    {
        "id": "choppy-cover",
        "pager_name": "市況偏亂、可能平淡倉",
        "when": "57:59–1:00:15",
        "nav": "市況仍然偏亂：短線淡倉或應平一啲",
        "eyebrow": "科目十三",
        "title": "好多股票仍在阻力／下降均線下面",
        "subtitle": "未有新升勢嘅好 setup；短線連續跳空同大陰線之後，淡倉風險回報未必好",
        "meta": "Martin Luk · 《Flipped long》 · 2026年11月4日 · 時間碼 57:59–1:00:15，並附 1:02:23–1:03:58 收結",
        "watch_label": "由 57:59 觀看直播片段",
        "watch_url": "https://www.youtube.com/watch?v=NUT6d6Hvbmw&t=3479s",
        "summary_kicker": "概要",
        "summary_title": "同意市況可能仍然 choppy，短線淡倉未必再划算",
        "summary": [
            "觀眾問：係咪同意好多股票仍然未有新升勢嘅好 setup，市況可能仲喺一個 choppy range？佢話同意，好多股票仍然喺所有阻力、所有下降均線下面。但短線有啲已經有少少伸延：連續跳空同好寬嘅大陰線向下，所以短線淡倉嘅風險回報未必好，可能係 cover shorts 嘅時候。收結前（1:02:23 起）再講應該放慢、等市況沉澱、整底、等波動下降，並觀察反彈同 fade 時個別股票嘅表現；覺得而家未必係最好嘅交易環境，可能正進入一個偏亂嘅市場，除非見到急轉彎。",
        ],
        "card": "好多股票仍在阻力同下降均線下面，未有新升勢嘅好 setup。連續跳空同大陰線之後，短線淡倉風險回報未必好。收結叫放慢、整底、觀察 bounce 同 fade。",
        "charts": [
            {
                "anchor": "chart-soxx",
                "toc": "SOXX 日線",
                "kicker": "圖一",
                "title": "SOXX 日線：仍然喺下降均線／阻力下面",
                "time": "直播 58:15",
                "annotated": "images/choppy-cover/01_soxx_daily_5815.jpg",
                "source": "images/choppy-cover/src_soxx_daily_5815.jpg",
                "caption": "圖一 · SOXX 日線 · 直播 58:15。價格已經低過呢堆均線；佢同意好多股票未有新升勢嘅好 setup。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 SOXX 日線圖：標示仍喺下降均線／阻力下面，以及價格已經低過呢堆均線。",
                "alt_source": "直播原畫面：SOXX 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "57:57–58:21 · 'declining EMAs' 按 YouTube；Whisper v2 聽到 declining gmas。標點為閱讀而加",
                                "en": "Do you agree that many stocks still not has a great setup for a new uptrend, so the market may still in a choppy range? Yes, like yes, and a lot of the stock is still under all the resistance, under all the declining EMAs.",
                            },
                        ],
                        "yc": "你同唔同意好多股票仍然未有一個新升勢嘅好 setup，所以市況可能仲喺一個 choppy 嘅區間？係，同意。好多股票仍然喺所有阻力下面，喺所有下降緊嘅 EMA 下面。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "半導體呢度用嚟示範「仍在下降均線下面」：價格喺右邊一堆向下嘅均線之下。呢句係市況判斷，唔等於叫人而家先至新開淡倉。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-vst",
                "toc": "VST 日線",
                "kicker": "圖二",
                "title": "VST 日線：好寬嘅大陰線，短線已經伸延",
                "time": "直播 59:28",
                "annotated": "images/choppy-cover/02_vst_daily_5928.jpg",
                "source": "images/choppy-cover/src_vst_daily_5928.jpg",
                "caption": "圖二 · VST 日線 · 直播 59:28。右邊獨立嗰支好寬嘅大陰線，用來理解「wide red candles、淡倉有少少伸延」。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 VST 日線圖：標示右邊呢支好寬嘅大陰線。",
                "alt_source": "直播原畫面：VST 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "59:06–59:24 · 機器轉寫，標點為閱讀而加。呢句講緊時畫面掃過包括 VST 呢類大陰線",
                                "en": "But in the short run some stocks are getting a little bit extended, like we got some consecutive gap downs and wide red candles to the downside.",
                            },
                        ],
                        "yc": "但短線有啲股票已經有少少伸延，例如我哋見到一啲連續跳空，同埋向下好寬嘅大陰線。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "VST 右邊幾乎獨立嘅大陰線（當日約 −13.85%）就係呢類「wide red candles」嘅清楚例子。佢冇單獨把 VST 講成一筆交易，本頁只用嚟對照口中嘅形態。",
                        ],
                    },
                ],
            },
            {
                "anchor": "chart-qqq",
                "toc": "QQQ 日線",
                "kicker": "圖三 · 主圖",
                "title": "QQQ 日線：連續跳空同大陰線之後，可能係平淡倉嘅時候",
                "time": "直播 59:35",
                "annotated": "images/choppy-cover/03_qqq_daily_5935.jpg",
                "source": "images/choppy-cover/src_qqq_daily_5935.jpg",
                "caption": "圖三 · QQQ 日線 · 直播 59:35。近期連續跳空同大陰線後有反彈；上面仍然係下降均線。 點圖可放大。",
                "alt_annotated": "加咗註解嘅 QQQ 日線圖：標示連續跳空同大陰線之後，以及上面仍然係下降均線。",
                "alt_source": "直播原畫面：QQQ 日線，未加註解。",
                "blocks": [
                    {
                        "kind": "quote",
                        "lines": [
                            {
                                "meta": "59:20–1:00:15 · 'cover the shorts' 按 YouTube；Whisper v2 聽到 shots。標點為閱讀而加",
                                "en": "So in the short run I think the risk reward of shorting may not be that good, and probably it's a good time to cover the shorts.",
                            },
                        ],
                        "yc": "所以短線嚟講，我覺得淡倉嘅風險回報未必咁好，而且可能係平掉淡倉嘅時候。",
                        "note": "收結（1:02:23–1:03:58）畫面多數仍然係 QQQ 日線（1:03:20 附近掃過 MDB，本頁唔另出圖）。原話按 YouTube「during the fade」（Whisper v2 聽到 bait），以及語境把 building some basis 讀成 bases：I think it's time to slow down a little bit and letting things to settle down, or like building some bases, letting the volatility to come down, and also observing the individual stocks actions during the bounce or during the fade. I think not really the best trading environment right now. I think maybe we're entering a choppy market, and unless we are seeing some sharp turns.\n譯：我覺得係時候放慢少少，等事情沉澱，或者整一啲底，等波動下降，亦觀察個別股票喺反彈或者 fade 期間點走。我覺得而家未必係最好嘅交易環境。我估我哋可能正進入一個偏亂嘅市場，除非見到一啲急轉彎。\n可選原畫面備份：images/choppy-cover/src_qqq_daily_10255.jpg（1:02:55，同 59:35 好接近，所以唔再註解多一張）。",
                    },
                    {
                        "kind": "read",
                        "paragraphs": [
                            "59:28 係 VST，59:30 係 GLW，到 59:35 先穩定喺 QQQ 日線。本頁用 59:35 做大市圖。QQQ 近期有連續跳空同大陰線，然後出現反彈，上面仍然係下降緊嘅均線——正好同時說明「短線淡倉已經伸延」同「未等於新升勢已經成立」。",
                            "呢句係管理已有淡倉嘅判斷，唔係叫人新開淡倉，亦冇講要全部平定、平喺邊個價。",
                        ],
                    },
                ],
            },
        ],
        "notes_title": "注意事項",
        "notes": [
            "圖上中文註解係之後加上嘅學習說明，唔係直播畫面原本已有嘅字。可用「原畫面」對返未加字嘅截圖。",
            "畫面睇唔到成交價、倉位大細或者損益，所以本頁唔寫死呢啲數字。",
            "圖例多數只有顏色同數值，冇印均線周期。本頁唔會把某條彩線寫死成某個周期；如果佢有講周期，只標「佢口中嘅位置就喺呢附近」。",
            "原話來自機器轉寫（faster-whisper large-v3-turbo，並對照 YouTube 自動英文字幕），並非逐字人工校對。標點為閱讀而加。",
            "1:00:17–1:02:19 係職業／謙虛問答，唔係讀圖，所以唔獨立成科。",
            "59:30 嘅 GLW、1:03:20 嘅 MDB 只係快速翻圖，冇獨立分析點，故唔出圖。",
            "本頁只拆市況同淡倉管理呢段（約 57:59–1:00:15，並附 1:02:23–1:03:58 收結），冇混入其他系統或者規則。",
        ],
    },
]

SUBJECTS: list[dict] = FIRST_HALF + SECOND_HALF

# One entry per livestream. Add a date here when another stream is ready.
# Subjects stay in time order; do not split a stream into display groups.
STREAMS: list[dict] = [
    {
        "id": "2026-11-04",
        "date_label": "2026年11月4日",
        "page": "2026-11-04.html",
        "title": "《Flipped long》",
        "eyebrow": "2026年11月4日",
        "subtitle": "技術分析科目",
        "meta": "Martin Luk · 開播 22:26（台北時間） · 全程重播約 1:04:14",
        "watch_label": "打開直播重播",
        "watch_url": YOUTUBE,
        "card": "由開場到完結，有讀圖嘅段落按時間順序排。",
        "summary_kicker": "概要",
        "summary_title": "呢一場可以學嘅技術分析",
        "summary": [
            "呢一頁係 Martin Luk《Flipped long》（2026年11月4日）入面，佢用圖解釋市場結構、形態、位置、均線，或者說明點解咁做嘅段落，由開場到直播完結（約 1:04:14）。長空白、閒聊，同冇講分析嘅快速翻圖，唔會單獨成科。",
            "每科都有加咗字嘅圖，可以切返原畫面。圖上中文註解係之後加上嘅讀圖說明，唔係直播畫面原本已有嘅字。「原話」係英文轉寫，再附粵語對譯；「點樣讀」係我哋嘅說明，兩者分開。轉寫係機器轉寫（faster-whisper，並對照 YouTube 自動字幕），並非逐字人工校對。",
        ],
        "notes_title": "注意事項",
        "notes": [
            "09:13 至 22:43 大約 13 分鐘幾乎冇對白，畫面主要係翻睇不同股票，本站唔會做成圖冊。",
            "30:00 之後亦有唔少靜音翻圖、閒聊同測試對話，例如 30:10–30:48 斷線／咪高峰測、32:15–33:27 靜音翻圖、39:41–43:57「I'm selling Crowd」玩笑測試、45:45–47:45 SPCE 靜音、52:25–56:13 問書同新聞、1:00:17–1:02:19 職業問答。呢啲唔會單獨成科。",
            "畫面睇唔到成交價、倉位大細或者損益，所以各科都唔寫死呢啲數字。",
            "YouTube 自動字幕有時會把 MSTR 聽成 MSTL、把 50 EMA 聽成 “50-year may” 或者 “15 year maybe”；Whisper 有時把 longs 聽成 loans、mean reversion 聽成 mini version、cover the shorts 聽成 shots。本站按畫面同較合理嘅一方更正，並喺該科附註說明。",
        ],
        "subjects": SUBJECTS,
    },
    STREAM_2026_11_03,
    STREAM_2026_11_02,
    STREAM_2026_10_28,
    STREAM_2026_10_27,
]


def subject_by_id(subject_id: str) -> dict | None:
    for stream in STREAMS:
        for subject in stream["subjects"]:
            if subject["id"] == subject_id:
                return subject
    return None


def stream_by_id(stream_id: str) -> dict | None:
    for stream in STREAMS:
        if stream["id"] == stream_id:
            return stream
    return None


def stream_for_subject(subject_id: str) -> dict | None:
    for stream in STREAMS:
        for subject in stream["subjects"]:
            if subject["id"] == subject_id:
                return stream
    return None


def image_rels() -> list[str]:
    rels: list[str] = []
    for stream in STREAMS:
        for subject in stream["subjects"]:
            for chart in subject["charts"]:
                rels.append(chart["annotated"])
                rels.append(chart["source"])
    return rels


def missing_images(root: Path) -> list[str]:
    return [rel for rel in image_rels() if not (root / rel).is_file()]
