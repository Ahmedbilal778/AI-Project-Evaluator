from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path("", views.home, name="home"), 
    path("dashboard/", views.dashboard, name="dashboard"), 
    path("evaluation/<int:project_id>/", views.evaluation,name="evaluation"), 
    path("history/", views.history, name="history"), 
    path("register/", views.register, name="register"), 
    path("login/", views.login_view, name="login"), 
    path("logout/", views.logout_view, name="logout"), 
    path("delete-project/<int:project_id>/", views.delete_project, name="delete_project"), 
]