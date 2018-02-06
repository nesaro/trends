from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from aliexpress.forms import UserLoginForm, TrackedProduct
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from aliexpress.models import TrackedListModel, User, Product


class Register(TemplateView):

    template_name = 'register.html'
    extra_context = {'form': UserCreationForm()}

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse('Success')
        return HttpResponse('Failed, please enter again')


class Login(TemplateView):

    template_name = 'login.html'
    extra_context = {'form': UserLoginForm()}

    def post(self, request):
        user = authenticate(request,  username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponse('You have logged in!')
        return HttpResponse('Please enter correct data!')


class TrackedList(TemplateView):
    template_name = 'tracked_list.html'
    extra_context = {'form': TrackedProduct()}

    def post(self, request):
        form = TrackedProduct(request.POST)
        if form.is_valid():
            add = TrackedListModel(user=User.objects.get(username=request.user),
                                   product=Product.objects.get(pk=request.POST.get('product')))
            add.save()

            return HttpResponse('OK')
        else:
            return HttpResponse('Failed')


@login_required
def login_test(_):
    return HttpResponse('You have logged in !')


def email_test(_):
    from aliexpress.utils import send_email
    send_email('lezgintsev13@yandex.ru')

    return HttpResponse('Success!')
