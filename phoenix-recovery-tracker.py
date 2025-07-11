import streamlit as st
import json
from datetime import datetime
import os

st.set_page_config(page_title="Phoenix Recovery Tracker", layout="centered")

# ========== STYLES ==========
st.markdown("""
    <style>
    body {
        background-color: #F5F5DC;
        color: #111111;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff !important;
    }
    .emoji-button {
        font-size: 32px;
        border: 1px solid #ccc;
        border-radius: 6px;
        padding: 8px;
        margin: 4px;
        background-color: #fff;
        cursor: pointer;
        text-align: center;
    }
    .emoji-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ========== FILE SETUP ==========
FILENAME = "phoenix_data.json"
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        json.dump([], f)

# ========== GLOBAL FIELDS ==========
st.markdown("### 🚨 Crisis Support")
st.markdown("**If you're in danger or need immediate help:** [Call 911](tel:911), [Call 988](tel:988), or [Text HOME to 741741](https://www.crisistextline.org)")

st.markdown("##### *This app does not replace medical, psychological, or emergency care.*")

user_name = st.text_input("👤 What should I call you? (optional)", key="user_name")

# ========== HELPER ==========
def save_entry(entry):
    with open(FILENAME, "r") as f:
        data = json.load(f)
    data.append(entry)
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=2)
    st.success("✅ Entry saved!")

timestamp = datetime.now().isoformat()

# ========== SECTION 1 - MIND ==========
with st.expander("🧠 MIND"):
    st.markdown("#### How are you feeling mentally today?")
    emoji_labels = [
        ("😊", "Happy"), ("😢", "Sad"), ("😡", "Angry"), ("😰", "Anxious"),
        ("😴", "Tired"), ("🤔", "Confused"), ("😤", "Frustrated"), ("😌", "Calm")
    ]

    selected_emoji = st.radio(
        "Pick your mood:",
        options=emoji_labels,
        format_func=lambda x: f"{x[0]} {x[1]}",
        horizontal=True,
        key="emoji_mind"
    )

    mind_journal = st.text_area("📝 How are you feeling mentally today?", height=100)
    if st.button("Save Mind Entry"):
        entry = {
            "user": user_name,
            "timestamp": timestamp,
            "selected_emoji": selected_emoji[0],
            "mood_name": selected_emoji[1],
            "mind_journal": mind_journal
        }
        save_entry(entry)

# ========== SECTION 2 - BODY ==========
with st.expander("🏋️ BODY"):
    pain_level = st.slider("Current pain level (0 = no pain, 10 = worst pain)", 0, 10)
    workout_log = st.text_area("🏃 PT exercises/workouts (sets x reps)", height=100)
    body_journal = st.text_area("📝 How does your body feel today?", height=100)
    if st.button("Save Body Entry"):
        entry = {
            "user": user_name,
            "timestamp": timestamp,
            "pain_level": pain_level,
            "workout_log": workout_log,
            "body_journal": body_journal
        }
        save_entry(entry)

# ========== SECTION 3 - FUEL ==========
with st.expander("🥗 FUEL"):
    meals_log = st.text_area("🍽️ What did you eat today?", height=100)
    post_meal_feelings = st.text_area("📝 How do you feel after eating?", height=100)
    if st.button("Save Fuel Entry"):
        entry = {
            "user": user_name,
            "timestamp": timestamp,
            "meals_log": meals_log,
            "post_meal_feelings": post_meal_feelings
        }
        save_entry(entry)

# ========== SECTION 4 - REST ==========
with st.expander("🛌 REST"):
    sleep_quality = st.slider("🕒 How long did you sleep? (hours)", 0, 12)
    rest_journal = st.text_area("📝 Thoughts about your rest/sleep", height=100)
    if st.button("Save Rest Entry"):
        entry = {
            "user": user_name,
            "timestamp": timestamp,
            "sleep_quality": sleep_quality,
            "rest_journal": rest_journal
        }
        save_entry(entry)

# ========== SECTION 5 - BELONG ==========
with st.expander("👥 BELONG"):
    belong_journal = st.text_area("📝 Social connections, relationships, community thoughts", height=100)
    if st.button("Save Belong Entry"):
        entry = {
            "user": user_name,
            "timestamp": timestamp,
            "belong_journal": belong_journal
        }
        save_entry(entry)

# ========== SECTION 6 - SAFETY ==========
with st.expander("🛡️ SAFETY"):
    safety_journal = st.text_area("📝 Safety, security, stability thoughts", height=100)
    if st.button("Save Safety Entry"):
        entry = {
            "user": user_name,
            "timestamp": timestamp,
            "safety_journal": safety_journal
        }
        save_entry(entry)

# ========== SECTION 7 - PURPOSE ==========
with st.expander("🎯 PURPOSE"):
    purpose_journal = st.text_area("📝 Meaning, direction, goals, purpose thoughts", height=100)
    if st.button("Save Purpose Entry"):
        entry = {
            "user": user_name,
            "timestamp": timestamp,
            "purpose_journal": purpose_journal
        }
        save_entry(entry)

# ========== END ==========
st.markdown("----")
st.caption("📘 Phoenix Recovery Tracker — Built to Rise Again") 