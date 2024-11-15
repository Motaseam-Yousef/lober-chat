import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the API key
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Load data from file
file_path = r'data/clean/ar.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.readlines()

# Chatbot prompt setup
prompt = f"""
أنت مساعد يقدم إجابات حول قوانين العمل في المملكة العربية السعودية بناءً على البيانات المقدمة فقط. يرجى الإجابة فقط من المعلومات المعطاة وباللغة العربية.

---
{data}
---

عند طرح المستخدم لأسئلة، يرجى تقديم إجابة دقيقة ومختصرة باللغة العربية، باستخدام المعلومات المتوفرة فقط في قوانين العمل المقدمة.
"""

MODEL = "gpt-4o"

# Define a function to respond as a customer service chatbot
def chatbot_response(user_input):
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

# Streamlit app layout
st.set_page_config(page_title="شات بوت لمساعدة في قانون العمل السعودي", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS for RTL styling and improved UI
st.markdown("""
    <style>
        .rtl {direction: rtl; text-align: right;}
        .stTextArea textarea {direction: rtl; text-align: right; font-size: 1.1em; background-color: #fdfdfd; padding: 10px; border-radius: 8px; border: 1px solid #ddd;}
        .stButton button {width: 100%; font-size: 1.2em; padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 8px; cursor: pointer;}
        .stButton button:hover {background-color: #45a049;}
        .chat-container {background-color: #f9f9f9; padding: 15px; border-radius: 8px; border: 1px solid #ddd; margin-top: 10px;}
        .chat-response {background-color: #e8f5e9; padding: 15px; border-radius: 8px; font-size: 1.1em; margin-top: 10px;}
        .footer {text-align: center; font-size: 0.9em; color: #888; margin-top: 30px;}
    </style>
    """, unsafe_allow_html=True)

# Main Interface
st.markdown("<h1 style='text-align: right;'>🤖 شات بوت للمساعدة في قانون العمل السعودي</h1>", unsafe_allow_html=True)
st.markdown('<div class="rtl">💼 مرحباً بك! كيف يمكنني مساعدتك؟</div>', unsafe_allow_html=True)

# Recommended Questions
st.markdown("<h3 style='text-align: right;'>❓ أسئلة مقترحة:</h3>", unsafe_allow_html=True)
recommended_questions = [
    "ما هي الشروط الأساسية التي يجب أن يتضمنها عقد العمل وفقًا لنظام العمل السعودي؟",
    "كيف يتم توثيق عقد العمل إلكترونيًا، وما هي الفائدة من هذا التوثيق؟",
    "ما هي حقوق العامل أثناء فترة التجربة، وهل يمكن تمديدها؟",
    "ما هي واجبات العامل تجاه صاحب العمل، وما الذي يجب عليه الالتزام به؟",
    "ما هي أنواع الإجازات التي يحق للعامل الحصول عليها وفقًا للنظام؟",
    "ما هي حقوق المرأة العاملة خلال فترة الحمل وإجازة الوضع؟",
    "كيف يتم احتساب ساعات العمل، وما هي الاستثناءات المطبقة خلال شهر رمضان؟",
    "ما هي الخطوات التي يجب اتباعها لتقديم شكوى أو تظلم في حال حدوث نزاع بين العامل وصاحب العمل؟",
    "ما هي الحالات التي يحق فيها للعامل ترك العمل دون إشعار مع الاحتفاظ بحقوقه؟",
    "كيف يتم التعامل مع الأجور، وما هي الشروط المتعلقة بدفع الرواتب واقتطاعات التأمينات الاجتماعية؟"
]

# Display recommended questions as clickable options
for question in recommended_questions:
    if st.button(question):
        st.session_state['user_input'] = question

# Chat Input
user_input = st.text_area("✍️ اكتب استفسارك هنا", key="user_input", max_chars=300, help="اكتب استفسارك حول قانون العمل السعودي هنا")

# Submit button
if st.button('إرسال'):
    if user_input.strip() == "":
        st.warning("الرجاء كتابة استفسار قبل الإرسال.")
    else:
        with st.spinner('جاري معالجة استفسارك...'):
            chatbot_reply = chatbot_response(user_input)
            
            # Display response
            st.markdown('<div class="rtl">✅ تم الرد:</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="rtl chat-response">{chatbot_reply}</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <hr>
    <div class="footer">
        جميع الحقوق محفوظة © 2024 قصة تك.
    </div>
    """, unsafe_allow_html=True)
