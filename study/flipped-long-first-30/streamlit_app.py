"""Streamlit entrypoint for the Flipped long study site.

Community Cloud main file path:
    study/flipped-long-first-30/streamlit_app.py

Local, from the repository root:
    streamlit run study/flipped-long-first-30/streamlit_app.py
"""

from __future__ import annotations

import base64
import html
from pathlib import Path

import streamlit as st

import study_content as content

ROOT = Path(__file__).resolve().parent
SUBJECT_INDEX = "__subjects__"


def _sync_query() -> None:
    stream_id = st.session_state.nav_stream
    subject_id = st.session_state.nav_subject
    if stream_id:
        st.query_params["stream"] = stream_id
    else:
        st.query_params.pop("stream", None)
    if subject_id:
        st.query_params["subject"] = subject_id
    else:
        st.query_params.pop("subject", None)


def _init_nav() -> None:
    if "nav_stream" not in st.session_state:
        stream_id = st.query_params.get("stream")
        subject_id = st.query_params.get("subject")
        stream = content.stream_by_id(stream_id) if stream_id else None
        subject = content.subject_by_id(subject_id) if subject_id else None
        if subject is not None and stream is None:
            stream = content.stream_for_subject(subject["id"])
        if stream is not None and subject is not None:
            if all(item["id"] != subject["id"] for item in stream["subjects"]):
                subject = None
        st.session_state.nav_stream = stream["id"] if stream else None
        st.session_state.nav_subject = subject["id"] if subject else None
        st.session_state._nav_from_button = True
    # A card or pager sets nav and asks the next run to move the radio.
    # Do this before the radio widget exists. A real radio click already updated
    # its own key, so it must not be overwritten here.
    if st.session_state.pop("_nav_from_button", False):
        st.session_state.pop("stream_radio", None)
        if st.session_state.nav_stream is None:
            st.session_state.pop("subject_radio", None)
        else:
            st.session_state.subject_radio = st.session_state.nav_subject or SUBJECT_INDEX


def _on_stream_radio() -> None:
    st.session_state.nav_stream = st.session_state.stream_radio
    st.session_state.nav_subject = None
    st.session_state._nav_from_button = True
    _sync_query()


def _on_subject_radio() -> None:
    chosen = st.session_state.subject_radio
    st.session_state.nav_subject = None if chosen == SUBJECT_INDEX else chosen
    _sync_query()


def _open_home() -> None:
    st.session_state.nav_stream = None
    st.session_state.nav_subject = None
    st.session_state._nav_from_button = True
    _sync_query()
    st.rerun()


def _open_stream(stream_id: str) -> None:
    st.session_state.nav_stream = stream_id
    st.session_state.nav_subject = None
    st.session_state._nav_from_button = True
    _sync_query()
    st.rerun()


def _open_subject(subject_id: str) -> None:
    stream = content.stream_for_subject(subject_id)
    if stream is not None:
        st.session_state.nav_stream = stream["id"]
    st.session_state.nav_subject = subject_id
    st.session_state._nav_from_button = True
    _sync_query()
    st.rerun()


@st.cache_data(show_spinner=False)
def _font_css() -> str:
    def face(weight: int, filename: str) -> str:
        raw = (ROOT / "fonts" / filename).read_bytes()
        encoded = base64.b64encode(raw).decode("ascii")
        return (
            "@font-face{"
            'font-family:"Noto Sans CJK TC";'
            f"src:url(data:font/woff2;base64,{encoded}) format('woff2');"
            f"font-weight:{weight};font-style:normal;font-display:swap;}}"
        )

    return face(400, "NotoSansCJKtc-Regular.woff2") + face(700, "NotoSansCJKtc-Bold.woff2")


