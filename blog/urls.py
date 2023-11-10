
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="blog"),
   path('<int:pk>/', views.single_post_page, name="single_post_page"),
]

