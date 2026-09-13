# 🤖 AI Project Evaluator

An AI-powered web application that evaluates academic and software projects using Gemini AI.

The platform analyzes project details and uploaded documentation/source code, then provides scores, strengths, weaknesses, recommendations, and personalized AI feedback.

---

## 🚀 Features

- 🔐 User Registration & Login
- 📊 Project Evaluation Dashboard
- 🤖 Gemini AI-Powered Evaluation
- 📄 PDF & DOCX Document Analysis
- 💻 Source Code Analysis from ZIP files
- 📈 8-Category Project Scoring
- 💡 AI-Generated Strengths & Weaknesses
- 📝 Personalized Recommendations
- 📋 Detailed AI Feedback
- 📚 Evaluation History
- 🗑️ Delete Previous Evaluations
- 🌙 Light / Dark Theme
- 🔒 User-Specific Project Access

---

## 📊 Evaluation Criteria

Every project is evaluated across 8 categories:

| Criteria | Description |
|---|---|
| Problem Statement | Clarity and relevance of the problem |
| Innovation | Originality and uniqueness |
| Technical Implementation | Quality of technologies and implementation |
| Functionality | Completeness and working features |
| UI / UX | Interface design and user experience |
| Architecture | Project structure and system design |
| Documentation | Quality and completeness of documentation |
| Security | Security practices and implementation |

Each category receives a score from **0–100**.

The overall score is calculated as the average of all eight categories.

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Django

### Database
- SQLite / Django ORM

### AI
- Google Gemini API

### Document Processing
- PyPDF
- python-docx

### Development Tools
- VS Code
- Git
- GitHub

---

## ⚙️ How It Works

```text
User
  ↓
Register / Login
  ↓
Dashboard
  ↓
Enter Project Details
  ↓
Upload Project Document / Source Code
  ↓
Document & Code Extraction
  ↓
Gemini AI Analysis
  ↓
8-Category Evaluation
  ↓
Overall Score
  ↓
AI Feedback & Recommendations
  ↓
Evaluation History




### 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Ahmedbilal778/AI-Project-Evaluator.git
cd AI-Project-Evaluator

2. Create Virtual Environment
python -m venv evaluator_env

3. Activate Virtual Environment
Windows:
evaluator_env\Scripts\activate.ps1

4. Install Required Packages
pip install django google-genai python-dotenv pypdf python-docx mysqlclient

5. Configure Environment Variables
Create a .env file in the project root:
GEMINI_API_KEY=your_gemini_api_key

6. Run Database Migrations
python manage.py makemigrations
python manage.py migrate

7. Start the Development Server
python manage.py runserver:
Open the application at:
http://127.0.0.1:8000/ 



