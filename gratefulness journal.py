# happiness_jar.py

import streamlit as st
import pandas as pd
from datetime import datetime
import os
import random
import matplotlib.pyplot as plt

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="Gratefulness Journal", page_icon="❤︎")
st.title("🫙 Happiness Jar & Gratefulness Journal")

# -------------------------
# Set up daily filename
# -------------------------
today = datetime.now().strftime("%Y-%m-%d")
filename = f"journal_{today}.csv"

# -------------------------
# Load existing entries if file exists
# -------------------------
if os.path.exists(filename):
    df = pd.read_csv(filename)
else:
    df = pd.DataFrame(columns=[
        "Time",
        "Grateful1",
        "Grateful2",
        "Grateful3",
        "Laugh",
        "Kindness",
        "Learned",
        "BestPart",
        "LookingForward",
        "Rating",
        "Color"
    ])

# -------------------------
# Happiness Jar Visual
# -------------------------
st.header("Happiness Jar")
st.write("💡 Add as many marbles as you like to describe your happiness!")

# Draw a simple jar using matplotlib
def draw_jar(num_entries, colors):
    fig, ax = plt.subplots(figsize=(4, 6))
    # Draw jar outline
    jar_outline = plt.Rectangle((0, 0), 1, 2, fill=False, edgecolor="black", linewidth=2)
    ax.add_patch(jar_outline)

    # Add circles for each entry
    for i in range(num_entries):
        x = random.uniform(0.1, 0.9)
        y = random.uniform(0.1, 1.9)
        color = colors[i]
        circle = plt.Circle((x, y), 0.05, color=color)
        ax.add_patch(circle)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 2)
    ax.axis("off")
    st.pyplot(fig)

# -------------------------
# Show Jar if there are entries
# -------------------------
if not df.empty:
    draw_jar(len(df), df["Color"].tolist())
else:
    st.write("Your Happiness Jar is empty. Add your first marble below!")

# -------------------------
# Journal Prompts
# -------------------------

with st.form("journal_form"):
    st.write("### 3 Things I'm Grateful For:")
    grateful1 = st.text_input("Grateful for #1")
    grateful2 = st.text_input("Grateful for #2")
    grateful3 = st.text_input("Grateful for #3")

    laugh = st.text_input("Something that made me laugh today:")

    kindness = st.text_input("I was kind to someone today by:")

    learned = st.text_input("Something I learnt today:")

    best_part = st.text_input("Best part of the day:")

    looking_forward = st.text_input("What I'm looking forward to tomorrow:")

    rating = st.slider("Rate your day:", 1, 10, 5)

    color = st.color_picker("Pick a color for your Happiness Jar marble:", "#FF69B4")

    submitted = st.form_submit_button("Add to Happiness Jar")

# -------------------------
# Save Entry if Submitted
# -------------------------
if submitted:
    new_entry = pd.DataFrame([{
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Grateful1": grateful1,
        "Grateful2": grateful2,
        "Grateful3": grateful3,
        "Laugh": laugh,
        "Kindness": kindness,
        "Learned": learned,
        "BestPart": best_part,
        "LookingForward": looking_forward,
        "Rating": rating,
        "Color": color
    }])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(filename, index=False)
    st.success("Added to your Happiness Jar! 💖")
    st.rerun()

# -------------------------
# Show daily entries table (optional)
# -------------------------
with st.expander("📄 See today's entries"):
    st.dataframe(df)
