import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.markdown("""
    <style>
    .stApp { background-color: white; }
    div.stButton > button {
        border-radius: 20px;
        font-weight: bold;
        border: 2px solid pink;
        color: pink;
        background-color: white;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: pink;
        color: white;
        border: 2px solid pink;
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: pink;'>Wybierz swoją liczbę:</h1>", unsafe_allow_html=True)
st.set_page_config(page_title="Surprise", page_icon="❤️", layout="centered")
_, center_space, _ = st.columns([1.5, 1, 1.5])
liczba = None
with center_space:
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("67"):
            liczba = "67"
    with btn_col2:
        if st.button("69"):
            liczba = "69"
col1, col2 = st.columns(2)
if liczba:
    st.balloons()

    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    fig, ax = plt.subplots(figsize=(10, 10))
    fig.patch.set_facecolor('none')
    ax.set_facecolor('none')
    color_map = {"67": "#EB4770", "69": "#74ACE4"}
    ax.fill(x, y, color=color_map.get(liczba), alpha=1.0)
    ax.plot(x, y, color=color_map.get(liczba), linewidth=3)
    ax.text(0, 0, liczba, fontsize=50, ha='center', va='center', color='white', fontweight='bold')
    ax.axis('equal')
    ax.axis('off') 

    st.pyplot(fig)

    