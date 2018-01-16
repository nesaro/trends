from django.urls import path
from aliexpress.views import Register, Login, login_test


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('test/', login_test, name='login_test')

]
