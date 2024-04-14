from django.shortcuts import render
from django.views import View


# Create your views here.
class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html')


class DonationAddView(View):
    def get(self, request):
        return render(request, 'form.html')


class DonationConfirmView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
