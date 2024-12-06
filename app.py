import streamlit as st
from model.model import chatbot_response  # Import the chatbot function

# Streamlit App Configuration
st.set_page_config(
    page_title="Saudi Labor Law Chatbot",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Right-to-Left and English Layout
st.markdown("""
    <style>
        .rtl {direction: rtl; text-align: right;}
        .ltr {direction: ltr; text-align: left;}
        .stTextArea textarea {direction: rtl; text-align: right; font-size: 1.1em; background-color: #fdfdfd; padding: 10px; border-radius: 8px; border: 1px solid #ddd;}
        .stButton button {width: 100%; font-size: 1.2em; padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 8px; cursor: pointer;}
        .stButton button:hover {background-color: #45a049;}
        .chat-response {background-color: #e8f5e9; padding: 15px; border-radius: 8px; font-size: 1.1em; margin-top: 10px;}
        .footer {text-align: center; font-size: 0.9em; color: #888; margin-top: 30px;}
    </style>
    """, unsafe_allow_html=True)

# Title and Description
st.markdown("<h1 style='text-align: center;'>🤖 Saudi Labor Law Chatbot</h1>", unsafe_allow_html=True)
st.markdown("💼 Welcome! How can I assist you today?", unsafe_allow_html=True)

# Recommended Questions
st.markdown("<h3>❓ Recommended Questions:</h3>", unsafe_allow_html=True)

questions = {
    "Arabic": [
        "ما هي العناصر الأساسية التي يجب تضمينها في عقد العمل وفقًا لنظام العمل السعودي؟",
        "ما هي أقصى مدة لفترة التجربة، وما هي شروط تمديدها؟",
        "كيف يتم دفع الأجور للعمال، وما هي الطرق المقبولة للدفع؟",
        "ما هي قواعد تكليف العامل بمهام مختلفة أو نقله إلى موقع آخر؟",
        "ما هي خطوات حساب مكافأة نهاية الخدمة للعاملين؟"
    ],
    "English": [
        "What are the obligations of the employer towards employee safety and health under Saudi Labor Law?",
        "What is the legal process for resolving disputes between an employer and an employee?",
        "What are the conditions under which an employee can legally resign without notice?",
        "How are overtime hours calculated, and what is the compensation rate for overtime work?",
        "What are the provisions regarding annual leave and public holidays for employees in Saudi Arabia?"
    ]
}

# Display Questions in Arabic and English
st.markdown("<h4>Arabic:</h4>", unsafe_allow_html=True)
for question in questions["Arabic"]:
    if st.button(question):
        st.session_state['user_input'] = question

st.markdown("<h4>English:</h4>", unsafe_allow_html=True)
for question in questions["English"]:
    if st.button(question):
        st.session_state['user_input'] = question

# User Input Area (Unlimited Size)
user_input = st.text_area(
    "✍️ Write your query here",
    key="user_input",
    height=150,  # Larger text area
    help="Enter your query about Saudi Labor Law here. Input size is unlimited."
)

# Submit Button and Chatbot Response
if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter a query before submitting.")
    else:
        with st.spinner("Processing your query..."):
            response = chatbot_response(user_input)  # Call the function from model.model
            st.markdown('<div class="ltr">✅ Response:</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="chat-response">{response}</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <div class="footer">
        All rights reserved © 2024 Qissat Tech.
    </div>
    """, unsafe_allow_html=True)
