import streamlit as st
from chatbot import generate_questions
from utils import is_exit_keyword, validate_input

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = -1  # For greeting
    st.session_state.answers = {}
    st.session_state.validation_error = ""

# Field questions and keys
questions = [
    "👋 Hello! What's your full name?",
    "📧 What's your email address?",
    "📱 What's your phone number?",
    "🡥 How many years of experience do you have?",
    "🎯 What's your desired position?",
    "📍 Where are you currently located?",
    "💻 What is your tech stack? (comma-separated, e.g., Python, React, MongoDB)"
]
field_keys = ['name', 'email', 'phone', 'experience', 'position', 'location', 'tech_stack']

st.title("🤖 TalentScout AI Hiring Assistant")

# Greeting message only once
if st.session_state.step == -1:
    st.markdown("👋 **Hello! I’m your AI Hiring Assistant at TalentScout.**")
    st.markdown("I'll help with your initial interview screening.\n\nLet’s get started by collecting a few basic details!")
    if st.button("🖐 Let's Start"):
        st.session_state.step += 1
        st.rerun()
    st.stop()

# Display previous answers
for i in range(st.session_state.step):
    key = field_keys[i]
    value = st.session_state.answers.get(key, "")
    st.markdown(f"**{questions[i]}**<br>{value}", unsafe_allow_html=True)
    st.markdown("---")

# Ask current question
current_step = st.session_state.step
if current_step < len(questions):
    st.subheader("🤠 Candidate Info")
    response = st.text_input(questions[current_step], key=f"q_{current_step}")
    exit_input = st.text_input("🖚 Type 'exit' here to quit anytime", key=f"exit_{current_step}")

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

# Final step: Generate questions
if st.session_state.step == len(questions):
    st.success("✅ All details received. Generating technical questions...")
    tech_stack = st.session_state.answers.get("tech_stack", "")

    with st.spinner("🤖 Thinking..."):
        questions = generate_questions(tech_stack)

    if questions:
        st.subheader("🦪 Technical Questions:")
        for idx, q in enumerate(questions, 1):
            st.markdown(f"**Q{idx}:** {q}")
        st.success("🎉 You're done! Thanks for chatting.")
    else:
        st.error("❌ Gemini API failed to generate questions.")
