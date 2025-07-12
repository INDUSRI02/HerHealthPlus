import streamlit as st
import requests

st.set_page_config(page_title="HerHealth+", page_icon="🌸", layout="centered")

st.title("🌸 HerHealth+ - PCOS Precision Companion")
st.markdown("Welcome back, my **Queen/Warrior** 👑")

# User details
with st.form("user_info"):
    name = st.text_input("Your Name")
    age = st.number_input("Age", 10, 60)
    weight = st.number_input("Weight (kg)", 30, 200)
    height = st.number_input("Height (cm)", 120, 200)
    cycle = st.selectbox("Menstrual Cycle", ["Regular", "Irregular"])
    symptoms = st.multiselect("Symptoms you're facing", [
        "Facial hair", "Hair loss", "Acne", "Weight gain", "Mood swings", "Fatigue"
    ])
    submitted = st.form_submit_button("Check PCOS Risk")

if submitted:
    st.success("Don't worry my Queen, you are more than your symptoms 💖")
    st.write("Here are some recommendations just for you 👇")

    st.markdown("### 🌿 Diet Recommendations")
    st.markdown("- Eat: leafy greens, berries, lentils, oats, cinnamon, turmeric")
    st.markdown("- Avoid: sugar, refined carbs, fried food, dairy, red meat")

    st.markdown("### 🧘‍♀️ Exercises")
    st.markdown("- Daily brisk walking (30 mins)")
    st.markdown("- Yoga (especially Surya Namaskar, butterfly pose)")
    st.markdown("- Strength training (twice a week)")

    st.markdown("### 💅 Hygiene Tips")
    st.markdown("- Change pads regularly")
    st.markdown("- Keep underarms and intimate areas clean & dry")
    st.markdown("- Avoid harsh hair removal creams if skin is sensitive")

    st.markdown("### 🧠 Mental Health Tips")
    st.markdown("- Track your cycle and symptoms with journaling apps")
    st.markdown("- Join PCOS support groups (online)")
    st.markdown("- Practice self-love and affirmations")

    st.info("🌸 You are a warrior, not a diagnosis. You're not alone 💫")

