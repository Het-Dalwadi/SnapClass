
import streamlit as st


def style_background_home():
    """Apply midnight-plum styling and yellow portal cards."""
    st.markdown(
        """
        <style>
        :root {
            --sc-bright: #F0D66B;
            --sc-leaf: #E9DFAF;
            --sc-moss: #9A8038;
            --sc-forest: #171321;
            --sc-surface: #211B30;
            --sc-card: #2B2340;
            --sc-border: #5C4A30;
            --sc-white: #F7F3FF;
        }

        .stApp {
            background:
                radial-gradient(
                    ellipse at 8% 4%,
                    rgba(240, 214, 107, .09),
                    transparent 30%
                ),
                radial-gradient(
                    ellipse at 94% 18%,
                    rgba(196, 161, 255, .08),
                    transparent 30%
                ),
                var(--sc-forest) !important;
            color: var(--sc-white);
        }

        [data-testid="stMainBlockContainer"] {
            max-width: 1220px;
            padding-top: 1.7rem;
            padding-bottom: 2.6rem;
        }

        [data-testid="stColumn"] > div {
            min-width: 0;
        }

        /* Student and Teacher yellow cards */
        [data-testid="stVerticalBlockBorderWrapper"]:has(
            [data-testid="stImage"]
        ) {
            background: #F0D66B !important;
            background-color: #F0D66B !important;
            border: 2px solid #F8E7A0 !important;
            border-radius: 22px !important;
            padding: 18px !important;
            box-shadow: 0 10px 30px rgba(0, 0, 0, .18) !important;
            transition: box-shadow .2s ease, border-color .2s ease;
        }

        [data-testid="stVerticalBlockBorderWrapper"]:has(
            [data-testid="stImage"]
        ):hover {
            border-color: #FFF1B8 !important;
            box-shadow: 0 14px 32px rgba(240, 214, 107, .18) !important;
        }

        /* Dark text inside yellow cards */
        [data-testid="stVerticalBlockBorderWrapper"]:has(
            [data-testid="stImage"]
        ) h1,
        [data-testid="stVerticalBlockBorderWrapper"]:has(
            [data-testid="stImage"]
        ) h2,
        [data-testid="stVerticalBlockBorderWrapper"]:has(
            [data-testid="stImage"]
        ) h3,
        [data-testid="stVerticalBlockBorderWrapper"]:has(
            [data-testid="stImage"]
        ) p,
        [data-testid="stVerticalBlockBorderWrapper"]:has(
            [data-testid="stImage"]
        ) [data-testid="stMarkdownContainer"] {
            color: #292313 !important;
        }

        /* SNAP CLASS heading accent */
        [data-testid="stAppViewContainer"] h1 {
            color: var(--sc-bright) !important;
        }

        /* White portal buttons */
        [data-testid="stAppViewContainer"] button[kind="primary"] {
            background: #F7F3FF !important;
            background-color: #F7F3FF !important;
            color: #171321 !important;
            -webkit-text-fill-color: #171321 !important;
            border: 1px solid #F7F3FF !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
        }

        [data-testid="stAppViewContainer"] button[kind="primary"]:hover {
            background: #fffb14 !important;
            background-color: #fffb14!important;
            border-color: #fffb14 !important;
            color: #171321 !important;
            -webkit-text-fill-color: #171321 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    """Apply midnight-plum dashboard styling."""
    st.markdown(
        """
        <style>
        :root {
            --sc-bright: #C4A1FF;
            --sc-leaf: #D8C9F5;
            --sc-moss: #7953A9;
            --sc-forest: #171321;
            --sc-surface: #211B30;
            --sc-card: #2B2340;
            --sc-border: #45365F;
            --sc-white: #F7F3FF;
        }

        .stApp {
            background:
                radial-gradient(
                    ellipse at 100% 0%,
                    rgba(196, 161, 255, .09),
                    transparent 26%
                ),
                var(--sc-forest) !important;
            color: var(--sc-bright);
        }

        [data-testid="stMainBlockContainer"] {
            max-width: 1280px;
            padding-top: 1.5rem;
            padding-bottom: 2.5rem;
        }

        [data-testid="stSidebar"] {
            background: #211B30;
            border-right: 1px solid var(--sc-border);
        }

        [data-testid="stSidebar"] * {
            color: var(--sc-leaf);
        }

        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: var(--sc-bright) !important;
        }

        [data-testid="stMetric"] {
            background: var(--sc-surface);
            border: 1px solid var(--sc-border);
            border-radius: 18px;
            padding: 1rem 1.1rem;
            box-shadow: 0 7px 22px rgba(0, 0, 0, .12);
        }

        [data-testid="stMetricLabel"] {
            color: var(--sc-leaf) !important;
            font-weight: 600;
        }

        [data-testid="stMetricValue"] {
            color: var(--sc-bright) !important;
            font-weight: 800;
        }

        [data-testid="stMetricDelta"] {
            font-weight: 600;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--sc-card);
            border: 1px solid var(--sc-border);
            border-radius: 20px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, .12);
        }

        [data-testid="stVerticalBlockBorderWrapper"]:hover {
            border-color: var(--sc-leaf);
            box-shadow: 0 12px 28px rgba(0, 0, 0, .20);
        }

        h1, h2, h3 {
            color: var(--sc-bright) !important;
        }

        p, label {
            color: var(--sc-leaf);
        }

        hr {
            border-color: var(--sc-border);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    """Apply shared typography and dark-theme component styling."""
    st.markdown(
        """
        <style>
        @import url(
            'https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap'
        );
        @import url(
            'https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap'
        );

        :root {
            --sc-bright: #C4A1FF;
            --sc-leaf: #D8C9F5;
            --sc-moss: #7953A9;
            --sc-forest: #171321;
            --sc-surface: #211B30;
            --sc-card: #2B2340;
            --sc-border: #45365F;
            --sc-white: #F7F3FF;
        }

        #MainMenu,
        footer,
        header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem !important;
        }

        [data-testid="stMainBlockContainer"] {
            color: var(--sc-bright);
        }

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: var(--sc-bright) !important;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: var(--sc-bright) !important;
        }

        h3, h4, p {
            font-family: 'Outfit', sans-serif;
        }

        h3, h4 {
            color: var(--sc-leaf) !important;
        }

        p, label {
            color: var(--sc-leaf);
        }

        [data-testid="stMarkdownContainer"] {
            color: var(--sc-leaf);
        }

        button {
            border-radius: 12px !important;
            background-color: var(--sc-bright) !important;
            color: var(--sc-forest) !important;
            padding: 10px 20px !important;
            border: 1px solid var(--sc-bright) !important;
            font-weight: 700 !important;
            transition: transform .2s ease, box-shadow .2s ease !important;
        }

        button[kind="secondary"] {
            background-color: var(--sc-moss) !important;
            color: var(--sc-white) !important;
            border: 1px solid var(--sc-border) !important;
        }

        button[kind="tertiary"] {
            background-color: var(--sc-surface) !important;
            color: var(--sc-bright) !important;
            border: 1px solid var(--sc-border) !important;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 14px rgba(0, 0, 0, .20);
        }

        button[kind="primary"]:hover {
            background-color: #fffb14 !important;
            border-color: var(--sc-leaf) !important;
            -webkit-text-fill-color: #171321 !important;
        }

        button[kind="secondary"]:hover {
            background-color: var(--sc-leaf) !important;
            color: white !important;
            -webkit-text-fill-color: #171321 !important;
        }

        button[kind="tertiary"]:hover {
            background-color: var(--sc-moss) !important;
            -webkit-text-fill-color: #171321 !important;
        }

        input, textarea {
            border-radius: 10px !important;
            background-color: var(--sc-surface) !important;
            color: var(--sc-white) !important;
            border-color: var(--sc-border) !important;
        }

        input:focus, textarea:focus {
            border-color: var(--sc-bright) !important;
            box-shadow: 0 0 0 1px var(--sc-bright) !important;
        }

        a {
            color: var(--sc-bright);
        }

        hr {
            border-color: var(--sc-border);
        }

        ::selection {
            background: var(--sc-bright);
            color: var(--sc-forest);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
