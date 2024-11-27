from django.urls import path
from . import views

urlpatterns = [
    path('job_description/', views.job_description_view, name='job_description_form'),
    path('job_description/<int:job_id>/', views.view_job_description, name='view_job_description'),
    path('job_description/<int:job_id>/edit_interview_questions/', views.edit_interview_questions, name='edit_interview_questions'),
     path('job-search/', views.job_search_view, name='job_search'),
]
