# 🏅 Sportsperson Info Finder

This project is a simple web application that uses a language model to identify and provide information about famous sportspersons. It is built using **Streamlit** and **LangChain** with OpenAI-compatible APIs.

## 🧠 Technologies Used

- **Streamlit** – A framework that enables the creation of interactive web applications in a streamlined manner.
- **LangChain** – A library for simplifying work with LLMs and managing complex chatbot interactions.
- **OpenAI-Compatible LLM (e.g., DeepSeek)**

## 🔐 Setup Instructions

### 1️ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/sportsperson-info-finder.git
cd sportsperson-info-finder
```

### 2 Install required packages
```bash
pip install streamlit langchain openai
```

### 3 Run the application
```bash
streamlit run app.py
```

## 📲 App Workflow

1. User enters a name in the input field  
2. The app uses the LLM to check: "Is [name] a famous sportsperson?"  
3. If **yes**:
   - Asks: "Tell me about the sportsperson [name]"  
   - Displays the response  
4. If **no**:
   - Shows a message: "Please enter the name of a sportsperson only"
  
## ✅ Example

**Input:** `Cristiano Ronaldo`  
**Output:** _Cristiano Ronaldo is a Portuguese professional footballer who plays as a forward..._


