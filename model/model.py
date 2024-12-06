import openai
from dotenv import load_dotenv
import os
from utils.language_detector import detect_language

# Load environment variables from .env file
load_dotenv()

# Set the API key
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Dynamically construct file paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARABIC_PROMPT_PATH = os.path.join(BASE_DIR, "queries", "arabic.py")
ENGLISH_PROMPT_PATH = os.path.join(BASE_DIR, "queries", "english.py")

# Load Arabic and English prompts
def load_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

arabic_data = load_prompt(ARABIC_PROMPT_PATH)
english_data = load_prompt(ENGLISH_PROMPT_PATH)

MODEL = "gpt-4o"

def chatbot_response(user_input):
    """
    Generate a response from the chatbot using OpenAI's API.

    Args:
        user_input (str): The user's input message.

    Returns:
        str: The chatbot's response or an error message if the language is unsupported.
    """
    # Detect the language of the input
    language = detect_language(user_input)

    if language == "Arabic":
        prompt = f"""أنت مساعد يقدم إجابات حول قوانين العمل في المملكة العربية السعودية بناءً على البيانات المقدمة فقط. يرجى الإجابة فقط من المعلومات المعطاة وباللغة العربية مع الإشارة إلى المرجع ومحتواه كاقتباس " ". 

---
{arabic_data}
---

عند طرح المستخدم لأسئلة، يرجى تقديم إجابة دقيقة ومختصرة باللغة العربية، باستخدام المعلومات المتوفرة فقط في قوانين العمل المقدمة، مع ذكر المرجع ومحتواه كاقتباس " ".  
لا تقم بالإجابة عن أي سؤال ليس له علاقة بقوانين العمل.
        """

    elif language == "English":
        prompt = f"""
You are an assistant that provides answers about labor laws in the Kingdom of Saudi Arabia based solely on the provided data. Please respond only using the given information, in English, and include the reference and its content as a quote " ".

---
{english_data}
---

When a user asks questions, please provide an accurate and concise response in English, using only the information available in the provided labor laws, and include the reference and its content as a quote " ".  
Do not answer any question unrelated to labor laws.
        """
    else:
        return "Unsupported language. Please use Arabic or English."

    try:
        response = openai.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0
        )
        print(response.usage)
        result = response.choices[0].message.content
        return result
    except Exception as e:
        raise RuntimeError(f"Error generating response: {str(e)}")
