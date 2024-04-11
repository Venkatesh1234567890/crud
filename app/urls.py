

from django.urls import path
from.import views

from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('insert/', views.insertdata, name="insertdata"),
    path('update/<id>', views.updatedata, name="updatedata"),

    path('delete/<id>', views.deletedata, name="deletedata"),  # Fix the view name here
]