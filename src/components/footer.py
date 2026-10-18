import streamlit as st

def footer_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""       
        <div style="margin-top:2rem;display:flex;gap:6px;justify:center;justify-content:center;item-align:center;">
            <p style="font-weight:bold;color:white;">created with ❤️ </p>
        </div>
         """, unsafe_allow_html=True)
