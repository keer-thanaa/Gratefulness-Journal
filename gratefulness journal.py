import streamlit as st
from datetime import datetime
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Gratefulness Journal", page_icon="❤︎")
st.title("🫙 Happiness Jar & Gratefulness Journal")

# -------------------------
# Initialize
# -------------------------
if "entries" not in st.session_state:
    st.session_state.entries = []

# -------------------------
# Jar Drawing
# -------------------------
def draw_jar(entries):
    fig, ax = plt.subplots(figsize=(4, 6))
    jar_outline = plt.Rectangle((0, 0), 1, 2, fill=False, edgecolor="black", linewidth=2)
    ax.add_patch(jar_outline)

    for entry in entries:
        x = random.uniform(0.1, 0.9)
        y = random.uniform(0.1, 1.9)
        circle = plt.Circle((x, y), 0.05, color=entry['Color'])
        ax.add_patch(circle)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 2)
    ax.axis("off")
    st.pyplot(fig)

# -------------------------
# UI
# -------------------------
st.header("Happiness Jar")
st.write("💡 *Add as many marbles as you like to describe your happiness!*")

if st.session_state.entries:
    draw_jar(st.session_state.entries)
else:
    st.write("Your Happiness Jar is empty. Add your first marble below!")

# -------------------------
# Form
# -------------------------
with st.form("journal_form"):
    st.write("### 3 Things I'm Grateful For:")
    g1 = st.text_input("Grateful for #1")
    g2 = st.text_input("Grateful for #2")
    g3 = st.text_input("Grateful for #3")

    laugh = st.text_input("Something that made me laugh today:")
    kind = st.text_input("I was kind to someone today by:")
    learned = st.text_input("Something I learnt today:")
    color = st.color_picker("Pick a marble color:", "#FF69B4")

    submitted = st.form_submit_button("Add to Happiness Jar")

# -------------------------
# Save to session and rerun
# -------------------------
if submitted:
    entry = {
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Grateful1": g1,
        "Grateful2": g2,
        "Grateful3": g3,
        "Laugh": laugh,
        "Kindness": kind,
        "Learned": learned,
        "Color": color
    }
    st.session_state.entries.append(entry)
    st.success("Added to your Happiness Jar! 💖")
    st.rerun()
