from django.urls import path

from . import views

urlpatterns = [
    path('create', views.SignUp.as_view(), name='create'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('', views.default_url, name='default_url'),
    path('logout', views.logout_user, name='logout'),
    path('update/<int:pk>', views.UpdateUser.as_view(), name='update_profile')
]
