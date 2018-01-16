from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from aliexpress.forms import UserLoginForm, TrackedProduct
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


class Register(TemplateView):

    template_name = 'register.html'
    extra_context = {'form': UserCreationForm()}

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse('Succes')
        return HttpResponse('Fail')


class Login(TemplateView):

    template_name = 'login.html'
    extra_context = {'form': UserLoginForm()}

    def post(self, request):
        form = UserLoginForm(request.POST)
        user = authenticate(request,
                         username=request.POST.get('username'),
                         password=request.POST.get('password'))
        if user.is_active:
            login(request, user)
            return HttpResponse('You have logged in!')
        return HttpResponse('Please enter correct data!')


class TrackedList(TemplateView):
    template_name = 'tracked_list.html'
    extra_context = {'form': TrackedProduct()}

    def post(self, request):
        form = TrackedProduct(request.POST)
        if form.is_valid():
            return HttpResponse('OK')
        else:
            return HttpResponse('Failed')


@login_required
def login_test(request):
    return HttpResponse('You are logged in!')
