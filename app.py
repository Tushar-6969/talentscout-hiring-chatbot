import streamlit as st
from chatbot import generate_questions
from utils import is_exit_keyword, validate_input, get_sentiment
from textblob import TextBlob

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = -1  # Greeting
    st.session_state.answers = {}
    st.session_state.language = 'English'
    st.session_state.validation_error = ""

# Page config
st.set_page_config(page_title="TalentScout AI", page_icon="🤖")
st.title("🤖 TalentScout AI Hiring Assistant")


# Greeting screen
if st.session_state.step == -1:
    st.markdown("👋 **Hello! I’m your AI Hiring Assistant at TalentScout.**")
    st.markdown("I'll guide you through a short screening process. You can type `'exit'` anytime to leave.")
    if st.button("👉 Let's Get Started"):
        st.session_state.step += 1
        st.rerun()
    st.stop()

# Define questions and field keys
questions = [
    "👋 What's your full name?",
    "📧 What's your email address?",
    "📱 What's your phone number?",
    "🡥 How many years of experience do you have?",
    "🎯 What's your desired position?",
    "📍 Where are you currently located?",
    "💻 What is your tech stack? (comma-separated, e.g., Python, React, MongoDB)"
]
field_keys = ['name', 'email', 'phone', 'experience', 'position', 'location', 'tech_stack']

# Show previous answers
for i in range(st.session_state.step):
    key = field_keys[i]
    value = st.session_state.answers.get(key, "")
    st.markdown(f"**{questions[i]}**<br>{value}", unsafe_allow_html=True)
    st.markdown("---")

# Ask current question
current_step = st.session_state.step
if current_step < len(questions):
    st.subheader("🧠 Candidate Info")
    response = st.text_input(questions[current_step], key=f"q_{current_step}")
    exit_input = st.text_input("🔚 Type 'exit' here to quit anytime", key=f"exit_{current_step}")

    if is_exit_keyword(exit_input):
        st.success("✅ Chat ended. Thank you for your time!")
        st.stop()

    if response:
        valid, error_msg = validate_input(field_keys[current_step], response)
        if valid:
            st.session_state.answers[field_keys[current_step]] = response
            st.session_state.step += 1
            st.session_state.validation_error = ""
            st.rerun()
        else:
            st.session_state.validation_error = error_msg

    if st.session_state.validation_error:
        st.warning(st.session_state.validation_error)

# All questions done — Consent & Output
if st.session_state.step == len(questions):
    st.subheader("📜 Consent")
    agree = st.checkbox("I agree to the use of my data for screening purposes.")

    if agree:
        st.success("✅ All details received. Generating technical questions...")
        tech_stack = st.session_state.answers.get("tech_stack", "")

        sentiment = get_sentiment(tech_stack)
        st.markdown(f"🧠 **Detected Tone of Your Tech Stack Input:** `{sentiment}`")

        with st.spinner("🤖 Thinking..."):
            generated = generate_questions(tech_stack)

        if generated:
            st.subheader("🦪 Technical Questions:")
            for idx, q in enumerate(generated, 1):
                st.markdown(f"**Q{idx}:** {q}")
            st.success("🎉 You're done! Thanks for chatting.")
        else:
            st.error("❌ Gemini API failed to generate questions.")
    else:
        st.warning("☝️ Please accept the consent checkbox to continue.")
