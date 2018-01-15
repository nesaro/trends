from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Login(View):

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return HttpResponse(render(request, 'login.html', {'form': form}))

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['user'], password=request.POST['password'])
            print(user)
            return HttpResponse('Succes')
        return redirect('aliexpress:login')

