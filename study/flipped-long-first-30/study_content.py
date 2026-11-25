"""Teaching content for the Flipped long first-30 study app.

Text is copied from the static HTML pages in this folder. Do not add fill
prices, size, or P&L. The second half of the 4 Nov 2026 stream is prepared
separately: append those subjects to SECOND_HALF when their pages and images
exist. Each subject uses the same keys as the entries in FIRST_HALF.
"""

from __future__ import annotations

from pathlib import Path

YOUTUBE = "https://www.youtube.com/watch?v=NUT6d6Hvbmw"

INDEX = {
    "id": "index",
    "eyebrow": "科目目錄",
    "title": "《Flipped long》頭 30 分鐘",
    "subtitle": "技術分析科目",
    "meta": "Martin Luk · 2026年11月4日 · 開頭 30:00 · 全程重播約 1:04:14",
    "watch_label": "打開直播重播",
    "watch_url": YOUTUBE,
    "banner": "呢份係教育拆解，方便之後 review 點樣用形態、位置同均線讀圖，唔係投資建議。",
    "summary_kicker": "概要",
    "summary_title": "頭 30 分鐘入面，可以學嘅技術分析",
    "summary": [
        "呢個本地網站收錄 Martin Luk《Flipped long》（2026年11月4日）開頭 30 分鐘入面，佢用圖解釋市場結構、形態、位置、均線，或者說明點解咁做嘅段落。長空白、閒聊，同冇講分析嘅快速翻圖，唔會單獨成科。",
        "每科都有加咗字嘅圖，可以切返原畫面。圖上中文註解係之後加上嘅讀圖說明，唔係直播畫面原本已有嘅字。「原話」係英文轉寫，再附粵語對譯；「點樣讀」係我哋嘅說明，兩者分開。轉寫係機器轉寫（faster-whisper，並對照 YouTube 自動字幕），並非逐字人工校對。",
    ],
    "notes_title": "注意事項",
    "notes": [
        "09:13 至 22:43 大約 13 分鐘幾乎冇對白，畫面主要係翻睇不同股票，本站唔會做成圖冊。",
        "畫面睇唔到成交價、倉位大細或者損益，所以各科都唔寫死呢啲數字。",
        "YouTube 自動字幕有時會把 MSTR 聽成 MSTL、把 50 EMA 聽成 “50-year may”；本站按 Whisper 同畫面更正。",
    ],
    "disclaimer": "免責聲明：呢份係教育拆解，方便之後 review 讀圖方法，唔係投資建議，亦唔好當作買賣指示。",
    "later_note": "後半段（約 30:00 之後）另外準備緊，呢度未收錄。",
}

_COMMON_BANNER = "呢份係教育拆解，方便之後 review 形態同位置嘅讀法，唔係投資建議。"
_COMMON_DISCLAIMER = "免責聲明：呢份係教育拆解，唔係投資建議，亦唔好當作買賣指示。"

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
        "banner": _COMMON_BANNER,
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
        "disclaimer": _COMMON_DISCLAIMER,
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
        "banner": _COMMON_BANNER,
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
        "disclaimer": _COMMON_DISCLAIMER,
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
        "banner": _COMMON_BANNER,
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
        "disclaimer": _COMMON_DISCLAIMER,
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
        "banner": _COMMON_BANNER,
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
        "disclaimer": _COMMON_DISCLAIMER,
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
        "banner": _COMMON_BANNER,
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
        "disclaimer": _COMMON_DISCLAIMER,
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
        "banner": _COMMON_BANNER,
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
        "disclaimer": "免責聲明：呢份係教育拆解，方便之後 review 點樣用形態同位置讀圖，唔係投資建議，亦唔好當作買賣指示。",
    },
]

# The second half of the 4 Nov 2026 stream is prepared separately and is not
# ready. Append subject dicts here later. Leave this empty until each new
# subject has its text plus annotated and source images.
SECOND_HALF: list[dict] = []

SUBJECTS: list[dict] = FIRST_HALF + SECOND_HALF


def subject_by_id(subject_id: str) -> dict | None:
    for subject in SUBJECTS:
        if subject["id"] == subject_id:
            return subject
    return None


def image_rels() -> list[str]:
    rels: list[str] = []
    for subject in SUBJECTS:
        for chart in subject["charts"]:
            rels.append(chart["annotated"])
            rels.append(chart["source"])
    return rels


def missing_images(root: Path) -> list[str]:
    return [rel for rel in image_rels() if not (root / rel).is_file()]
