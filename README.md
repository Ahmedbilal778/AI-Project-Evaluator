# 🤖 AI Project Evaluator

An AI-powered web application that evaluates academic and software projects using Google Gemini AI.

The platform analyzes project details and uploaded documentation or source code, then provides intelligent scores, strengths, weaknesses, recommendations, and personalized AI feedback.

---

## 🚀 Features

- 🔐 User Registration & Login
- 📊 Project Evaluation Dashboard
- 🤖 Gemini AI-Powered Project Evaluation
- 📄 PDF & DOCX Document Analysis
- 💻 Source Code Analysis from ZIP Files
- 📈 8-Category Project Scoring
- 💡 AI-Generated Strengths & Weaknesses
- 📝 Personalized Recommendations
- 📋 Detailed AI Feedback
- 📚 Evaluation History
- 🗑️ Delete Previous Evaluations
- ⚠️ Delete Confirmation
- 🌙 Light / Dark Theme
- 🔒 User-Specific Project Access
- 🛡️ Django Authentication & CSRF Protection

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

The overall score is calculated as the average of all eight criteria.

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
- MySQL
- Django ORM

### Artificial Intelligence
- Google Gemini API
- `google-genai`

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
Individual Scores
  ↓
Overall Score
  ↓
Strengths + Weaknesses
  ↓
Recommendations + AI Feedback
  ↓
Evaluation History

📁 Project Structure
AI-Project-Evaluator/
│
├── evaluator/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── evaluator_app/
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_project_user.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── ai_service.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── dashboard.html
│   ├── evaluation.html
│   ├── history.html
│   ├── login.html
│   ├── register.html
│   └── confirm_delete.html
│
├── manage.py
├── .gitignore
└── README.md

🔧 Installation & Setup

1. Clone the Repository
git clone https://github.com/Ahmedbilal778/AI-Project-Evaluator.git
cd AI-Project-Evaluator

2. Create Virtual Environment
python -m venv evaluator_env

3. Activate Virtual Environment
Windows PowerShell
.\evaluator_env\Scripts\Activate.ps1
Windows CMD
evaluator_env\Scripts\activate.ps1

4. Install Required Packages
pip install django google-genai python-dotenv pypdf python-docx mysqlclient

5. Configure MySQL
Create a MySQL database and configure the database connection in:
evaluator/settings.py
Add your own:
Database name
Username
Password
Host
Port

6. Configure Gemini API
Create a .env file in the project root:
GEMINI_API_KEY=your_gemini_api_key
Never upload your API key or .env file to GitHub.

7. Run Migrations
python manage.py makemigrations
python manage.py migrate
8. Start the Development Server
python manage.py runserver

Open the application:

http://127.0.0.1:8000/


🤖 AI Evaluation

The system evaluates projects using both the information entered by the user and available uploaded content.

Input Considered:
-Project Name
-Project Type
-Student Name
-Project Description
-Technology Stack
-Problem Statement
-Project Objectives
-Uploaded Documentation
-Uploaded Source Code

AI Output:
Gemini generates:

-Problem Statement Score
-Innovation Score
-Technical Implementation Score
-Functionality Score
-UI / UX Score
-Architecture Score
-Documentation Score
-Security Score
-Overall Score
-Strengths
-Weaknesses
-Recommendations
-Personalized AI Feedback
The application calculates the final overall score from the eight individual evaluation scores.

📄 Supported Files:
The evaluator supports:

-PDF
-DOCX
-TXT
-Markdown
-Source Code Files
-ZIP Project Files
ZIP files can contain supported source-code files such as:

-Python
-JavaScript
-HTML
-CSS
-Java
-C / C++
-SQL
-JSON
-PHP
The system extracts readable content from supported files and sends it to Gemini for analysis.

🔐 Security:
-Django user authentication
-Login-protected dashboard
-User-specific project access
-User-specific evaluation history
-CSRF protection
-Protected API credentials using .env
-User-specific project deletion
-Confirmation before project deletion
API credentials are not stored directly inside the source code.

📚 Main Application Pages
Home:

Introduces the platform, its features, workflow, and AI evaluation capabilities.

Register:

Allows new users to create an account.

Login:

Authenticates existing users.

Dashboard:

Allows users to submit project details and upload documentation/source code.

Evaluation Result:

Displays the complete AI-generated evaluation.

Evaluation History:

Shows previously evaluated projects along with:

-Total Projects
-Average Score
-Highest Score
-Individual Project Scores
-Delete Confirmation
Provides a confirmation screen before permanently deleting a project.

🎯 Future Improvements
📑 Downloadable PDF Evaluation Reports
📊 Advanced Evaluation Analytics
📈 Score Charts & Visualizations
👨‍🏫 Teacher / Admin Panel
📱 Further Mobile Optimization
☁️ Cloud Deployment
🔔 Notifications
📌 Project Comparison
📚 Evaluation Export


👨‍💻 Author
Ahmed Bilal

Computer Science Student & Full-Stack Developer

-Skills
-Python
-Django
-JavaScript
-HTML
-Bootstrap
-CSS
-SQL
-Git & GitHub
-AI Integration

⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.