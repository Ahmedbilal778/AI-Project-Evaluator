import json
import zipfile
from pathlib import Path

from pypdf import PdfReader
from docx import Document
from dotenv import load_dotenv
from google import genai


# =========================================
# LOAD ENVIRONMENT
# =========================================

load_dotenv()

client = genai.Client()


# =========================================
# TEXT FILE EXTENSIONS
# =========================================

TEXT_EXTENSIONS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".html",
    ".htm",
    ".css",
    ".scss",
    ".sql",
    ".json",
    ".xml",
    ".txt",
    ".md",
    ".yml",
    ".yaml",
    ".java",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".php",
}


# =========================================
# PDF TEXT EXTRACTION
# =========================================

def extract_pdf_text(file_path):

    text = []

    try:

        reader = PdfReader(file_path)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text.append(page_text)

    except Exception as error:

        print("PDF Extraction Error:", error)

        return ""

    return "\n".join(text)


# =========================================
# DOCX TEXT EXTRACTION
# =========================================

def extract_docx_text(file_path):

    text = []

    try:

        document = Document(file_path)

        for paragraph in document.paragraphs:

            if paragraph.text.strip():

                text.append(paragraph.text)

    except Exception as error:

        print("DOCX Extraction Error:", error)

        return ""

    return "\n".join(text)


# =========================================
# TEXT FILE EXTRACTION
# =========================================

def extract_text_file(file_path):

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            return file.read()

    except Exception as error:

        print("Text File Extraction Error:", error)

        return ""


# =========================================
# ZIP / SOURCE CODE EXTRACTION
# =========================================

def extract_zip_text(file_path):

    extracted_files = []

    try:

        with zipfile.ZipFile(file_path, "r") as zip_file:

            for file_info in zip_file.infolist():

                if file_info.is_dir():
                    continue

                file_name = file_info.filename

                extension = Path(file_name).suffix.lower()

                if extension not in TEXT_EXTENSIONS:
                    continue

                # Avoid extremely large files
                if file_info.file_size > 500000:
                    continue

                try:

                    content = zip_file.read(
                        file_info
                    ).decode(
                        "utf-8",
                        errors="ignore"
                    )

                    extracted_files.append(
                        f"""
--- FILE: {file_name} ---

{content}
"""
                    )

                except Exception:

                    continue

    except Exception as error:

        print("ZIP Extraction Error:", error)

        return ""

    return "\n".join(extracted_files)


# =========================================
# DOCUMENT TEXT EXTRACTION
# =========================================

def extract_document_text(project):

    if not project.project_file:

        return ""

    try:

        file_path = project.project_file.path

        extension = Path(file_path).suffix.lower()


        # PDF

        if extension == ".pdf":

            return extract_pdf_text(
                file_path
            )


        # DOCX

        elif extension == ".docx":

            return extract_docx_text(
                file_path
            )


        # TXT / MD / SOURCE FILE

        elif extension in TEXT_EXTENSIONS:

            return extract_text_file(
                file_path
            )


        # ZIP SOURCE PROJECT

        elif extension == ".zip":

            return extract_zip_text(
                file_path
            )


    except Exception as error:

        print(
            "Document Extraction Error:",
            error
        )

        return ""

    return ""


# =========================================
# AI PROJECT EVALUATION
# =========================================

