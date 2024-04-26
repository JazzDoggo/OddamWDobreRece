from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from charity.models import Donation, Institution, Category
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


class DonationAddView(LoginRequiredMixin, View):
    def get(self, request):
        cnx = {
            'category_list': Category.objects.all(),
            'institution_list': Institution.objects.all(),
        }
        return render(request, 'form.html', cnx)

    def post(self, request):
        quantity = request.POST['bags']
        categories = request.POST.getlist('categories')
        institution = request.POST['organization']
        institution = Institution.objects.get(pk=institution)
        address = request.POST['address']
        phone_number = request.POST['phone']
        city = request.POST['city']
        zip_code = request.POST['postcode']
        pickup_date = request.POST['date']
        pickup_time = request.POST['time']
        pickup_comment = request.POST.get('more_info')
        user = CustomUser.objects.get(email=request.user)

        response = render(request, 'form.html')
        validators = (
            quantity is not None,
            categories is not None,
            institution is not None,
            address is not None,
            phone_number is not None,
            city is not None,
            zip_code is not None,
            pickup_date is not None,
            pickup_time is not None,
            user is not None,
        )
        print(categories)
        print(institution)
        print(validators)
        print(user)

        response = render(request, 'form.html')
        if all(validators):
            donation = Donation.objects.create(quantity=quantity,
                                               institution=institution,
                                               address=address,
                                               phone_number=phone_number,
                                               city=city,
                                               zip_code=zip_code,
                                               pickup_date=pickup_date,
                                               pickup_time=pickup_time,
                                               pickup_comment=pickup_comment,
                                               user=user)
            donation.categories.set(categories)
            donation.save()
            print(donation)
            response = render(request, 'form-confirmation.html')
        return response


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
