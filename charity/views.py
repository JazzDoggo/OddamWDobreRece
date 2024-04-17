from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from charity.models import Donation, Institution
from users.models import CustomUser


# Create your views here.
class LandingPageView(View):
    def get(self, request):
        no_donations = sum([donation.quantity for donation in Donation.objects.all()])
        no_charities = Institution.objects.filter(donation__isnull=False).count()
        cnx = {
            'no_donations': no_donations,
            'no_institutions': no_charities,
            'foundations': Institution.objects.filter(type=1),
            'ngos': Institution.objects.filter(type=2),
            'local_charities': Institution.objects.filter(type=3),

        }
        return render(request, 'index.html', cnx)


class DonationAddView(View):
    def get(self, request):
        return render(request, 'form.html')


class DonationConfirmView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        validators = (
            email is not None,
            password is not None,
        )

        response = render(request, 'login.html')
        if all(validators):
            response = redirect('register')
            if CustomUser.objects.filter(email=email).exists():
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    response = redirect('index')
        return response


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        first_name = request.POST.get('name')
        last_name = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        validations = (
            first_name is not None,
            last_name is not None,
            email is not None,
            password is not None,
            password2 is not None,
            password == password2,
        )

        response = render(request, 'register.html')
        if all(validations):
            user = CustomUser.objects.create(first_name=first_name, last_name=last_name, email=email)
            user.set_password(password)
            user.save()
            response = redirect('login')
        return response
