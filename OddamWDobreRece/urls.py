"""
URL configuration for OddamWDobreRece project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from charity import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.LandingPageView.as_view(), name='index'),
    path('donation/add/', views.DonationAddView.as_view(), name='donation_add'),
    path('donation/<int:pk>/', views.DonationDetailsView.as_view(), name='donation_details'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('user/', views.UserProfileView.as_view(), name='user_profile'),

    path('verify-email/', user_views.verify_email, name='verify-email'),
    path('verify-email/done/', user_views.verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', user_views.verify_email_confirm, name='verify-email-confirm'),
    path('verify-email/complete/', user_views.verify_email_complete, name='verify-email-complete'),
]