def evaluate_project(project):

    # =====================================
    # PROJECT INFORMATION
    # =====================================

    description = (
        project.description
        or ""
    )

    technologies = (
        project.technologies
        or ""
    )

    problem_statement = (
        project.problem_statement
        or ""
    )

    objectives = (
        project.objectives
        or ""
    )


    # =====================================
    # UPLOADED FILE
    # =====================================

    document_text = extract_document_text(
        project
    )


    # Limit extremely large documents

    document_text = document_text[:50000]


    if document_text:

        uploaded_content = document_text

    else:

        uploaded_content = (
            "No readable project document "
            "or source code was uploaded."
        )


    # =====================================
    # COMPLETE PROJECT INFORMATION
    # =====================================

    project_information = f"""
PROJECT NAME:
{project.project_name}

PROJECT TYPE:
{project.project_type}

STUDENT NAME:
{project.student_name}

DESCRIPTION:
{description}

TECHNOLOGIES:
{technologies}

PROBLEM STATEMENT:
{problem_statement}

OBJECTIVES:
{objectives}

UPLOADED PROJECT DOCUMENT / SOURCE CODE:
{uploaded_content}
"""


    # =====================================
    # GEMINI PROMPT
    # =====================================

    prompt = f"""
You are an expert academic and software
project evaluator.

Evaluate the student's project using BOTH:

1. The information entered in the form.
2. The uploaded project document or source code.

IMPORTANT:

Do not give generic evaluation.

Actually analyze the provided project
information and source code/documentation.

If source code is available, inspect it
carefully and use it when evaluating:

- Technical Implementation
- Functionality
- Architecture
- UI/UX
- Security

If documentation is available, use it when
evaluating:

- Problem Statement
- Objectives
- Documentation
- Overall quality

If information is missing, reduce the
appropriate score.

Do NOT assume features exist unless there
is evidence in the provided information
or source code.

Evaluate these 8 criteria:

1. Problem Statement
2. Innovation
3. Technical Implementation
4. Functionality
5. UI/UX
6. Architecture
7. Documentation
8. Security

Give every criterion a score from 0 to 100.

The overall score MUST be the average of
the eight criterion scores.

Also provide:

- 3 to 6 specific strengths
- 3 to 6 specific weaknesses
- 3 to 6 practical recommendations
- Detailed personalized AI feedback

The feedback must clearly refer to the
actual project instead of generic statements.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "problem_statement_score": 0,
    "innovation_score": 0,
    "technical_score": 0,
    "functionality_score": 0,
    "ui_ux_score": 0,
    "architecture_score": 0,
    "documentation_score": 0,
    "security_score": 0,
    "overall_score": 0,

    "strengths": [
        "strength 1",
        "strength 2"
    ],

    "weaknesses": [
        "weakness 1",
        "weakness 2"
    ],

    "recommendations": [
        "recommendation 1",
        "recommendation 2"
    ],

    "ai_feedback": "Detailed personalized evaluation of the actual project."
}}

PROJECT TO EVALUATE:

{project_information}
"""


    # =====================================
    # CALL GEMINI
    # =====================================

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        result = json.loads(
            response.text
        )

    except Exception as error:

        print(
            "Gemini Evaluation Error:",
            error
        )

        return {
            "problem_statement_score": 0,
            "innovation_score": 0,
            "technical_score": 0,
            "functionality_score": 0,
            "ui_ux_score": 0,
            "architecture_score": 0,
            "documentation_score": 0,
            "security_score": 0,
            "overall_score": 0,

            "strengths": (
                "AI evaluation failed."
            ),

            "weaknesses": (
                "Unable to generate AI evaluation."
            ),

            "recommendations": (
                "Please try evaluating the project again."
            ),

            "ai_feedback": (
                "Gemini AI could not evaluate "
                "this project. Please check "
                "the API configuration and try again."
            ),
        }


    # =====================================
    # CLEAN SCORES
    # =====================================

    score_fields = [
        "problem_statement_score",
        "innovation_score",
        "technical_score",
        "functionality_score",
        "ui_ux_score",
        "architecture_score",
        "documentation_score",
        "security_score",
        "overall_score",
    ]


    for field in score_fields:

        try:

            result[field] = float(
                result.get(
                    field,
                    0
                )
            )

            result[field] = max(
                0,
                min(
                    result[field],
                    100
                )
            )

        except (
            TypeError,
            ValueError
        ):

            result[field] = 0


    # =====================================
    # CALCULATE OVERALL SCORE
    # =====================================

    scores = [
        result["problem_statement_score"],
        result["innovation_score"],
        result["technical_score"],
        result["functionality_score"],
        result["ui_ux_score"],
        result["architecture_score"],
        result["documentation_score"],
        result["security_score"],
    ]


    result["overall_score"] = round(
        sum(scores) / len(scores),
        2
    )


    # =====================================
    # CONVERT LISTS TO TEXT
    # =====================================

    if isinstance(
        result.get("strengths"),
        list
    ):

        result["strengths"] = "\n".join(
            f"• {item}"
            for item in result["strengths"]
        )


    if isinstance(
        result.get("weaknesses"),
        list
    ):

        result["weaknesses"] = "\n".join(
            f"• {item}"
            for item in result["weaknesses"]
        )


    if isinstance(
        result.get("recommendations"),
        list
    ):

        result["recommendations"] = "\n".join(
            f"• {item}"
            for item in result["recommendations"]
        )


    # =====================================
    # FINAL RESULT
    # =====================================

    return result