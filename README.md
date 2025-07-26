# 🤖 TalentScout AI Hiring Assistant

TalentScout is an interactive AI-powered chatbot built with Streamlit that collects candidate details and dynamically generates technical interview questions based on the user's tech stack using Google's Gemini API. It also uses basic sentiment analysis to detect the tone of the user's tech stack input.

---

## 🔥 Features

- Step-by-step chatbot-style UI
- Fields collected:
  - Full Name
  - Email Address
  - Phone Number
  - Years of Experience
  - Desired Position
  - Location
  - Tech Stack
- Validates user inputs (e.g., phone must be digits, email format, etc.)
- Allows user to exit any time by typing "exit"
- Uses Gemini API to generate 3–5 real-world technical questions
- Performs sentiment analysis on tech stack input (Positive/Neutral/Negative)
- Requires user consent before generating final questions ✅

---

## 📦 Requirements

These are listed in `requirements.txt`:

```txt
streamlit>=1.35.0
python-dotenv>=1.0.1
google-generativeai>=0.4.1
textblob>=0.18.0
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/talentscout-hiring-chatbot.git
cd talentscout-hiring-chatbot
```

### 2. Install dependencies

It's recommended to use a virtual environment:

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory with your Gemini API key:

```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### 4. Launch the app

```bash
streamlit run app.py
```

---

## 🦪 Example Output

```text
🤖 TalentScout AI Hiring Assistant

👋 What's your full name?
Tushar

📧 What's your email address?
tusharrathory60@gmail.com

📱 What's your phone number?
88265925678

🏥 How many years of experience do you have?
0

🌟 What's your desired position?
Backend Engineer

📍 Where are you currently located?
Gurgaon

💻 What is your tech stack?
python, nodejs, express

📜 Consent: ✅ Accepted

🧠 Detected Tone of Your Tech Stack Input: Neutral

🧪 Technical Questions:
Q1: In Python, explain the difference between __str__ and __repr__ methods and when would you use each? Provide an example.
Q2: Using NodeJS and Express, how would you set up a route that accepts a file upload and saves it to the server?
Q3: What are closures in JavaScript and how are they useful in asynchronous code?
Q4: Describe middleware chaining in Express.js. How do you handle errors in middleware functions?

🎉 You're done! Thanks for chatting.
```

---

## 📁 Folder Structure

```
.
├── app.py                 # Main Streamlit app
├── chatbot.py             # Gemini API logic
├── utils.py               # Input validation & sentiment analysis
├── .env                   # Environment file (API keys)
├── requirements.txt       # Dependencies
└── README.md              # You're here!
```

---

## 🙌 Acknowledgements

- Built using [Streamlit](https://streamlit.io)
- Powered by [Google Gemini API](https://ai.google.dev/)
- Sentiment analysis via [TextBlob](https://textblob.readthedocs.io/en/dev/)

---

## 🛡 License

MIT License – free to use, modify, and share.
