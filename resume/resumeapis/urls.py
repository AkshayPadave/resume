from django.urls import path
from . import views

urlpatterns = [
    path('template1/', views.Template.template1, name="template1")
]


