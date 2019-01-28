from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('add_instructor', views.add_instructor, name='add_instructor'),
    # path('instructor_approve/<int:user_id>/', views.instructor_approve, name='instructor_approve')
    
]

