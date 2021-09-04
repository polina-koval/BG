from django.urls import path

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.register, name='register'),
    path('dashboard/', views.view_profile, name='view_profile'),
    path('dashboard/edit', views.edit_profile, name='edit_profile'),
    path('dashboard/change-password', views.change_password, name='change_password'),
]
