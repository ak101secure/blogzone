
# blog/urls.py
from django.urls import path
from . import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostUpdateView, PostDeleteView

urlpatterns = [
    
    path('', views.home, name='home'),
    path('post/<int:pk>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('search/', views.search, name='search'),
    

]
