# Chatbot API

A simple RESTful API for interacting with a chatbot. This API processes user input and provides chatbot responses.

---

## Features
- **API Endpoint**: `/chat` for chatbot interaction.
- **Input Validation**: Ensures valid input is provided.
- **Error Handling**: Handles processing errors gracefully.

---

## Requirements

- Python 3.7+
- Flask

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/chatbot-api.git
    cd chatbot-api
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. **Start the API**:
    ```bash
    python main.py
    ```

2. **POST Request** to `/chat`:
   - **Payload**:
     ```json
     {
       "user_input": "Hello, chatbot!"
     }
     ```
   - **Response**:
     ```json
     {
       "response": "Hello! How can I help you today?"
     }
     ```

---

# TEST
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"user_input": "What is the process for resolving labor disputes, and how does the WIDI platform facilitate this?"}'


{
  "response": "The process for resolving labor disputes in the Kingdom of Saudi Arabia involves several steps, including the use of the WIDI platform. According to the provided labor laws:\n\n\"### **Labor Disputes and Resolution**\n\n#### **1. Filing Complaints**:\n- Workers and employers can file disputes on the **WIDI platform** for amicable settlement.\n- If no resolution is achieved, disputes are escalated to labor courts.\" \n\nThis indicates that the WIDI platform is used as an initial step for filing complaints and seeking amicable settlements between workers and employers. If the disputes are not resolved through the platform, they are then escalated to labor courts for further adjudication."
}


### cURL Request:
```bash
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"user_input": "ما هي الحالات التي يحق فيها للعامل ترك العمل دون إشعار مع الاحتفاظ بحقوقه؟"}'
```

### Response:
```json
{
  "response": "يحق للعامل ترك العمل دون إشعار في حالة عدم التزام صاحب العمل بتعهداته العقدية. وفقًا للمعلومات المقدمة: \"يمكن للعامل ترك العمل دون إشعار في حالة عدم التزام صاحب العمل بتعهداته العقدية.\""
}
```