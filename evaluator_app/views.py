from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Project, Evaluation
from .ai_service import evaluate_project


# =========================================
# HOME
# =========================================

def home(request):
    return render(request, "home.html")


# =========================================
# REGISTER
# =========================================

def register(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(
                request,
                "register.html",
                {"error": "Passwords do not match."}
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "register.html",
                {"error": "Username already exists."}
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect("dashboard")

    return render(request, "register.html")


# =========================================
# LOGIN
# =========================================

def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")
    
        return render(
            request,
            "login.html",
            {"error": "Invalid username or password."}
        )

    return render(request, "login.html")


# =========================================
# LOGOUT
# =========================================

def logout_view(request):

    logout(request)

    return redirect("home")


# =========================================
# DASHBOARD
# =========================================

@login_required(login_url="login")
def dashboard(request):

    if request.method == "POST":

        project_name = request.POST.get("project_name")
        student_name = request.POST.get("student_name")
        project_type = request.POST.get("project_type")
        description = request.POST.get("project_description")
        technologies = request.POST.get("technology")
        problem_statement = request.POST.get("problem_statement")
        objectives = request.POST.get("objectives")
        project_file = request.FILES.get("project_file")

        # SAVE PROJECT

        project = Project.objects.create(
            user=request.user,
            project_name=project_name,
            student_name=student_name,
            project_type=project_type,
            description=description,
            technologies=technologies,
            problem_statement=problem_statement,
            objectives=objectives,
            project_file=project_file,
        )

        # AI EVALUATION

        ai_result = evaluate_project(project)

        # SAVE EVALUATION

        Evaluation.objects.create(
            project=project,

            problem_statement_score=ai_result["problem_statement_score"],
            innovation_score=ai_result["innovation_score"],
            technical_score=ai_result["technical_score"],
            functionality_score=ai_result["functionality_score"],
            ui_ux_score=ai_result["ui_ux_score"],
            architecture_score=ai_result["architecture_score"],
            documentation_score=ai_result["documentation_score"],
            security_score=ai_result["security_score"],

            overall_score=ai_result["overall_score"],

            strengths=ai_result["strengths"],
            weaknesses=ai_result["weaknesses"],
            recommendations=ai_result["recommendations"],
            ai_feedback=ai_result["ai_feedback"],
        )

        return redirect(
            "evaluation",
            project_id=project.id
        )

    # CURRENT USER PROJECT COUNT

    projects_count = Project.objects.filter(
        user=request.user
    ).count()

    return render(
        request,
        "dashboard.html",
        {
            "projects_count": projects_count,
        }
    )


# =========================================
# EVALUATION
# =========================================

@login_required(login_url="login")
def evaluation(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id,
        user=request.user
    )

    evaluation = Evaluation.objects.filter(
        project=project
    ).first()

    if evaluation is None:
        evaluation = Evaluation.objects.create(
            project=project
        )

    return render(
        request,
        "evaluation.html",
        {
            "project": project,
            "evaluation": evaluation,
        }
    )


# =========================================
# EVALUATION HISTORY
# =========================================

@login_required(login_url="login")
def history(request):

    # Only logged-in user's projects

    projects = Project.objects.filter(
        user=request.user
    ).select_related(
        "evaluation"
    ).order_by(
        "-created_at"
    )

    # Total projects

    total_projects = projects.count()

    # All evaluation scores

    scores = [
        project.evaluation.overall_score
        for project in projects
        if hasattr(project, "evaluation")
    ]

    # Average & highest score

    if scores:

        average_score = round(
            sum(scores) / len(scores),
            2
        )

        highest_score = max(scores)

    else:

        average_score = 0
        highest_score = 0

    return render(
        request,
        "history.html",
        {
            "projects": projects,
            "total_projects": total_projects,
            "average_score": average_score,
            "highest_score": highest_score,
        }
    )

# =========================================
# DELETE PROJECT
# =========================================

@login_required(login_url="login")
def delete_project(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id,
        user=request.user
    )

    # GET request → confirmation page
    if request.method == "GET":
        return render(
            request,
            "confirm_delete.html",
            {
                "project": project,
            }
        )

    # POST request → actually delete
    if request.method == "POST":
        project.delete()
        return redirect("history")