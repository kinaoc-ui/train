#!/usr/bin/env python3
"""Study content for Strong bounce | 27 Oct 2026."""

from __future__ import annotations

YT = "https://www.youtube.com/watch?v=cxh5np47P9w"
DATE = "2026年10月27日"
STREAM_TITLE = "《Strong bounce》"
WHISPER_META = "機器轉寫，標點為閱讀而加；主要跟 faster-whisper large-v3-turbo float32，並對照 YouTube 自動英文字幕"


def _meta(when: str) -> str:
    return f"Martin Luk · {STREAM_TITLE} · {DATE} · 時間碼 {when}"


def q(meta, en, yc, note=None):
    b = {"kind": "quote", "lines": [{"meta": meta, "en": en}], "yc": yc}
    if note:
        b["note"] = note
    return b


def r(*paragraphs):
    return {"kind": "read", "paragraphs": list(paragraphs)}


def chart(anchor, toc, kicker, title, time, annotated, source, caption, alt_a, alt_s, blocks):
    if "點圖可放大" not in caption:
        caption = caption.rstrip("。") + "。 點圖可放大。"
    return {
        "anchor": anchor,
        "toc": toc,
        "kicker": kicker,
        "title": title,
        "time": time,
        "annotated": annotated,
        "source": source,
        "caption": caption,
        "alt_annotated": alt_a,
        "alt_source": alt_s,
        "blocks": blocks,
    }


