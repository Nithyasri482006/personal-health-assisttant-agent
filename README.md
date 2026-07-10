# 🩺 Personal Health Assistant Agent

## 📌 Project Overview
The Personal Health Assistant Agent is an AI-powered web application developed using Streamlit. It helps users manage their daily health through simple health-related tools and provides AI-based responses to health questions using the Hugging Face API.

## ✨ Features
- 🤖 AI Health Q&A
- ⚖️ BMI Calculator
- 💧 Water Intake Calculator
- 💊 Medicine Reminder
- 🌿 Daily Health Tips
- ❤️ Health Risk Checker
- 🥗 Food Suggestions

## 🛠️ Technologies Used
- Python
- Streamlit
- Hugging Face API
- Requests
- Python-dotenv

## 📂 Project Structure
```
Personal_Health_Assistant_Agent/
│── app.py
│── agent.py
│── tools.py
│── requirements.txt
│── README.md
│── .env
```

## 🚀 How to Run the Project
1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your Hugging Face API token:
   ```
   HF_TOKEN=your_huggingface_token
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## 📋 How It Works
1. The user selects a feature from the sidebar.
2. The application processes the user's input.
3. Health tools such as BMI, water intake, medicine reminders, and health tips generate instant results.
4. Health-related questions are sent to the Hugging Face AI model.
5. The AI generates a simple and personalized health response, which is displayed in the application.

