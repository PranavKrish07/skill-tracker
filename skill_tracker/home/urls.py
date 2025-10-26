from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signUpView.as_view(), name='signup'),
    path('home/', views.home, name='home'),
    path('addskill/', views.addSkill, name='addskill'),
    path('<str:sk>/', views.skills, name='skills'),
    path('<str:sk>/delete/', views.deleteSkill, name='delete_skill'),
]