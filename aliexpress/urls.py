from django.urls import path
from aliexpress.views import Login


urlpatterns = [
    path('login/', Login.as_view(), name='login')

]
