# Application-Development-with-Bedrock

# 🧠 AI-Powered To-Do List App (with Amazon Bedrock)

This is a full-stack to-do list web application enhanced with AI-generated suggestions using Amazon Bedrock (Claude v2). Built using Flask (Python) and deployed using AWS App Runner.

---

## 🌐 Live App

🟢 **URL**:  
[https://csw4tcrfia.us-east-2.awsapprunner.com/](https://csw4tcrfia.us-east-2.awsapprunner.com/)

---

## 🧱 Architecture Overview

### 🧩 Components

| Layer         | Technology                      |
|---------------|----------------------------------|
| Frontend      | HTML, CSS, JavaScript, Jinja2   |
| Backend       | Flask (Python)                  |
| AI Service    | Amazon Bedrock – Claude v2      |
| Deployment    | AWS App Runner                  |
| IAM Role      | AppRunnerRole with Bedrock Access |

---

### 🔄 Application Flow

```text
User Input (Goal or Task)
        ↓
Flask Frontend (Jinja Templates)
        ↓
Flask Backend (routes.py)
        ↓
Amazon Bedrock (Claude v2 API call via boto3)
        ↓
AI Suggestions Returned
        ↓
User Views Tasks in UI
