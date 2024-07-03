from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form, name='form'),
    path('index/', views.index, name='index'),
    # other URL patterns
]