def _inject_css() -> None:
    st.markdown(
        f"""
        <style>
        {_font_css()}
        .stApp, .stMarkdown, .stMarkdown p, .stCaption, [data-testid="stCaptionContainer"],
        [data-testid="stHeading"], [data-testid="stHeading"] *,
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] label,
        h1, h2, h3, li {{
          font-family: "Noto Sans CJK TC", "PingFang TC", "Microsoft JhengHei",
            "Noto Sans TC", sans-serif !important;
        }}
        .stApp {{ background: #11100e; color: #f1eee6; }}
        [data-testid="stSidebar"] {{
          background: #171614;
          border-right: 1px solid rgba(212, 180, 131, 0.16);
        }}
        section.main > div.block-container {{
          max-width: 70rem;
          padding-top: 1.5rem;
        }}
        .eyebrow {{
          margin: 0;
          color: #d4b483;
          font-size: 0.78rem;
          font-weight: 700;
          letter-spacing: 0.14em;
        }}
        .subtitle {{ margin: 0.25rem 0 0.35rem; color: #a8a297; font-size: 1.15rem; }}
        .meta {{ margin: 0; color: #7c776e; font-size: 0.92rem; }}
        .banner, .disclaimer {{
          margin: 1rem 0 0;
          padding: 0.75rem 0.95rem;
          border-left: 3px solid #8a7350;
          background: #1c1b18;
          color: #a8a297;
          border-radius: 0 12px 12px 0;
        }}
        .disclaimer {{
          border-left: none;
          background: #23221e;
          border-radius: 12px;
        }}
        .kicker {{
          margin: 1.4rem 0 0.25rem;
          color: #d4b483;
          font-size: 0.75rem;
          font-weight: 700;
          letter-spacing: 0.16em;
        }}
        .time-chip {{
          margin-left: 0.75rem;
          color: #a8a297;
          font-weight: 400;
          letter-spacing: 0;
        }}
        h2.chart-title {{ margin: 0 0 0.6rem; font-size: 1.55rem; }}
        .toc {{ margin: 0.4rem 0 0.2rem; color: #a8a297; }}
        .toc a {{ color: #d4b483; text-decoration: none; margin-right: 0.15rem; }}
        .quote, .read {{
          margin: 0.35rem 0 0.9rem;
          padding: 0.95rem 1rem;
          background: #1c1b18;
          border: 1px solid rgba(212, 180, 131, 0.16);
          border-radius: 14px;
        }}
        .read {{ background: #171614; border-color: rgba(212, 180, 131, 0.28); }}
        .section-label {{
          margin: 0 0 0.45rem;
          color: #d4b483;
          font-size: 0.78rem;
          font-weight: 700;
          letter-spacing: 0.12em;
        }}
        .quote-en {{
          margin: 0 0 0.85rem;
          padding-left: 0.85rem;
          border-left: 3px solid #8a7350;
          color: #ddd8cd;
          font-style: italic;
        }}
        .quote-meta {{
          display: block;
          margin-bottom: 0.4rem;
          color: #7c776e;
          font-size: 0.78rem;
          font-style: normal;
        }}
        .yc-label {{
          margin: 0.15rem 0 0.25rem;
          color: #d4b483;
          font-size: 0.78rem;
          font-weight: 700;
          letter-spacing: 0.12em;
        }}
        .quote-yc {{ margin: 0; color: #f1eee6; }}
        .aside {{ margin: 0.75rem 0 0; color: #a8a297; font-size: 0.92rem; }}
        .read p {{ margin: 0 0 0.7rem; }}
        .read p:last-child {{ margin-bottom: 0; }}
        .figcap {{ margin: 0.45rem 0 0.2rem; color: #a8a297; font-size: 0.92rem; }}
        .when {{
          margin: 0;
          color: #d4b483;
          font-weight: 700;
          letter-spacing: 0.04em;
        }}
        .later {{ margin-top: 0.8rem; color: #7c776e; font-size: 0.92rem; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def _html(text: str) -> str:
    return html.escape(text, quote=True)


@st.dialog("放大查看", width="large")
def _zoom(path: str, caption: str, alt: str) -> None:
    st.image(path, caption=caption, width="stretch", alt=alt)


def _image_path(rel: str) -> Path:
    return (ROOT / rel).resolve()


def _header(page: dict) -> None:
    st.markdown(
        f'<p class="eyebrow">{_html(page["eyebrow"])}</p>',
        unsafe_allow_html=True,
    )
    st.title(page["title"])
    st.markdown(f'<p class="subtitle">{_html(page["subtitle"])}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="meta">{_html(page["meta"])}</p>', unsafe_allow_html=True)
    if page.get("watch_url"):
        st.link_button(page["watch_label"], page["watch_url"])
    st.markdown(f'<p class="banner">{_html(page["banner"])}</p>', unsafe_allow_html=True)


def _summary(page: dict) -> None:
    st.markdown(
        f'<p class="kicker">{_html(page["summary_kicker"])}</p>',
        unsafe_allow_html=True,
    )
    st.header(page["summary_title"])
    for paragraph in page["summary"]:
        st.markdown(paragraph)


def _notes(page: dict) -> None:
    st.markdown('<div id="notes"></div>', unsafe_allow_html=True)
    st.markdown('<p class="kicker">附註</p>', unsafe_allow_html=True)
    st.header(page["notes_title"])
    for note in page["notes"]:
        st.markdown(f"- {note}")
    st.markdown(f'<p class="disclaimer">{_html(page["disclaimer"])}</p>', unsafe_allow_html=True)


def _render_home() -> None:
    page = content.HOME
    _header(page)
    _summary(page)
    st.markdown('<p class="kicker">直播</p>', unsafe_allow_html=True)
    for stream in content.STREAMS:
        with st.container(border=True):
            st.markdown(f'<p class="when">{_html(stream["date_label"])}</p>', unsafe_allow_html=True)
            st.subheader(stream["title"])
            st.markdown(stream["card"])
            if st.button("睇呢場科目", key=f"open-stream-{stream['id']}"):
                _open_stream(stream["id"])
    _notes(page)
    st.caption("同一資料夾嘅 index.html 係直播目錄，可以離線打開。直播連結需要上網。")


def _render_stream(stream: dict) -> None:
    _header(stream)
    _summary(stream)
    st.markdown('<p class="kicker">科目</p>', unsafe_allow_html=True)
    for subject in stream["subjects"]:
        with st.container(border=True):
            st.markdown(f'<p class="when">{_html(subject["when"])}</p>', unsafe_allow_html=True)
            st.subheader(subject["nav"])
            st.markdown(subject["card"])
            if st.button("閱讀呢科", key=f"open-{subject['id']}"):
                _open_subject(subject["id"])
    _notes(stream)
    if st.button("返回直播目錄", key=f"back-home-{stream['id']}"):
        _open_home()
    st.caption("同一資料夾可以離線打開。直播連結需要上網。")


def _chart_mode(subject_id: str, index: int, all_source: bool) -> str:
    if all_source:
        return "source"
    mode = st.segmented_control(
        "顯示版本",
        options=["annotated", "source"],
        default="annotated",
        format_func=lambda value: "註解圖" if value == "annotated" else "原畫面",
        key=f"mode-{subject_id}-{index}",
        label_visibility="collapsed",
        required=True,
    )
    return mode or "annotated"


def _render_blocks(blocks: list[dict]) -> None:
    for block in blocks:
        if block["kind"] == "quote":
            lines = []
            for line in block["lines"]:
                lines.append(
                    '<p class="quote-en">'
                    f'<span class="quote-meta">{_html(line["meta"])}</span>'
                    f'{_html(line["en"])}</p>'
                )
            note = block.get("note")
            if note:
                note_html = (
                    '<p class="aside">'
                    + "<br>".join(_html(part) for part in note.split("\n"))
                    + "</p>"
                )
            else:
                note_html = ""
            st.markdown(
                '<div class="quote">'
                '<p class="section-label">原話</p>'
                + "".join(lines)
                + '<p class="yc-label">粵語對譯</p>'
                + f'<p class="quote-yc">{_html(block["yc"])}</p>'
                + note_html
                + "</div>",
                unsafe_allow_html=True,
            )
        else:
            paragraphs = "".join(f"<p>{_html(paragraph)}</p>" for paragraph in block["paragraphs"])
            st.markdown(
                '<div class="read"><p class="section-label">點樣讀</p>' + paragraphs + "</div>",
                unsafe_allow_html=True,
            )


def _render_chart(subject_id: str, index: int, chart: dict, all_source: bool) -> None:
    st.markdown(
        (
            f'<p class="kicker" id="{_html(chart["anchor"])}">'
            f'{_html(chart["kicker"])}'
            f'<span class="time-chip">{_html(chart["time"])}</span></p>'
            f'<h2 class="chart-title">{_html(chart["title"])}</h2>'
        ),
        unsafe_allow_html=True,
    )
    mode = _chart_mode(subject_id, index, all_source)
    rel = chart["source"] if mode == "source" else chart["annotated"]
    alt = chart["alt_source"] if mode == "source" else chart["alt_annotated"]
    path = _image_path(rel)
    if path.is_file():
        st.image(str(path), width="stretch", alt=alt)
    else:
        st.error(f"找不到圖片：{rel}")
    st.markdown(f'<p class="figcap">{_html(chart["caption"])}</p>', unsafe_allow_html=True)
    if path.is_file() and st.button("放大查看", key=f"zoom-{subject_id}-{index}"):
        _zoom(str(path), chart["caption"], alt)
    _render_blocks(chart["blocks"])


def _render_subject(subject: dict) -> None:
    _header(subject)
    toc_bits = [
        f'<a href="#{_html(chart["anchor"])}">{number}. {_html(chart["toc"])}</a>'
        for number, chart in enumerate(subject["charts"], start=1)
    ]
    toc_bits.append('<a href="#notes">注意事項</a>')
    st.markdown(
        '<p class="toc">閱讀次序 ' + " · ".join(toc_bits) + "</p>",
        unsafe_allow_html=True,
    )
    flag = f"all-source-{subject['id']}"
    st.session_state.setdefault(flag, False)
    toggle_label = "全部改回註解圖" if st.session_state[flag] else "全部顯示原畫面"
    if st.button(toggle_label, key=f"toggle-{subject['id']}"):
        st.session_state[flag] = not st.session_state[flag]
        st.rerun()
    _summary(subject)
    for index, chart in enumerate(subject["charts"]):
        _render_chart(subject["id"], index, chart, st.session_state[flag])
    _notes(subject)
    _pager(subject)
    st.caption("開播時間 2026年11月4日 22:26（台北時間）。直播連結需要上網。")


def _subject_label(subject_id: str) -> str:
    if subject_id == SUBJECT_INDEX:
        return "科目目錄"
    subject = content.subject_by_id(subject_id)
    assert subject is not None
    return f"{subject['when']}  {subject['pager_name']}"


def _pager(subject: dict) -> None:
    stream = content.stream_for_subject(subject["id"])
    subjects = stream["subjects"] if stream else content.SUBJECTS
    index = next(i for i, item in enumerate(subjects) if item["id"] == subject["id"])
    prev_subject = subjects[index - 1] if index > 0 else None
    next_subject = subjects[index + 1] if index + 1 < len(subjects) else None
    left, mid, right = st.columns(3)
    if prev_subject is None:
        left.caption("呢個係第一科")
    elif left.button(f"← 上一科：{prev_subject['pager_name']}", key=f"prev-{subject['id']}"):
        _open_subject(prev_subject["id"])
    if mid.button("科目目錄", key=f"home-{subject['id']}"):
        if stream is None:
            _open_home()
        else:
            _open_stream(stream["id"])
    if next_subject is None:
        right.caption("呢個係最後一科")
    elif right.button(f"下一科：{next_subject['pager_name']} →", key=f"next-{subject['id']}"):
        _open_subject(next_subject["id"])


def _sidebar(stream: dict | None) -> None:
    st.sidebar.caption("教育拆解，唔係投資建議。")
    if stream is None:
        st.sidebar.markdown("**直播目錄**")
        st.sidebar.caption("先揀一場直播嘅日期。")
        st.sidebar.radio(
            "直播",
            [item["id"] for item in content.STREAMS],
            format_func=lambda stream_id: (
                f"{content.stream_by_id(stream_id)['date_label']}  "
                f"{content.stream_by_id(stream_id)['title']}"
            ),
            index=None,
            key="stream_radio",
            on_change=_on_stream_radio,
        )
        return
    st.sidebar.markdown(f"**{stream['date_label']}**")
    st.sidebar.caption(stream["title"])
    if st.sidebar.button("返回直播目錄", key="sidebar-home"):
        _open_home()
    st.sidebar.radio(
        "科目",
        [SUBJECT_INDEX] + [subject["id"] for subject in stream["subjects"]],
        format_func=_subject_label,
        key="subject_radio",
        on_change=_on_subject_radio,
    )
    if stream.get("watch_url"):
        st.sidebar.link_button("打開直播重播", stream["watch_url"], width="stretch")


def main() -> None:
    st.set_page_config(
        page_title="技術分析科目",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    _inject_css()
    missing = content.missing_images(ROOT)
    if missing:
        st.error("缺圖：" + "、".join(missing))
    _init_nav()
    stream = content.stream_by_id(st.session_state.nav_stream) if st.session_state.nav_stream else None
    _sidebar(stream)
    if stream is None:
        _render_home()
        return
    subject = content.subject_by_id(st.session_state.nav_subject) if st.session_state.nav_subject else None
    if subject is None:
        _render_stream(stream)
    else:
        _render_subject(subject)


main()
