from django.urls import path
from aliexpress import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('auth', views.RegisterLogin.as_view(), name='rlogin'),
    path('test/', views.login_test, name='login_test'),
    path('track/', login_required(views.TrackedList.as_view()), name='track'),
    path('email/', views.email_test, name='email_test')

]
