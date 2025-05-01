from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('post_job/', views.post_job, name='post_job'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
]