SUBJECTS: list[dict] = [

    {
        "id": "nq-declining-emas",
        "pager_name": "彈入下降均線，淡倉唔再加碼",
        "when": "06:11–07:07",
        "nav": "彈入下降均線，淡倉唔再加碼",
        "eyebrow": "科目一",
        "title": "彈入下降均線，淡倉唔再加碼",
        "subtitle": "大市行入阻力，軟件偏強，捱沽嘅半導體或會彈返均線",
        "meta": _meta("06:11–07:07"),
        "watch_label": "由 06:11 觀看直播片段",
        "watch_url": f"{YT}&t=371s",
        "description": "Martin Luk 直播拆解：NQ 彈入下降均線後唔再加淡倉，並提到軟件偏強同捱沽半導體或會彈返 9、21 甚至 50。",
        "summary_kicker": "概要",
        "summary_title": "開場先讀大市位置，再解釋點解唔加碼",
        "summary": [
            "06:11 開始，佢話今日未見到好多嘢，雖然大市彈高少少，但而家行入阻力、就係下降中嘅 EMAs。自己淡倉曝險已經偏高，所以唔打算再加碼。同時軟件幾強，大市都有機會轉高。一啲捱沽嘅半導體已經向下有少少延伸，或會彈返 9、21，甚至 50。",
            "畫面先係 NQ 日線，之後睇 IGV、AAOI。Whisper 把 beaten-down semi names 聽成 bid and down semi names。圖例冇印均線週期。",
        ],
        "card": "NQ 彈入下降均線，淡倉已經偏重所以唔加碼。軟件（IGV）偏強，大市有機會轉高；捱沽嘅半導體（AAOI）或會彈返 9、21 甚至 50。",
        "charts": [
            chart(
                "chart-nq-0625", "NQ 日線 06:25", "圖一",
                "NQ 日線：彈起後行入下降均線",
                "直播 06:25",
                "images/nq-declining-emas/01_nq_daily_0625.jpg",
                "images/nq-declining-emas/src_01_nq_daily_0625.jpg",
                "圖一 · NQ 日線 · 直播 06:25。註解標示價格彈起後行入下降均線，以及淡倉曝險已偏高所以唔再加碼。",
                "加咗註解嘅 NQ 日線：標示彈入下降均線，同唔再加淡倉。",
                "直播原畫面：NQ 日線，未加註解。",
                [
                    q(
                        f"06:11–06:41 · {WHISPER_META}",
                        "Not seeing much today, although the market is bouncing high a little bit, but it's now reeling into the resistance, the declining EMAs, but I've already got pretty high exposure on the short side, so I'm not gonna double down on this one I guess.",
                        "今日未見到好多嘢。雖然大市彈高少少，但而家行入阻力，就係下降中嘅 EMAs。我淡倉嗰邊曝險已經偏高，所以估唔會再喺呢個位置加碼。",
                    ),
                    r(
                        "呢一步係先讀大市位置，再解釋點解唔加淡倉。原話係行入下降均線嘅阻力，而唔係已經確認轉勢。",
                        "畫面係 NQ#1 日線（Nasdaq 100 E-mini）。圖例冇印均線週期；下降 EMAs 以口中同位置為準。",
                    ),
                ],
            ),
            chart(
                "chart-igv-0710", "IGV 日線 07:10", "圖二",
                "IGV：軟件偏強，大市有機會轉高",
                "直播 07:10",
                "images/nq-declining-emas/02_igv_daily_0710.jpg",
                "images/nq-declining-emas/src_02_igv_daily_0710.jpg",
                "圖二 · IGV 日線 · 直播 07:10。註解標示軟件相對強，以及呢點令大市都有機會轉高。",
                "加咗註解嘅 IGV 日線：標示軟件偏強。",
                "直播原畫面：IGV 日線，未加註解。",
                [
                    q(
                        "06:43–06:51 · 機器轉寫，標點為閱讀而加",
                        "And also like the softwares are pretty strong, there's the chance that the market can turn higher.",
                        "而且軟件幾強，大市都有機會轉高。",
                    ),
                    r(
                        "軟件強係佢唔加碼嘅另一個理由：大市仍有轉高嘅可能。",
                        "畫面標題寫住 iShares 軟件 ETF，只當圖上文字。",
                    ),
                ],
            ),
            chart(
                "chart-aaoi-0700", "AAOI 日線 07:00", "圖三",
                "AAOI：捱沽嘅半導體或會彈返 9、21 甚至 50",
                "直播 07:00",
                "images/nq-declining-emas/03_aaoi_daily_0700.jpg",
                "images/nq-declining-emas/src_03_aaoi_daily_0700.jpg",
                "圖三 · AAOI 日線 · 直播 07:00。註解標示向下延伸後嘅半導體例子，以及或會彈返 9、21 甚至 50。",
                "加咗註解嘅 AAOI 日線：標示或會彈返均線。",
                "直播原畫面：AAOI 日線，未加註解。",
                [
                    q(
                        "06:51–07:07 · 機器轉寫，標點為閱讀而加",
                        "And with together with some like bid and down semi names, some are a little bit overextended to the downside, that could have, like, that could get a pull back into the maybe the 9 and 21 or even the 50.",
                        "再加埋一啲捱沽嘅半導體，有啲已經向下有少少延伸，噉或會彈返大概 9 同 21，甚至 50。",
                        "Whisper 寫成 bid and down semi names；對照語境同 AAOI 畫面，較合理嘅聽法係 beaten-down semi names。9、21、50 以口中為準，圖例冇印週期。",
                    ),
                    r(
                        "呢度唔係叫即刻淡 AAOI，而係話呢類已經向下延伸嘅半導體，有機會彈返均線。",
                        "畫面標題 Applied Optoelectronics，只當圖上文字。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "開場 03:45–06:10 係問候同空白，唔單獨成科。06:50 前後亦掃過 PANW，作為軟件偏強嘅例子，重點用 IGV 出圖。",
            "07:39–07:55 只有一句「maybe SpaceX short」，並翻到 SPCX 日線，冇展開讀圖，唔單獨成科。",
        ],
    },

    {
        "id": "spy-resistance",
        "pager_name": "都喺阻力，想睇市場點反應",
        "when": "13:26–13:40",
        "nav": "都喺阻力，想睇市場點反應",
        "eyebrow": "科目二",
        "title": "都喺阻力，想睇市場點反應",
        "subtitle": "下降均線上嘅反應仲未見到",
        "meta": _meta("13:26–13:40"),
        "watch_label": "由 13:26 觀看直播片段",
        "watch_url": f"{YT}&t=806s",
        "description": "Martin Luk 直播拆解：指數同相關品種都到咗下降均線阻力，想先睇市場點反應。",
        "summary_kicker": "概要",
        "summary_title": "位置到咗，先睇反應",
        "summary": [
            "13:26 佢話想睇市場點樣反應呢啲下降 EMAs：而家佢哋都到咗阻力位置，自己好想知道呢次反應會點。畫面先係 SPY 日線，隨即翻到 SPCX 小時圖。",
        ],
        "card": "SPY 等已經去到下降均線阻力，想先睇反應。跟住亦翻到 SPCX 小時圖。",
        "charts": [
            chart(
                "chart-spy-1335", "SPY 日線 13:35", "圖一",
                "SPY 日線：已經去到阻力",
                "直播 13:35",
                "images/spy-resistance/01_spy_daily_1335.jpg",
                "images/spy-resistance/src_01_spy_daily_1335.jpg",
                "圖一 · SPY 日線 · 直播 13:35。註解標示價格靠近下降均線叢，以及佢想睇市場點反應。",
                "加咗註解嘅 SPY 日線：標示去到阻力。",
                "直播原畫面：SPY 日線，未加註解。",
                [
                    q(
                        f"13:26–13:40 · {WHISPER_META}",
                        "Let's see how the market reacts to this, declining EMAs. Like all of them are now at the resistance level. Really curious to see the reaction.",
                        "睇下市場點樣反應呢啲下降 EMAs。而家佢哋都到咗阻力位置。我真係好想知道呢次反應會點。",
                    ),
                    r(
                        "呢段冇新規則，只係把開場講過嘅下降均線阻力再核對一次，並且明確話要等反應。",
                        "圖例冇印均線週期。",
                    ),
                ],
            ),
            chart(
                "chart-spcx-1340", "SPCX 小時 13:40", "圖二",
                "SPCX 小時圖亦靠近均線",
                "直播 13:40",
                "images/spy-resistance/02_spcx_hourly_1340.jpg",
                "images/spy-resistance/src_02_spcx_hourly_1340.jpg",
                "圖二 · SPCX 小時圖 · 直播 13:40。註解標示講完「都到咗阻力」之後翻到呢張，以及畫面公司名只當圖上文字。",
                "加咗註解嘅 SPCX 小時圖：標示靠近均線。",
                "直播原畫面：SPCX 小時圖，未加註解。",
                [
                    r(
                        "「all of them」係口中複數，畫面由 SPY 轉到 SPCX。唔好把呢張單獨讀成已經確認嘅淡倉訊號。",
                        "畫面寫住 Space Exploration Technologies Corp，只當圖上文字；代碼以分頁 SPCX 為準。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "13:40 之後到 25:42 大約 12 分鐘幾乎冇對白，主要係翻圖，唔做成圖冊。",
            "08:43–12:07 同 25:42–27:00 係執行風格、坐咗場外同加倉流程嘅問答，冇對應走圖教學，唔單獨成科。",
        ],
    },


    {
        "id": "nbis-gap-9",
        "pager_name": "NBIS：彈入下降 9 同未補缺口",
        "when": "31:41–32:33",
        "nav": "NBIS：彈入下降 9 同未補缺口",
        "eyebrow": "科目三",
        "title": "NBIS：彈入下降 9 同未補缺口",
        "subtitle": "自身形態、相對弱勢，又同大市同步",
        "meta": _meta("31:41–32:33"),
        "watch_label": "由 31:41 觀看直播片段",
        "watch_url": f"{YT}&t=1901s",
        "description": "Martin Luk 直播拆解：NBIS 急彈入下降 9 同未補缺口，再加相對弱勢同大市同步，覺得係好淡倉。",
        "summary_kicker": "概要",
        "summary_title": "聊天室問 NBIS，佢覺得形態同位置都齊",
        "summary": [
            "31:41 聊天室多人問 Nerebius／NBIS 好唔好淡。佢覺得好：唔單止自身圖好睇，仲有急彈入下降 9、未補缺口、相對弱勢，而且同大市同步。",
            "Whisper 把 NBIS 聽成 Nerebius，把 short 聽成 shot；以畫面 Nebius Group N.V.（NBIS）為準。",
        ],
        "card": "NBIS 急彈入下降 9 同未補缺口，再加相對弱勢同大市同步，覺得係好淡倉。字幕聽成 Nerebius。",
        "charts": [
            chart(
                "chart-nbis-3200", "NBIS 日線 32:00", "圖一",
                "NBIS 日線：急彈入下降 9 同未補缺口",
                "直播 32:00",
                "images/nbis-gap-9/01_nbis_daily_3200.jpg",
                "images/nbis-gap-9/src_01_nbis_daily_3200.jpg",
                "圖一 · NBIS 日線 · 直播 32:00。註解標示急彈入下降 9 同未補缺口，以及相對弱勢又同大市同步。",
                "加咗註解嘅 NBIS 日線：標示彈入下降 9 同缺口。",
                "直播原畫面：NBIS 日線，未加註解。",
                [
                    q(
                        f"31:41–32:33 · {WHISPER_META}",
                        "Nerebius, so many of you guys asking Nerebius is a good short. 9 EMA. Yeah, I think it's a good one. Not only it looks great on its own chart, a really quick bounce into the declining 9 and also into this unfilled gap level. Relative weakness, and also the market, it also synchronized with the markets too.",
                        "Nerebius，你好多人問 Nerebius 好唔好淡，9 EMA。係，我覺得係好淡倉。唔單止佢自己張圖好睇，仲有一次好急嘅反彈，彈入下降中嘅 9，亦彈入呢個未補缺口。相對弱勢，而且同大市都同步。",
                        "Whisper 把 NBIS 聽成 Nerebius，把 short 聽成 shot。畫面係 Nebius Group N.V.（NBIS），以畫面為準。9 EMA 以口中為準，圖例冇印週期。",
                    ),
                    r(
                        "佢把「自身圖、下降 9、未補缺口、相對弱勢、同大市同步」疊埋一齊，先話呢個淡倉幾好。",
                        "畫面公司名只當圖上文字。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "講 NBIS 之前畫面曾經停喺 QQQ 小時圖，對白轉到 NBIS 之後先切日線。",
        ],
    },

    {
        "id": "indices-soxx-timing",
        "pager_name": "指數同 SOXX 對齊，今日淡倉時機",
        "when": "32:33–33:17",
        "nav": "指數同 SOXX 對齊，今日淡倉時機",
        "eyebrow": "科目四",
        "title": "指數同 SOXX 對齊，今日淡倉時機",
        "subtitle": "三個指數彈入下降均線，半導體 ETF 亦入下降 9",
        "meta": _meta("32:33–33:17"),
        "watch_label": "由 32:33 觀看直播片段",
        "watch_url": f"{YT}&t=1953s",
        "description": "Martin Luk 直播拆解：三個指數彈入下降 EMAs，SOXX 亦入下降 9，覺得今日淡半導體嘅時機較好。",
        "summary_kicker": "概要",
        "summary_title": "大市同板塊同一時間對齊",
        "summary": [
            "32:33 佢把 NBIS 嘅讀法拉闊到大市：覺得今日整體淡倉時機都幾好，因為三個指數都彈入下降 EMAs，半導體 ETF 亦彈入下降 9。所以覺得今日淡邊隻半導體都得；又話可能講得誇張少少，但普遍都認為入場可以。",
            "呢一段畫面見到 SPY、QQQ 日線同 SOXX 日線。口中「all three indices」，呢段未清楚見到 IWM。字幕把 semis ETF 聽成 sami's ETF。",
        ],
        "card": "SPY、QQQ 彈入下降均線，SOXX 彈入下降 9，覺得今日淡半導體時機較好，甚至話淡邊隻都可以。",
        "charts": [
            chart(
                "chart-spy-3244", "SPY 日線 32:44", "圖一",
                "SPY 日線：彈入下降均線",
                "直播 32:44",
                "images/indices-soxx-timing/01_spy_daily_3244.jpg",
                "images/indices-soxx-timing/src_01_spy_daily_3244.jpg",
                "圖一 · SPY 日線 · 直播 32:44。註解標示彈入下降均線，以及口中三個指數一齊對齊。",
                "加咗註解嘅 SPY 日線：標示彈入下降均線。",
                "直播原畫面：SPY 日線，未加註解。",
                [
                    q(
                        f"32:33–32:47 · {WHISPER_META}",
                        "I think today we got a really good short timing. I think today's a really good short timing for the general market as well. The all three indices are rallying into the declining EMAs, so all things aligned.",
                        "我覺得今日有一個好好嘅淡倉時機。我覺得今日對整體大市嚟講，都係好好嘅淡倉時機。三個指數都彈入下降中嘅 EMAs，所以所有嘢都對齊咗。",
                    ),
                    r(
                        "「all things aligned」係指指數一齊行入下降均線，而唔係另有一套未講嘅條件清單。",
                        "口中 all three indices；呢幾秒畫面係 SPY 同隨後嘅 QQQ，未清楚見到第三個指數。",
                    ),
                ],
            ),
            chart(
                "chart-qqq-3247", "QQQ 日線 32:47", "圖二",
                "QQQ 日線：同樣彈入下降均線",
                "直播 32:47",
                "images/indices-soxx-timing/02_qqq_daily_3247.jpg",
                "images/indices-soxx-timing/src_02_qqq_daily_3247.jpg",
                "圖二 · QQQ 日線 · 直播 32:47。註解標示同樣彈入下降均線，以及畫面基金名稱只當圖上文字。",
                "加咗註解嘅 QQQ 日線：標示彈入下降均線。",
                "直播原畫面：QQQ 日線，未加註解。",
                [
                    r(
                        "QQQ 同 SPY 一齊用，係為咗核對「指數都彈入下降均線」呢句。",
                        "畫面寫住 Invesco QQQ Trust, Series 1，只當圖上文字。圖例冇印週期。",
                    ),
                ],
            ),
            chart(
                "chart-soxx-3256", "SOXX 日線 32:56", "圖三",
                "SOXX 日線：亦彈入下降 9",
                "直播 32:56",
                "images/indices-soxx-timing/03_soxx_daily_3256.jpg",
                "images/indices-soxx-timing/src_03_soxx_daily_3256.jpg",
                "圖三 · SOXX 日線 · 直播 32:56。註解標示半導體 ETF 彈入下降 9，以及佢覺得今日淡邊隻半導體都得。",
                "加咗註解嘅 SOXX 日線：標示彈入下降 9。",
                "直播原畫面：SOXX 日線，未加註解。",
                [
                    q(
                        "32:47–33:17 · 機器轉寫，標點為閱讀而加",
                        "And also semis ETF into the declining 9 as well. So to me, I think if you're shorting any semis, that would be a good entry. Maybe it's a little bit exaggerated, but I generally believe, like, just pick any semi stocks to short today. I think they are all good entries.",
                        "而且半導體 ETF 亦彈入下降中嘅 9。所以對我嚟講，如果你淡任何半導體，都會係一個好入場。可能講得誇張少少，但我普遍都相信，今日淡邊隻半導體都得。我覺得佢哋全部都係好入場。",
                        "Whisper 把 semis 聽成 sami's／samis／semi stops。畫面係 iShares PHLX SOX Semiconductor Sector Index Fund（SOXX），以畫面為準。",
                    ),
                    r(
                        "「pick any semi stocks」係當時對板塊位置嘅概括，佢自己都話可能誇張少少。唔好當成每隻半導體都有同一規則。",
                        "9 EMA 以口中為準，圖例冇印週期。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "口中 all three indices，呢段清楚見到 SPY 同 QQQ；IWM 要到直播後段先獨立出圖。唔擅自補一張當時未定影嘅 IWM。",
        ],
    },

    {
        "id": "amd-soxx-9",
        "pager_name": "AMD 同 SOXX：21 同缺口上嘅 9",
        "when": "36:21–37:29",
        "nav": "AMD 同 SOXX：21 同缺口上嘅 9",
        "eyebrow": "科目五",
        "title": "AMD 同 SOXX：21 同缺口上嘅 9",
        "subtitle": "AMD 入場覺得有效，但更想淡半導體 ETF",
        "meta": _meta("36:21–37:29"),
        "watch_label": "由 36:21 觀看直播片段",
        "watch_url": f"{YT}&t=2181s",
        "description": "Martin Luk 直播拆解：AMD 在 21 EMA 同先前高位仍然係好淡倉，但佢更想淡已經彈入未補缺口同 9 EMA 嘅 SOXX。",
        "summary_kicker": "概要",
        "summary_title": "同一板塊，兩隻嘅位置都講清楚",
        "summary": [
            "36:21 提到 AMD 在 21 EMA、先前高位，覺得係好淡倉，入場有效。不過自己更想淡半導體 ETF：SOXX 而家彈入未補缺口同 9 EMA。",
            "中間 33:17–36:21 幾分鐘幾乎冇新對白。37:33 之後係 TQQQ 止蝕同成交量問答，冇走圖教學，唔另開一科。",
        ],
        "card": "AMD 在 21 EMA 同先前高位，入場覺得有效；但更想淡已彈入未補缺口同 9 EMA 嘅 SOXX。",
        "charts": [
            chart(
                "chart-amd-3700", "AMD 日線 37:00", "圖一",
                "AMD 日線：21 EMA 同先前高位",
                "直播 37:00",
                "images/amd-soxx-9/01_amd_daily_3700.jpg",
                "images/amd-soxx-9/src_01_amd_daily_3700.jpg",
                "圖一 · AMD 日線 · 直播 37:00。註解標示口中 21 EMA 同先前高位，以及佢覺得入場仍然有效。",
                "加咗註解嘅 AMD 日線：標示 21 EMA 同先前高位。",
                "直播原畫面：AMD 日線，未加註解。",
                [
                    q(
                        f"36:21–37:15 · {WHISPER_META}",
                        "AMD at 21 EMA in previous highs. Yeah, could be, but yeah, I think it's a great short. But I think I would like the shorts that are semis ETF a little bit more, but I think AMD is still a really nice short.",
                        "AMD 在 21 EMA、先前高位。可以係，我覺得係一個好好嘅淡倉。不過我更想淡半導體 ETF 嗰啲，但 AMD 我仍然覺得係好好嘅淡倉。",
                    ),
                    r(
                        "佢冇否定 AMD，只係相對更鍾意板塊 ETF 嘅位置。",
                        "21 EMA 以口中為準，圖例冇印週期。畫面 Advanced Micro Devices Inc. 只當圖上文字。",
                    ),
                ],
            ),
            chart(
                "chart-soxx-3714", "SOXX 日線 37:14", "圖二",
                "SOXX：彈入未補缺口同 9 EMA",
                "直播 37:14",
                "images/amd-soxx-9/02_soxx_daily_3714.jpg",
                "images/amd-soxx-9/src_02_soxx_daily_3714.jpg",
                "圖二 · SOXX 日線 · 直播 37:14。註解標示彈入未補缺口同 9 EMA，以及佢更想淡呢邊。",
                "加咗註解嘅 SOXX 日線：標示缺口同 9 EMA。",
                "直播原畫面：SOXX 日線，未加註解。",
                [
                    q(
                        "37:16–37:29 · 機器轉寫，標點為閱讀而加",
                        "I just like how weak the semis ETF is, and now it's bouncing right into the gap, unfilled gap at the 9 EMA. But still, AMD, I think the entry is pretty good. It's valid.",
                        "我只係鍾意半導體 ETF 有幾弱，而家佢就彈入呢個缺口，未補缺口，就在 9 EMA。不過 AMD，我仍然覺得入場幾好，係有效嘅。",
                        "Whisper 一度把 semis ETF 聽成 The same is ETFAs。以畫面 SOXX 為準。",
                    ),
                    r(
                        "同上一科嘅 SOXX 下降 9 係同一條思路，呢度再補「未補缺口」同「點解仲講 AMD」。",
                        "圖例冇印週期。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "37:33–38:14 有人問 TQQQ 會唔會仍然用 1% 止蝕，以及突破時點樣睇成交量。佢話入場多數唔睇成交量，成交量較多係做拋物線淡倉或者做多先會用。呢段冇對應走圖，唔單獨成科。提到嘅 1% 只保留問句原話，唔當可複製規則。",
        ],
    },

    {
        "id": "rklb-daily-hourly",
        "pager_name": "RKLB：日線 9 同小時 50",
        "when": "43:36–46:08",
        "nav": "RKLB：日線 9 同小時 50",
        "eyebrow": "科目六",
        "title": "RKLB：日線 9 同小時 50",
        "subtitle": "碰到日線 9，但守住小時 50；佢主要睇日線",
        "meta": _meta("43:36–46:08"),
        "watch_label": "由 43:36 觀看直播片段",
        "watch_url": f"{YT}&t=2616s",
        "description": "Martin Luk 直播拆解：RKLB 碰到日線 9 但仍在小時 50 之上；佢主要睇日線，覺得有少少延伸，但板塊弱而且同大市同步。",
        "summary_kicker": "概要",
        "summary_title": "日線同小時圖唔一致時，佢點取捨",
        "summary": [
            "43:36 聊天室問：今日淡倉碰到日線 9 EMA，但仍守住小時 50，價格又在小時 50 之上，仲算唔算好淡倉。佢話多數會以日線為主。Rocket Lab 對佢嚟講有少少延伸，但板塊好弱，今日呢次回調又同大市同步、一齊彈入下降 9，所以仍然當 fairly short。",
            "佢唔肯定有冇數據證明「淡喺 50 EMA 之上完全唔影響勝率」，只係自己唔太理會呢點；又話如果你淡喺 9 或者 50 之上，唔會在嗰啲位置加倉。字幕一度把 RKLB 聽成 rock a lap，之後 Whisper 清楚講 rocket lab。",
        ],
        "card": "RKLB 碰到日線 9，但仍在小時 50 之上。佢主要睇日線，覺得有少少延伸，但板塊弱而且同大市同步，仍然當可以淡。",
        "charts": [
            chart(
                "chart-rklb-4400", "RKLB 日線 44:00", "圖一",
                "RKLB 日線：彈入下降 9",
                "直播 44:00",
                "images/rklb-daily-hourly/01_rklb_daily_4400.jpg",
                "images/rklb-daily-hourly/src_01_rklb_daily_4400.jpg",
                "圖一 · RKLB 日線 · 直播 44:00。註解標示彈入下降 9，以及雖然有少少延伸，但板塊弱而且同大市同步。",
                "加咗註解嘅 RKLB 日線：標示彈入下降 9。",
                "直播原畫面：RKLB 日線，未加註解。",
                [
                    q(
                        f"43:36–45:32 · {WHISPER_META}",
                        "If short today, Rocket Lab, touches the daily 9 EMA but holding above the hourly 50, is it still a good short setup if the price is above hourly 50? Yeah, I get your point. Most of the time I will focus on the daily most. So Rocket Lab to me, I think it's a little bit extended, but yeah, it's a really weak sector, and I think today especially this pullback matches, it just correlates with the market, synchronized with the market, it's pulling back into the declining 9 at the same time, so I think it's still fine. I think I would still consider this is a fairly short.",
                        "如果今日淡 Rocket Lab，碰到日線 9 EMA，但守住小時 50，價格又在小時 50 之上，仲算唔算好淡倉？我明白你嘅意思。多數時候我會以日線為主。所以 Rocket Lab 對我嚟講，我覺得有少少延伸，但係，呢個板塊好弱，而且我覺得今日呢次回調啱啱同大市同步，一齊彈入下降中嘅 9，所以我覺得仍然可以。我仍然會當呢個係一個還可以嘅淡倉。",
                        "開首 Whisper 把 Rocket Lab 聽成 rock a lap；稍後同一段清楚講 rocket lab。以畫面 Rocket Lab Corporation（RKLB）為準。",
                    ),
                    r(
                        "取捨好清楚：小時 50 之上唔會自動取消呢個淡倉，因為佢主要睇日線，再加板塊同大市同步。",
                        "畫面公司名只當圖上文字。9、50 以口中為準，圖例冇印週期。",
                    ),
                ],
            ),
            chart(
                "chart-rklb-4410", "RKLB 小時 44:10", "圖二",
                "小時圖：問緊係咪仍在 50 之上",
                "直播 44:10",
                "images/rklb-daily-hourly/02_rklb_hourly_4410.jpg",
                "images/rklb-daily-hourly/src_02_rklb_hourly_4410.jpg",
                "圖二 · RKLB 小時圖 · 直播 44:10。註解標示聊天室問嘅小時 50，以及佢主要睇日線、唔肯定呢點會唔會改勝率。",
                "加咗註解嘅 RKLB 小時圖：標示小時 50 嘅疑問。",
                "直播原畫面：RKLB 小時圖，未加註解。",
                [
                    q(
                        "45:32–46:08 · 機器轉寫，標點為閱讀而加",
                        "But whether, like, do I have any data that really I'm very certain that shorting above the 50 EMA would really make no difference in the win rate? Like I'm not sure, but personally I don't really bother this one. As you're like shorting above the 9, above the 50, you're not going to add those levels, and I tend to focus more on the daily.",
                        "但係，我有冇數據令我好肯定，淡喺 50 EMA 之上真係完全唔會改到勝率？我唔肯定，但就我自己而言，我唔太理會呢點。如果你係淡喺 9 之上、淡喺 50 之上，你唔會在嗰啲位置加倉，而且我傾向更睇日線。",
                    ),
                    r(
                        "佢冇提供勝率數字，亦冇把「唔在 9／50 之上加倉」講成一條可以照抄嘅硬規則，只係說明自己點處理呢種位置。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "50:44–52:42 有人問應唔應捉升勢回調同跌勢反彈嘅細浪。佢話如果可以做大趨勢，就唔會為咗 3% 而放棄 30%，除非你在逆勢有好大優勢。呢段冇獨立走圖，唔單獨成科。",
        ],
    },

    {
        "id": "gev-earnings",
        "pager_name": "GEV 業績，傾向持有過市",
        "when": "54:13–54:27",
        "nav": "GEV 業績，傾向持有過市",
        "eyebrow": "科目七",
        "title": "GEV 業績，傾向持有過市",
        "subtitle": "聽日早上有業績，聊天室提醒之後先交代",
        "meta": _meta("54:13–54:27"),
        "watch_label": "由 54:13 觀看直播片段",
        "watch_url": f"{YT}&t=3253s",
        "description": "Martin Luk 直播拆解：聊天室提醒 GEV 聽日早上有業績，佢話大概會持有過業績。",
        "summary_kicker": "概要",
        "summary_title": "先回應業績時間，再決定點處理",
        "summary": [
            "54:13 聊天室提醒 GEV 聽日早上有業績。佢多謝提醒，並話自己大概會持有過呢次業績。畫面係 GEV 日線。",
        ],
        "card": "聊天室提醒 GEV 聽日早上有業績；佢話大概會持有過業績。",
        "charts": [
            chart(
                "chart-gev-5422", "GEV 日線 54:22", "圖一",
                "GEV 日線：聽日早上有業績",
                "直播 54:22",
                "images/gev-earnings/01_gev_daily_5422.jpg",
                "images/gev-earnings/src_01_gev_daily_5422.jpg",
                "圖一 · GEV 日線 · 直播 54:22。註解標示聽日早上有業績，以及佢話大概會持有過市。",
                "加咗註解嘅 GEV 日線：標示業績前傾向持有。",
                "直播原畫面：GEV 日線，未加註解。",
                [
                    q(
                        f"54:13–54:27 · {WHISPER_META}",
                        "GEV has earnings tomorrow morning. Thanks for reminding. I probably am going to hold it into the earnings.",
                        "GEV 聽日早上有業績。多謝提醒。我大概會持有過呢次業績。",
                    ),
                    r(
                        "呢句係當時對已有倉嘅打算，畫面睇唔到倉位大細或者損益，亦唔係叫人跟住持有過業績。",
                        "畫面 GE Vernova 只當圖上文字。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "呢科好短，但有對應走圖同持倉理由，所以獨立成科。",
        ],
    },

    {
        "id": "twst-avwap",
        "pager_name": "TWST：等錨定 VWAP 超調",
        "when": "54:38–56:32",
        "nav": "TWST：等錨定 VWAP 超調",
        "eyebrow": "科目八",
        "title": "TWST：等錨定 VWAP 超調",
        "subtitle": "拋物線後出現大陰線，但佢覺得仲偏強，所以自己唔淡",
        "meta": _meta("54:38–56:32"),
        "watch_label": "由 54:38 觀看直播片段",
        "watch_url": f"{YT}&t=3278s",
        "description": "Martin Luk 直播拆解：TWST 拋物線後出現大陰線，如果要淡會等錨定 VWAP 超調；但呢隻仍偏強，所以自己唔淡。",
        "summary_kicker": "概要",
        "summary_title": "形態可以討論，但仲有更弱嘅選擇",
        "summary": [
            "54:38 有人問，拋物線大升之後出現大分布陰線，可唔可以淡，並舉今日 TWST 為例。佢話如果要淡，會等錨定 VWAP 再超調，淡喺稍微高過呢條線或會最好；但自己唔會淡呢隻，因為外面仲有更弱嘅品種，而 TWST 仍然偏強。亦有可能只係第一個更低高位，但仍要證明。",
            "字幕把 anchored VWAP 聽成 angle view up 或者 coffee web。",
        ],
        "card": "TWST 拋物線後出現大陰線。如果要淡會等錨定 VWAP 超調；但佢覺得呢隻仍偏強，所以自己唔淡。",
        "charts": [
            chart(
                "chart-twst-5510", "TWST 日線 55:10", "圖一",
                "TWST 日線：拋物線後出現大陰線",
                "直播 55:10",
                "images/twst-avwap/01_twst_daily_5510.jpg",
                "images/twst-avwap/src_01_twst_daily_5510.jpg",
                "圖一 · TWST 日線 · 直播 55:10。註解標示拋物線後嘅大陰線，以及佢想等錨定 VWAP 超調、自己唔淡。",
                "加咗註解嘅 TWST 日線：標示大陰線同等錨定 VWAP。",
                "直播原畫面：TWST 日線，未加註解。",
                [
                    q(
                        f"54:38–56:32 · {WHISPER_META}",
                        "What's your opinion on shorts after a big distribution candle after a long parabolic run? For example, TWST today. If I have to short, I will wait for the anchored VWAP, like to wait for it to even overshoot the anchored VWAP. Shorting maybe slightly above it will be the best. But I think I'm not going to short this thing, because there are the weaker names out there. Like it's still pretty strong. Yeah, but I don't know, like it could be also like the first lower highs, but it has to prove it. I think overshooting the anchored VWAP will be the best.",
                        "拋物線大升之後出現大分布陰線，你點睇淡倉？例如今日 TWST。如果我要淡，我會等錨定 VWAP，甚至等佢超調呢條錨定 VWAP。淡喺稍微高過呢條線或會最好。但我想我唔會淡呢隻，因為外面仲有更弱嘅品種。呢隻仍然偏強。不過我唔知，佢亦有可能只係第一個更低高位，但要證明到。我覺得超調錨定 VWAP 會係最好。",
                        "Whisper 把 anchored VWAP 聽成 angle view up／angle for you；YouTube 字幕亦有 coffee web 一類聽法。呢度按同一直播先前用詞同語境寫成錨定 VWAP，並標明聽音分歧。",
                    ),
                    r(
                        "「如果要淡」同「我自己唔淡」要分開讀。位置條件講咗，但即時結論係仲有更弱嘅選擇，而且第一個更低高位仍未證明。",
                        "畫面 Twist Bioscience Corporation 只當圖上文字。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "錨定 VWAP 喺官方字幕同 Whisper 都聽得唔穩，本頁按語境同本站先前同一講者嘅用詞還原，並在該科標明。",
        ],
    },

    {
        "id": "mrvl-entries",
        "pager_name": "MRVL：日線可以淡，低週期有多個入場",
        "when": "57:35–58:36",
        "nav": "MRVL：日線可以淡，低週期有多個入場",
        "eyebrow": "科目九",
        "title": "MRVL：日線可以淡，低週期有多個入場",
        "subtitle": "5 分鐘跌破、1 分鐘 9，同錨定 VWAP 失敗奪回",
        "meta": _meta("57:35–58:36"),
        "watch_label": "由 57:35 觀看直播片段",
        "watch_url": f"{YT}&t=3455s",
        "description": "Martin Luk 直播拆解：MRVL 日線睇淡幾好；低週期可以用 5 分鐘跌破、1 分鐘收市低過 9 EMA，或者錨定 VWAP 失敗奪回。",
        "summary_kicker": "概要",
        "summary_title": "日線方向定咗，再喺低週期揀入場",
        "summary": [
            "57:35 有人話 Marvell 日線淡倉機會不錯，但低週期搵唔到理想入場，問佢會點拆。佢同意日線睇淡幾好，並指出 5 分鐘跌破好乾淨；1 分鐘收市低過 9 EMA 可以係另一個入場，錨定 VWAP 失敗奪回亦可以。上面有好多入場，錯過咗，下面次優位置都得。",
            "Whisper 把 Marvell 聽得清楚；1 minute 9 EMA 聽成 9 year make；anchored VWAP 聽成 coffee web。",
        ],
        "card": "MRVL 日線睇淡幾好。低週期可以用 5 分鐘跌破、1 分鐘收市低過 9 EMA，或者錨定 VWAP 失敗奪回；錯過上面，下面次優位置都得。",
        "charts": [
            chart(
                "chart-mrvl-5800", "MRVL 15 分鐘 58:00", "圖一",
                "MRVL 15 分鐘：跌破後嘅走勢",
                "直播 58:00",
                "images/mrvl-entries/01_mrvl_15_5800.jpg",
                "images/mrvl-entries/src_01_mrvl_15_5800.jpg",
                "圖一 · MRVL 15 分鐘 · 直播 58:00。註解標示低週期跌破後嘅走勢，以及上面有多個入場、下面亦有次優位置。",
                "加咗註解嘅 MRVL 15 分鐘：標示跌破同多個入場。",
                "直播原畫面：MRVL 15 分鐘，未加註解。",
                [
                    q(
                        f"57:35–58:36 · {WHISPER_META}",
                        "Marvell seems having a good short chance on the daily chart, however I can't really find an optimal entry point using lower time frames. Just wonder how you analyze this chart. Yeah, on the daily it looks pretty good on the short side. 5 minute breakdown, I think it's pretty clean. Breakdown of the 5 minute candle. Maybe even close below the 1 minute 9 EMA could be another entry, and AVWAP failed reclaim would be another entry. This one could be another entry. I think you got a lot of entries up here. If you missed the upper one, maybe you can also get these entries, the suboptimal ones down here, it's also possible.",
                        "Marvell 日線睇落有不錯嘅淡倉機會，但低週期搵唔到理想入場，想知道你會點拆呢張圖。係，日線喺淡嗰邊睇落幾好。5 分鐘跌破，我覺得好乾淨。5 分鐘 K 線嘅跌破。甚至 1 分鐘收市低過 9 EMA 都可以係另一個入場，錨定 VWAP 失敗奪回亦可以係另一個入場。呢個都可以係。我覺得上面有好多入場。如果你錯過上面嗰個，或者都可以攞呢啲下面嘅次優入場，都有可能。",
                        "Whisper 把 9 EMA 聽成 9 year make，把 anchored VWAP 聽成 coffee web。原話按語境還原，並標明聽音分歧。畫面係 Marvell Technology（MRVL）。",
                    ),
                    r(
                        "日線先定方向，低週期先至講具體入場。15 分鐘係跟住睇嘅畫面，口中明確提到嘅係 5 分鐘跌破。",
                        "畫面公司名只當圖上文字。圖例冇印週期。",
                    ),
                ],
            ),
            chart(
                "chart-mrvl-5830", "MRVL 1 分鐘 58:30", "圖二",
                "1 分鐘：收市低過 9 EMA 都可以入",
                "直播 58:30",
                "images/mrvl-entries/02_mrvl_1m_5830.jpg",
                "images/mrvl-entries/src_02_mrvl_1m_5830.jpg",
                "圖二 · MRVL 1 分鐘 · 直播 58:30。註解標示收市低過 9 EMA 可以係另一個入場，以及錨定 VWAP 失敗奪回。",
                "加咗註解嘅 MRVL 1 分鐘：標示 9 EMA 同錨定 VWAP。",
                "直播原畫面：MRVL 1 分鐘，未加註解。",
                [
                    r(
                        "呢張係口中「1 分鐘 9 EMA」同「AVWAP failed reclaim」對應嘅低週期畫面。唔好把每一種入場都寫成必須同時成立。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "講日線睇淡時，前幾秒畫面仍喺 QQQ，之後先切到 MRVL。日線判斷以口中為準，本頁用低週期圖對應入場講法。",
        ],
    },

    {
        "id": "ionq-vulnerable",
        "pager_name": "IONQ 睇落好脆弱",
        "when": "59:35–59:50",
        "nav": "IONQ 睇落好脆弱",
        "eyebrow": "科目十",
        "title": "IONQ 睇落好脆弱",
        "subtitle": "最好等彈入 21，或推入呢啲波段低位",
        "meta": _meta("59:35–59:50"),
        "watch_label": "由 59:35 觀看直播片段",
        "watch_url": f"{YT}&t=3575s",
        "description": "Martin Luk 直播拆解：IONQ 睇落好脆弱，但佢覺得最好等彈入 21，或者推入波段低位。",
        "summary_kicker": "概要",
        "summary_title": "脆弱唔等於即刻係最好入場",
        "summary": [
            "59:35 佢指住另一隻話睇落好脆弱。不過覺得最好仍係等彈入 21，或者推入呢啲波段低位。畫面係 IONQ 日線。Whisper 同字幕把 IONQ 聽成 Power and Q。",
        ],
        "card": "IONQ 睇落好脆弱，但最好等彈入 21，或推入波段低位。字幕聽成 Power and Q。",
        "charts": [
            chart(
                "chart-ionq-5936", "IONQ 日線 59:36", "圖一",
                "IONQ 日線：睇落好脆弱",
                "直播 59:36",
                "images/ionq-vulnerable/01_ionq_daily_5936.jpg",
                "images/ionq-vulnerable/src_01_ionq_daily_5936.jpg",
                "圖一 · IONQ 日線 · 直播 59:36。註解標示睇落好脆弱，以及最好等彈入 21 或推入波段低位。",
                "加咗註解嘅 IONQ 日線：標示脆弱同等 21。",
                "直播原畫面：IONQ 日線，未加註解。",
                [
                    q(
                        f"59:35–59:50 · {WHISPER_META}",
                        "One thumbs up, another short. IONQ right here looks very vulnerable. Although, I think the pullback into the 21 would be the best. Also, pushing into this swing lows.",
                        "再多一隻淡倉。IONQ 呢度睇落好脆弱。不過，我覺得彈入 21 會係最好。亦都係推入呢啲波段低位。",
                        "Whisper 同 YouTube 字幕把 IONQ 聽成 Power and Q。畫面係 IonQ, Inc.（IONQ），以畫面為準。前幾秒曾掃過 APLD，對白轉到「another short」時先係 IONQ。",
                    ),
                    r(
                        "「脆弱」同「最好入場」分開：而家睇落弱，但佢仍然想等 21 或者波段低位。",
                        "21 以口中為準，圖例冇印週期。畫面公司名只當圖上文字。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "原話開頭 One thumbs up 只係口頭帶過，唔另作分析。",
        ],
    },

    {
        "id": "sndk-oct9",
        "pager_name": "SNDK 10月9日入場：只在小時 9",
        "when": "1:01:18–1:03:35",
        "nav": "SNDK 10月9日入場：只在小時 9",
        "eyebrow": "科目十一",
        "title": "SNDK 10月9日入場：只在小時 9",
        "subtitle": "日線已離開 9 同 21，所以唔係最好；低週期阻力勝率較低",
        "meta": _meta("1:01:18–1:03:35"),
        "watch_label": "由 1:01:18 觀看直播片段",
        "watch_url": f"{YT}&t=3678s",
        "description": "Martin Luk 直播拆解：回看 10 月 9 日在 50 EMA 反彈淡 SNDK，覺得唔係最好，因為日線已離開 9 同 21，只係小時 9 嘅阻力。",
        "summary_kicker": "概要",
        "summary_title": "回看一筆「還可以但唔係最好」嘅入場",
        "summary": [
            "1:01:18 有人問 10 月 9 日在 50 EMA 反彈淡 SNDK 點樣。佢覺得唔係最好，因為日線已經離開 9 同 21。不過弱市裏面，呢類還可以嘅入場有時會行得好好。呢筆只係小時 9 EMA 嘅阻力；淡喺低週期阻力，勝率會較低。最好仍然係 9 EMA 上面嗰啲影線。如果錯過最好位置但仍想參與，可以當還可以嘅入場，但要知勝率低、好容易被停，如果再彈上下降 9 同 21，就要準備再入。",
        ],
        "card": "10 月 9 日在 50 EMA 反彈淡 SNDK，唔係最好，因為日線已離開 9 同 21，只係小時 9。弱市可以行到，但勝率較低，要準備再入。",
        "charts": [
            chart(
                "chart-sndk-0140", "SNDK 小時 1:01:40", "圖一",
                "SNDK 小時圖：回看 10 月 9 日入場",
                "直播 1:01:40",
                "images/sndk-oct9/01_sndk_hourly_0140.jpg",
                "images/sndk-oct9/src_01_sndk_hourly_0140.jpg",
                "圖一 · SNDK 小時圖 · 直播 1:01:40。註解標示呢筆只係小時 9 嘅阻力，以及日線已離開 9、21 所以唔係最好。",
                "加咗註解嘅 SNDK 小時圖：標示小時 9 同較低勝率。",
                "直播原畫面：SNDK 小時圖，未加註解。",
                [
                    q(
                        f"1:01:18–1:03:35 · {WHISPER_META}",
                        "What do you think about my short entry on SNDK on 9th of October on the bounce on the 50 EMA? It's not the best one, because it is a little bit extended on the daily from the 9 EMA and 21 as well. But you know what, sometimes like a fair entries could work very great, could work beautifully in the weak markets, like when you're really nailing the trend. So I think the entry is not the best one. It's only at the hourly 9 EMA. And as I've said, if you're short at the hourly 9, like the lower time frame resistance, you're gonna have a lower win rate. But if you can nail the timing, then it all matters. To me the best short is definitely like at the 9 EMAs, like those wicks here above here. But somehow if you miss them, but still would like to participate on the short side, I think that's a fair entry, but you need to know it's going to be a very low win rate entries, and you have a pretty high chance of getting stopped out. Then if it's going to bounce higher into the declining 9 and 21, you have to be prepared for the re-entry.",
                        "你點睇我 10 月 9 日喺 50 EMA 反彈淡 SNDK 呢筆入場？呢筆唔係最好，因為日線已經離開 9 EMA 同 21。不過有時候呢類還可以嘅入場，在弱市裏面、當你真係捉到趨勢，可以行得好好。所以我覺得呢筆唔係最好，佢只係在小時 9 EMA。正如我講過，如果你淡喺小時 9，即係低週期阻力，勝率會較低。但如果你捉到時間，噉又係關鍵。對我嚟講，最好嘅淡倉一定係在 9 EMA，就係上面呢啲影線。不過如果你錯過咗，但又想參與淡倉，我覺得呢個係還可以嘅入場；但你要知道呢類勝率會好低，被停嘅機會頗高。如果之後再彈上下降中嘅 9 同 21，你就要準備再入。",
                    ),
                    r(
                        "呢度同時承認「弱市裏面還可以嘅入場都可以行到」，又把最好位置定在 9 EMA 嘅影線，並且預先講低週期入場要準備再入。",
                        "畫面 Sandisk Corporation（SNDK），只當圖上文字。圖例冇印週期。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "10 月 9 日嘅成交價、倉位同損益畫面睇唔到，只保留入場位置嘅討論。",
        ],
    },

    {
        "id": "tem-not-short",
        "pager_name": "TEM 唔淡：軟件仲強，等 21 超調",
        "when": "1:03:35–1:05:24",
        "nav": "TEM 唔淡：軟件仲強，等 21 超調",
        "eyebrow": "科目十二",
        "title": "TEM 唔淡：軟件仲強，等 21 超調",
        "subtitle": "週線企穩，日線有偏多反轉、undercut-rally 同 pin bar",
        "meta": _meta("1:03:35–1:05:24"),
        "watch_label": "由 1:03:35 觀看直播片段",
        "watch_url": f"{YT}&t=3815s",
        "description": "Martin Luk 直播拆解：聊天室問 TEM 今日好唔好淡；佢唔考慮，因為軟件仍係偏強板塊，日線有偏多反轉。如果要淡，會等稍微超調 21。",
        "summary_kicker": "概要",
        "summary_title": "反覆拒絕均線，唔等於就要淡",
        "summary": [
            "1:03:35 有人問 TAM／TEM 今日好唔好淡：已經多次被 10 同 15 EMA 拒絕，但會唔會反而令向上突破更有機會。佢而家唔考慮淡。首先軟件仍係而家偏強嘅板塊之一；週線企得幾好，日線有偏多反轉，之後 undercut and rally、pin bar。呢度有少少亂、波動偏高，佢唔鍾意在呢度淡。如果一定要淡，會等稍微超調 21。",
            "聊天室同轉寫寫成 TAM，畫面係 Tempus AI（TEM）。",
        ],
        "card": "TEM 多次被均線拒絕，但佢唔淡：軟件仍偏強，週線企穩，日線有偏多反轉、undercut-rally 同 pin bar。如果要淡，會等稍微超調 21。",
        "charts": [
            chart(
                "chart-tem-0430", "TEM 日線 1:04:30", "圖一",
                "TEM 日線：唔考慮淡",
                "直播 1:04:30",
                "images/tem-not-short/01_tem_daily_0430.jpg",
                "images/tem-not-short/src_01_tem_daily_0430.jpg",
                "圖一 · TEM 日線 · 直播 1:04:30。註解標示唔考慮淡，以及日線有偏多反轉、undercut-rally 同 pin bar；如果要淡會等超調 21。",
                "加咗註解嘅 TEM 日線：標示唔淡同等 21 超調。",
                "直播原畫面：TEM 日線，未加註解。",
                [
                    q(
                        f"1:03:35–1:05:24 · {WHISPER_META}",
                        "Do you think TAM has a good short setup today? It has been rejected by the 10 and 15 EMAs several times. Or could those repeated rejections actually make an upside breakout more likely? Right now, I won't consider shorting it. First, it's one of the strongest sector right now, softwares, and like on the weekly it's holding up pretty well, and on the daily we got like the better bullish reversal and then the undercut and rally, the pin bar candle. I don't like shorting here. It's a little bit too choppy, the volatility a little bit too high down here. If I have to short, I will wait for maybe a little bit overshoot the 21 would be the best, like somewhere here. So maybe a little bit overshoot, but I just don't consider it.",
                        "你覺得 TAM 今日好唔好淡？已經多次被 10 同 15 EMA 拒絕。定係呢啲反覆拒絕反而令向上突破更有機會？而家我唔會考慮淡佢。首先，軟件而家係偏強嘅板塊之一；週線企得幾好，日線有比較好嘅偏多反轉，之後 undercut and rally、pin bar。我唔鍾意在呢度淡。呢度有少少亂，波動亦偏高。如果我一定要淡，我會等大概稍微超調 21，會係最好，就係大概呢一帶。所以可能稍微超調，但我就唔考慮。",
                        "聊天室同轉寫寫成 TAM；畫面係 Tempus AI, Inc.（TEM），以畫面為準。口中 10、15、21 EMA，圖例冇印週期，唔擅自改寫成 9 或者 50。",
                    ),
                    r(
                        "反覆拒絕均線，喺佢呢度唔等於自動變成淡倉；佢先睇板塊強弱、週線同日線反轉形態。",
                        "畫面公司名同「Packaged Software」只當圖上文字。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "Whisper 有一句聽到 but biotech softwares；主句仍然係 softwares 板塊偏強。唔把生物科技寫成事實。",
        ],
    },

    {
        "id": "sell-into-strength",
        "pager_name": "偏向賣喺強勢",
        "when": "1:05:57–1:09:06",
        "nav": "偏向賣喺強勢",
        "eyebrow": "科目十三",
        "title": "偏向賣喺強勢",
        "subtitle": "唔一定等收市跌破 9 或 21；可以留最強嗰兩筆再抱",
        "meta": _meta("1:05:57–1:09:06"),
        "watch_label": "由 1:05:57 觀看直播片段",
        "watch_url": f"{YT}&t=3957s",
        "description": "Martin Luk 直播拆解：有人提到留部分倉等趨勢走完；佢較寬鬆喺賣出，有時會整筆賣喺強勢，尤其係大市已經延伸。",
        "summary_kicker": "概要",
        "summary_title": "用大市例子講點解有時唔等均線先走",
        "summary": [
            "1:05:57 聊天室提到一位交易者成日話，食完利潤之後都要留部分倉，等趨勢走完。佢自己賣出方面較寬鬆：唔一定等收市跌破 9 或者 21 EMA，有時會在強勢裏面整筆賣掉，尤其係覺得大市已經延伸。例如可能就在呢根綠燭走，因為已經拉得太遠；如果再等回調跌破 9，會交回太多，但代價係可能錯過再向上。賣喺強勢嘅好處係減少回撤，令權益曲線同心理資本都留在高位。佢仍然想盡量抱多一兩個星期、攞到大部分而唔係全部。因為經常賣得太早，所以想用混合做法：如果有五筆做多，可能嗰日賣三筆，留最強兩筆再抱高啲。賣出真係好難，佢冇硬性規則。",
            "畫面用 QQQ 日線做「somewhere here, maybe on this green candle」嘅例子。",
        ],
        "card": "賣出較寬鬆，有時會整筆賣喺強勢，唔一定等跌破 9 或 21。可以用混合做法：五筆做多賣三筆，留最強兩筆再抱。",
        "charts": [
            chart(
                "chart-qqq-0810", "QQQ 日線 1:08:10", "圖一",
                "用大市例子講賣喺強勢",
                "直播 1:08:10",
                "images/sell-into-strength/01_qqq_daily_0810.jpg",
                "images/sell-into-strength/src_01_qqq_daily_0810.jpg",
                "圖一 · QQQ 日線 · 直播 1:08:10。註解標示口中「可能就在呢根綠燭」賣出，以及唔一定等收市跌破 9 或 21。",
                "加咗註解嘅 QQQ 日線：標示賣喺強勢嘅例子。",
                "直播原畫面：QQQ 日線，未加註解。",
                [
                    q(
                        f"1:05:57–1:09:06 · {WHISPER_META}",
                        "Someone has always said to keep some of the position left open after taking profits to let it ride the trend to the end. What do you think about that? Personally I'm more like lenient on the sell side, so sometimes I'm not going to wait for the close below maybe the 9 EMA or the 21 EMA. Sometimes I just sell the whole positions into the strength, and especially when I consider the market has been extended. Maybe I would exit the whole position somewhere here, like maybe on this green candle, just because I think it's just so extended, so stretched to the upside, and I will give back a little bit too much if I wait for the pullback to the close below the 9 EMA, but that means I'm going to miss the potential further upside. But selling the strength has a pretty big advantage, which is to minimize your drawdown, to keep your equity curve at the all-time highs and to also put your mental capital at the all-time highs too. To me, I tend to sell into strength more, but I still would like to hold as much as possible, to hold for at least maybe a week or two, and trying to capture most of the move but maybe not all of the move. But I always sell too early because of that. So maybe I would try to use a mixed approach: if I got five longs, maybe I would sell maybe three on this day and maybe keep the strongest two and then ride them higher. But I think selling is really hard, and I don't really have a hard rule on that.",
                        "有人成日話，食完利潤之後都要留部分倉，等趨勢走完。你點睇？我自己賣出方面較寬鬆，所以有時唔會等收市跌破大概 9 EMA 或者 21 EMA。有時我會在強勢裏面把成筆倉都賣掉，尤其係我覺得大市已經延伸。可能我會就在呢一帶離場，例如就在呢根綠燭，只係因為我覺得已經拉得太遠、向上拉得太緊，如果再等回調跌破 9 EMA，我會交回太多；但噉亦意味住可能錯過再向上。不過賣喺強勢有個頗大好處，就係減少回撤，令權益曲線留在高位，亦令心理資本留在高位。對我嚟講，我較傾向賣喺強勢，但我仍然想盡量抱得耐啲，至少抱多大概一兩個星期，盡量攞到大部分走勢，但未必全部。不過正因為噉，我經常賣得太早。所以或者我會試混合做法：如果我有五筆做多，可能嗰日賣三筆，留最強兩筆再抱高啲。但我覺得賣出真係好難，我喺呢樣冇硬性規則。",
                        "聊天室人名 Whisper 聽成 Krishna Kolomagyi，唔擅自改寫。呢段係賣出習慣，唔係新開倉規則。",
                    ),
                    r(
                        "重點係權衡：等均線先走，可能交回太多；賣喺強勢，又可能賣得太早。佢用混合做法去折衷，並且公開話冇硬性規則。",
                        "「五筆賣三、留兩筆」只係口中例子，唔當可複製倉位公式。圖例冇印週期。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "聊天室提到嘅交易者名字以機器轉寫為準，唔確定官方寫法，故唔改名。",
        ],
    },

    {
        "id": "oil-break",
        "pager_name": "大市小時 9 有彈，原油向下破",
        "when": "1:09:37–1:10:47",
        "nav": "大市小時 9 有彈，原油向下破",
        "eyebrow": "科目十四",
        "title": "大市小時 9 有彈，原油向下破",
        "subtitle": "一口帶過兩個位置",
        "meta": _meta("1:09:37–1:10:47"),
        "watch_label": "由 1:09:37 觀看直播片段",
        "watch_url": f"{YT}&t=4177s",
        "description": "Martin Luk 直播拆解：大市喺小時 9 有彈，同時原油睇落向下破。",
        "summary_kicker": "概要",
        "summary_title": "講完賣出習慣，隨即掃一眼大市同油",
        "summary": [
            "1:09:37 佢話大市喺小時 9 有彈，而原油睇落向下破。畫面隨即見到 USO 小時圖同 WTI。Whisper 把 the market 聽成 mark，把 hourly 9 聽成 already 9。",
        ],
        "card": "口中大市喺小時 9 有彈；原油（USO／WTI）睇落向下破。",
        "charts": [
            chart(
                "chart-uso-0930", "USO 小時 1:09:30", "圖一",
                "USO 小時圖：原油相關",
                "直播 1:09:30",
                "images/oil-break/01_uso_hourly_0930.jpg",
                "images/oil-break/src_01_uso_hourly_0930.jpg",
                "圖一 · USO 小時圖 · 直播 1:09:30。註解標示原油相關品種，以及口中先講大市小時 9 有彈、再講油向下。",
                "加咗註解嘅 USO 小時圖：標示原油相關。",
                "直播原畫面：USO 小時圖，未加註解。",
                [
                    q(
                        f"1:09:37–1:10:47 · {WHISPER_META}",
                        "The market is bouncing at the hourly 9, and the oil still looks like it's breaking lower.",
                        "大市喺小時 9 有彈，而原油仍然睇落向下破。",
                        "Whisper 把 The market 聽成 mark is，把 hourly 9 聽成 already 9。對照 YouTube 字幕同語境還原，並標明。講大市小時 9 嗰陣，畫面已經開始切到原油相關品種，未另留一張同步嘅指數小時圖。",
                    ),
                    r(
                        "呢句把兩個位置並排：指數有彈，油向下。唔好把 USO 讀成大市本身。",
                        "畫面 United States Oil Fund 只當圖上文字。9 以口中為準。",
                    ),
                ],
            ),
            chart(
                "chart-usoil-1030", "USOIL 1:10:30", "圖二",
                "WTI：睇落向下破",
                "直播 1:10:30",
                "images/oil-break/02_usoil_1030.jpg",
                "images/oil-break/src_02_usoil_1030.jpg",
                "圖二 · WTI · 直播 1:10:30。註解標示口中原油睇落向下破，以及畫面商品名稱只當圖上文字。",
                "加咗註解嘅 WTI 圖：標示向下破。",
                "直播原畫面：WTI，未加註解。",
                [
                    r(
                        "呢張用來對口中「oil is breaking lower」。位置讀法以當時畫面同原話為準，唔另加未講過嘅目標。",
                        "畫面寫住 CFDs on WTI Crude Oil，只當圖上文字。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "1:10:47–1:23:55 大部分時間靜音或只係講自己靜咗咪，主要係翻圖，唔做成圖冊。",
        ],
    },

    {
        "id": "dram-gap-reverse",
        "pager_name": "Memory ETF 超調後喺缺口倒轉",
        "when": "1:23:55–1:24:12",
        "nav": "Memory ETF 超調後喺缺口倒轉",
        "eyebrow": "科目十五",
        "title": "Memory ETF 超調後喺缺口倒轉",
        "subtitle": "超調第一根小時高位，再喺未補缺口附近反轉向下",
        "meta": _meta("1:23:55–1:24:12"),
        "watch_label": "由 1:23:55 觀看直播片段",
        "watch_url": f"{YT}&t=5035s",
        "description": "Martin Luk 直播拆解：Memory ETF（畫面代碼 DRAM）超調第一根小時高位後，在未補缺口附近倒轉向下。",
        "summary_kicker": "概要",
        "summary_title": "靜音翻圖之後，單獨指出呢個位置",
        "summary": [
            "1:23:55 佢話有啲鍾意呢隻 memory ETF：超調咗第一根小時 K 線高位，而家就在未補缺口附近倒轉向下。畫面代碼係 DRAM，標題寫住 Roundhill Memory ETF。",
        ],
        "card": "Memory ETF（DRAM）超調第一根小時高位後，在未補缺口附近倒轉向下。",
        "charts": [
            chart(
                "chart-dram-2355", "DRAM 小時 1:23:55", "圖一",
                "Memory ETF 小時圖：超調後喺缺口倒轉",
                "直播 1:23:55",
                "images/dram-gap-reverse/01_dram_hourly_2355.jpg",
                "images/dram-gap-reverse/src_01_dram_hourly_2355.jpg",
                "圖一 · DRAM 小時圖 · 直播 1:23:55。註解標示超調第一根小時高位後，在未補缺口附近倒轉向下。",
                "加咗註解嘅 DRAM 小時圖：標示超調同缺口倒轉。",
                "直播原畫面：DRAM 小時圖，未加註解。",
                [
                    q(
                        f"1:23:55–1:24:12 · {WHISPER_META}",
                        "Now I kind of like this memory ETF overshooting the first hourly candle high and now reversing lower right at this unfilled gap level.",
                        "而家我有啲鍾意呢隻 memory ETF：佢超調咗第一根小時 K 線高位，而家就在呢個未補缺口位置倒轉向下。",
                    ),
                    r(
                        "重點係兩個位置疊埋：超調第一根小時高位，同喺未補缺口倒轉。",
                        "畫面代碼 DRAM，標題 Roundhill Memory ETF，都只當圖上文字。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "講完之後又掃過 USO、SPCX 五分鐘等，冇新嘅獨立分析點，唔另開一科。",
        ],
    },

    {
        "id": "cover-or-wait",
        "pager_name": "想平淡倉，但又喺阻力猶豫",
        "when": "1:37:57–1:44:36",
        "nav": "想平淡倉，但又喺阻力猶豫",
        "eyebrow": "科目十六",
        "title": "想平淡倉，但又喺阻力猶豫",
        "subtitle": "UVXY 同部分淡倉未決定；Spaces、SK Hynix 今日偏弱",
        "meta": _meta("1:37:57–1:44:36"),
        "watch_label": "由 1:37:57 觀看直播片段",
        "watch_url": f"{YT}&t=5877s",
        "description": "Martin Luk 直播拆解：緊決定要唔要平 UVXY 或者一啲淡倉；好多品種仍在阻力，想再等更闊確認。Spaces 同 SK Hynix 今日偏弱，令佢猶豫平倉。",
        "summary_kicker": "概要",
        "summary_title": "阻力未破，所以未肯輕易平淡倉",
        "summary": [
            "1:37:57 佢話仍然喺度決定，要唔要平 UVXY，或者平一啲淡倉。但好多品種仍然在阻力，所以想再等一等，等見到更闊、更多品種出現更強嘅動作。之後又話自己曾想平一啲淡倉，但同時好多品種真係彈入阻力；今日 Spaces 偏弱，SK Hynix 都偏弱，半導體盤中亦相對弱，令佢猶豫平淡倉。",
            "畫面見到 IWM 日線同 QQQ 小時圖。Whisper 把 SK Hynix 聽成 Esky Hynix，把 the semis 聽成 Themis，把 cover the shorts 聽成 offer the shots。呢段未單獨定影到 SK Hynix 本身。",
        ],
        "card": "緊決定要唔要平 UVXY 或者一啲淡倉。好多品種仍在阻力，想再等確認；Spaces 同 SK Hynix 今日偏弱，令佢猶豫平倉。",
        "charts": [
            chart(
                "chart-iwm-13800", "IWM 日線 1:38:00", "圖一",
                "IWM 日線：好多品種仍在阻力",
                "直播 1:38:00",
                "images/cover-or-wait/01_iwm_daily_13800.jpg",
                "images/cover-or-wait/src_01_iwm_daily_13800.jpg",
                "圖一 · IWM 日線 · 直播 1:38:00。註解標示好多品種仍在阻力，以及佢仲未決定要唔要平 UVXY 或者一啲淡倉。",
                "加咗註解嘅 IWM 日線：標示仍在阻力、未肯輕易平倉。",
                "直播原畫面：IWM 日線，未加註解。",
                [
                    q(
                        f"1:37:57–1:39:02 · {WHISPER_META}",
                        "I'm still deciding whether to close maybe like UVXY or like some of my shorts right now, but a lot of the names is still at the resistance level. I'm not sure, like I tend to wait for a little bit, like to wait for some confirmation, maybe seeing more, like stronger actions from a broader amount of names.",
                        "我仍然喺度決定，而家要唔要平 UVXY，或者平一啲淡倉。但好多品種仍然在阻力位置。我唔肯定，我傾向再等一等，等一啲確認，或者見到更闊、更多品種出現更強嘅動作。",
                    ),
                    r(
                        "平倉與否仍然未決，理由係阻力未破，同埋未見到夠闊嘅確認。",
                        "畫面 iShares Russell 2000 Index Fund 只當圖上文字。呢段未見到 UVXY 本圖，UVXY 只在口中出現。",
                    ),
                ],
            ),
            chart(
                "chart-qqq-14340", "QQQ 小時 1:43:40", "圖二",
                "QQQ 小時：彈入阻力",
                "直播 1:43:40",
                "images/cover-or-wait/02_qqq_hourly_14340.jpg",
                "images/cover-or-wait/src_02_qqq_hourly_14340.jpg",
                "圖二 · QQQ 小時圖 · 直播 1:43:40。註解標示彈入阻力，以及 Spaces、SK Hynix 今日偏弱令佢猶豫平淡倉。",
                "加咗註解嘅 QQQ 小時圖：標示彈入阻力同猶豫平倉。",
                "直播原畫面：QQQ 小時圖，未加註解。",
                [
                    q(
                        "1:43:42–1:44:36 · 機器轉寫，標點為閱讀而加",
                        "I was thinking to maybe close some of the shorts, but at the same time it's just a lot of the names is really bouncing into the resistance, and some of the Spaces is pretty weak today, SK Hynix is pretty weak today, the semis is also comparatively weak intraday. Yeah, I don't know, like it just made me hesitated to cover the shorts.",
                        "我有想過或者平一啲淡倉，但同時好多品種真係彈入阻力；而且有啲 Spaces 今日偏弱，SK Hynix 今日都偏弱，半導體盤中亦相對弱。係，我唔知，呢啲就令我猶豫平淡倉。",
                        "Whisper 把 SK Hynix 聽成 Esky Hynix，把 the semis 聽成 Themis，把 cover the shorts 聽成 offer the shots。Spaces 以口中為準；呢段畫面主要係 QQQ，未單獨定影 SK Hynix。",
                    ),
                    r(
                        "猶豫平倉嘅理由有兩邊：大市同好多品種仍在阻力，同時個別弱勢（Spaces、SK Hynix、半導體）又未叫佢放手。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "1:38:30 前後亦掃過其他品種，例如 SATS、LITE，冇獨立分析點，唔另出圖。",
            "口中 UVXY、SK Hynix、Spaces 喺呢段未全部定影；本頁唔補未見到嘅圖。",
        ],
    },

    {
        "id": "crypto-both-ways",
        "pager_name": "加密兩邊都可以，聽日有 FOMC",
        "when": "1:44:44–1:48:10",
        "nav": "加密兩邊都可以，聽日有 FOMC",
        "eyebrow": "科目十七",
        "title": "加密兩邊都可以，聽日有 FOMC",
        "subtitle": "若由日線 50 反轉再沿上升 9 走，或會係不錯嘅週線入場；而家仍在 9 同 21 之下",
        "meta": _meta("1:44:44–1:48:10"),
        "watch_label": "由 1:44:44 觀看直播片段",
        "watch_url": f"{YT}&t=6284s",
        "description": "Martin Luk 直播拆解：加密處於有趣位置，兩邊都可以。若由日線 50 反轉再沿上升 9 走，或會係不錯嘅週線入場；而家仍在 9 同 21 之下。聽日 FOMC 或會成轉折或下跌跟進。",
        "summary_kicker": "概要",
        "summary_title": "收結前把加密同聽日 FOMC 放在一齊",
        "summary": [
            "1:44:44 佢話加密都處於幾有趣嘅位置，兩邊都可以。有啲較強品種已經到 21。如果加密能夠做出實在突破，例如由日線 50 EMA 反轉，再沿上升 9 走，並且由下降 9 EMA 收復，或會係一個頗好嘅週線入場。但而家肯定仍在 9 同 21 之下，所以兩邊都有可能；加密相關股票偏弱。佢會再監察至少一兩小時，等向上確認，或者等弱勢出現。自己而家有少少猶豫。覺得今日直播就到呢度，有啲悶，只係睇住等。聽日有 FOMC，或會成為呢輪跌勢嘅轉折，或者觸發向下跟進。",
            "畫面主要係 ETH 日線。Whisper 把 cryptos 聽成 Kripplus。",
        ],
        "card": "加密兩邊都可以。若由日線 50 反轉再沿上升 9 走，或會係不錯嘅週線入場；而家仍在 9 同 21 之下。聽日 FOMC 或會成轉折或下跌跟進。",
        "charts": [
            chart(
                "chart-eth-14520", "ETH 日線 1:45:20", "圖一",
                "ETH 日線：兩邊都可以",
                "直播 1:45:20",
                "images/crypto-both-ways/01_eth_daily_14520.jpg",
                "images/crypto-both-ways/src_01_eth_daily_14520.jpg",
                "圖一 · ETH 日線 · 直播 1:45:20。註解標示若由日線 50 反轉再沿上升 9 走或會係不錯嘅週線入場，以及而家仍在 9 同 21 之下。",
                "加咗註解嘅 ETH 日線：標示兩邊都可以，仍在 9 同 21 之下。",
                "直播原畫面：ETH 日線，未加註解。",
                [
                    q(
                        f"1:44:44–1:46:37 · {WHISPER_META}",
                        "I think crypto is also at pretty interesting levels. You could go both ways. Some stronger names are at like the 21. Like if cryptos can do a solid breakout, like a reversal from the 50 EMA on daily, and then riding the rising 9, if it can recover from the declining 9 EMA, that could be a pretty good weekly entry. But right now it's definitely still under both the 9 and 21. I think they could go both ways, and I don't know, but the crypto stocks are weak. I'll keep monitoring, maybe at least an hour or two, try to wait for any confirmation on the upside, or if we're seeing some weakness coming in. I am a little indecisive right now.",
                        "我覺得加密都處於幾有趣嘅位置，兩邊都可以。有啲較強品種已經到譬如 21。如果加密能夠做出實在突破，例如由日線 50 EMA 反轉，再沿上升 9 走，如果可以由下降 9 EMA 收復，噉或會係一個頗好嘅週線入場。但而家肯定仍在 9 同 21 之下。我覺得兩邊都可以，我唔知，不過加密相關股票偏弱。我會再監察，可能至少再一兩小時，等向上確認，或者等見到弱勢出現。我而家有少少猶豫。",
                        "Whisper 把 cryptos 聽成 Kripplus。畫面係 ETHUSDT 永續合約日線；代碼同交易所名稱只當圖上文字。講到 crypto stocks 時未另開股票圖。",
                    ),
                    r(
                        "「兩邊都可以」要同入場條件一齊讀：理想情況係日線 50 反轉，再收復並沿上升 9 走；而家仍在 9 同 21 之下，所以未當確認。",
                        "圖例冇印週期。9、21、50 以口中為準。",
                    ),
                    q(
                        "1:47:02–1:48:10 · 機器轉寫，標點為閱讀而加",
                        "I think that will be the end of the stream. It's too boring, just watching and waiting. And I think we will see, maybe like tomorrow, tomorrow we got FOMC, and could be a turning point of this downtrend, or like a trigger for a downside follow through. Thank you guys for coming, see you in the next one.",
                        "我覺得今日直播就到呢度。有啲悶，只係睇住等。我想我哋會睇到，或者聽日，聽日有 FOMC，或會成為呢輪跌勢嘅轉折，或者觸發一次向下跟進。多謝大家到來，下次再見。",
                    ),
                    r(
                        "FOMC 被講成兩種可能：跌勢轉折，或者下跌跟進。佢冇預先揀邊邊。",
                        "收結時繼續用同一張加密日線，冇另開 FOMC 專圖。",
                    ),
                ],
            ),
        ],
        "notes_title": "注意事項",
        "notes": [
            "講加密時亦掃過 XRP／SOL 等合約，只係快速翻圖，重點用 ETH 日線出圖。",
            "「至少再等一兩小時」只係當時嘅等待計劃，唔當可複製持倉時限。",
        ],
    },
]

STREAM = {
    "id": "2026-10-27",
    "date_label": "2026年10月27日",
    "page": "2026-10-27.html",
    "title": "《Strong bounce》",
    "eyebrow": "2026年10月27日",
    "subtitle": "技術分析科目",
    "meta": "Martin Luk · 開播 21:19（台北時間） · 全程重播約 1:48:18",
    "watch_label": "打開直播重播",
    "watch_url": YT,
    "footer_time": "開播時間 2026年10月27日 21:19（台北時間）。",
    "card": "由開場到完結，有讀圖嘅段落按時間順序排。",
    "summary_kicker": "概要",
    "summary_title": "呢一場可以學嘅技術分析",
    "summary": [
        "呢一頁係 Martin Luk《Strong bounce》（2026年10月27日）入面，佢用圖解釋市場結構、形態、位置、均線，或者說明點解咁做嘅段落，由開場到直播完結（約 1:48:18）。長空白、閒聊，同冇講分析嘅快速翻圖，唔會單獨成科。科目按時間順序一齊列，唔分組。",
        "每科都有加咗字嘅圖，可以切返原畫面。圖上中文註解係之後加上嘅讀圖說明，唔係直播畫面原本已有嘅字。「原話」係英文轉寫，再附粵語對譯；「點樣讀」係我哋嘅說明，兩者分開。轉寫主要跟 faster-whisper large-v3-turbo（CPU，float32），並對照 YouTube 自動英文字幕。呢場冇 en-orig：YouTube 把原語音誤標為菲律賓語，英文自動字幕係翻譯軌，所以原話以 Whisper 為主。代碼同均線以畫面為準，並非逐字人工校對。",
    ],
    "notes_title": "注意事項",
    "notes": [
        "開場問候、08:43–12:07 執行風格同「坐場外等肥球」問答、25:42–27:00 加倉流程、37:33–38:14 TQQQ／成交量、50:44–52:42 逆勢細浪，以及 07:49「maybe SpaceX short」一句、27:51 一句過嘅持倉，若冇展開走圖，都唔單獨成科。13:40–25:42、33:17–36:21、1:10:47–1:23:55 等長空白或者靜音翻圖，唔做成圖冊。",
        "畫面睇唔到成交價、倉位大細或者損益，所以各科都唔寫死呢啲數字。提到嘅 1%、五筆賣三筆、再等一兩小時，只保留原話，唔當可複製規則。",
        "YouTube 自動字幕同 Whisper 都有聽錯代碼或用詞：例如 beaten-down 聽成 bid and down、NBIS 聽成 Nerebius、short 聽成 shot、semis ETF 聽成 sami's ETF／The same is ETFAs、Rocket Lab 一度聽成 rock a lap、anchored VWAP 聽成 angle view up／coffee web、9 EMA 聽成 9 year make、IONQ 聽成 Power and Q、TEM 聽成 TAM、the market 聽成 mark、hourly 9 聽成 already 9、SK Hynix 聽成 Esky Hynix、the semis 聽成 Themis、cover the shorts 聽成 offer the shots／shots、cryptos 聽成 Kripplus。本站按畫面同較合理嘅一方更正，並喺該科附註說明。圖例多數冇印均線週期，提到嘅 9、10、15、21、50 係口中或者位置讀法。",
        "NQ、SPY、QQQ、IGV、AAOI、SPCX、NBIS、SOXX、AMD、RKLB、GEV、TWST、MRVL、IONQ、SNDK、TEM、USO、USOIL、DRAM、IWM、ETH 等畫面公司名或基金名，都只當圖上文字。DRAM 畫面寫住 Roundhill Memory ETF；SPCX 畫面寫住 Space Exploration Technologies Corp。口中 all three indices 嗰段，清楚定影嘅係 SPY 同 QQQ，未見到同步嘅 IWM。講大市小時 9 時，畫面已經切到原油相關品種。講 UVXY、SK Hynix、Spaces 時，部分未單獨定影。聊天室人名 Whisper 聽成 Krishna Kolomagyi，唔擅自改寫。TEM 被問到嘅 10 同 15 EMA 按口中保留，唔改寫成 9 或者 50。",
    ],
    "subjects": SUBJECTS,
}
