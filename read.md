# HNG12 Stage 0 Public API

This is a simple **FastAPI-based** public API for **HNG12 Stage 0**. The API provides basic information, including:  

- Your registered **email** (used in the HNG12 Slack workspace).  
- The **current datetime** in ISO 8601 format (UTC).  
- A link to the **GitHub repository** of the project.  

---

## 🚀 API URL

> **🔗 URL**  

---

## 📌 Features
- **FastAPI** with a simple GET request.  
- Returns JSON response inluding email, timestamp, and GitHub URL.  
- **CORS support** for accessibility.  
- Deployed on **Render** for public access.  

---

## 🛠️ Setup Instructions (local set_up)

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/Danok01/created_Api.git
cd api

python3 -m venv venv

- Windows: venv\Scripts\activate
- Mac/Linux: source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
- The API will be available at http://127.0.0.1:5000/

```

### **2️⃣ Clone the Repository**
- URL: https://created_Api.onrender.com/

- Response Format (200 OK)

    {
    "email": "dhaniroyal01@gmail.com",
    "current_datetime": "2025-02-30T10:40:00Z",
    "github_url": "https://github.com/Danok01/created_Api"
    }


#### 📚 Example Usage
**Using curl**

- curl -X GET https://created_Api.onrender.com/

**Using Python (requests)**

```bash
import requests

url: "https://created_Api.onrender.com/"
response = requests.get(url)
print(response.json())

```

🔗 Related Resources
Looking to hire skilled Python Developers? Check out:
👉[Hire Python Developers](https://hng.tech/hire/python-developers)

📜 License: 
This project is licensed under the MIT License.

👨‍💻 Author:
Okorie Daniel

[Linkdln](https:www.linkedin.com/in/daniel-okorie)
