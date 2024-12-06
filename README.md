TEST
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