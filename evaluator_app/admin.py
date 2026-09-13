from django.contrib import admin
from .models import Project, Evaluation


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "project_name",
        "student_name",
        "project_type",
        "created_at",
    )

    search_fields = (
        "project_name",
        "student_name",
    )


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "overall_score",
        "evaluated_at",
    )

    search_fields = (
        "project__project_name",
    )