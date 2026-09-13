from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):

    # Logged-in user
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="projects",
        null=True,
        blank=True
    )

    project_name = models.CharField(
        max_length=200
    )

    student_name = models.CharField(
        max_length=150
    )

    project_type = models.CharField(
        max_length=100,
        blank=True
    )

    description = models.TextField()

    technologies = models.CharField(
        max_length=500,
        blank=True
    )

    problem_statement = models.TextField(
        blank=True
    )

    objectives = models.TextField(
        blank=True
    )

    project_file = models.FileField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.project_name


class Evaluation(models.Model):

    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name="evaluation"
    )

    problem_statement_score = models.FloatField(
        default=0
    )

    innovation_score = models.FloatField(
        default=0
    )

    technical_score = models.FloatField(
        default=0
    )

    functionality_score = models.FloatField(
        default=0
    )

    ui_ux_score = models.FloatField(
        default=0
    )

    architecture_score = models.FloatField(
        default=0
    )

    documentation_score = models.FloatField(
        default=0
    )

    security_score = models.FloatField(
        default=0
    )

    overall_score = models.FloatField(
        default=0
    )

    strengths = models.TextField(
        blank=True
    )

    weaknesses = models.TextField(
        blank=True
    )

    recommendations = models.TextField(
        blank=True
    )

    ai_feedback = models.TextField(
        blank=True
    )

    evaluated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return (
            f"{self.project.project_name} "
            f"- {self.overall_score}/100"
        )