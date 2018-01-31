from django.urls import path
from aliexpress import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('test/', views.login_test, name='login_test'),
    path('track/', login_required(views.TrackedList.as_view()), name='track'),
    path('email/', views.email_test, name='email_test')

]
