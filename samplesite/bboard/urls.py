from django.urls import path

from .views import index, rubric_bbc

urlpatterns = [
    path('<int:rubric_id>/', rubric_bbs)
    path('', index),
]