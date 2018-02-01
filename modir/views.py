from django.contrib.auth import authenticate, login as auth_login
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

import time
from datetime import date

from MySite.forms import ContactForm
from karbar.forms import SignupForm1
from karbar.models import MyUser
from hamyar.models import Hamyar
from madadkar.models import Madadkar


class AdminGoalsView(TemplateView):
    template_name = 'modir/Admin_Goals.html'


class AdminHomeView(TemplateView):
    template_name = 'modir/Admin_Home.html'


class AdminContactView(TemplateView):
    template_name = 'modir/Admin_Contact.html'

    def get(self, request, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        text = None
        if form.is_valid():
            # post = form.save(commit=False)
            # post.user = request.user
            # post.save()
            form.save()
            text = form.cleaned_data
            form = ContactForm()

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


class AdminHistoryView(TemplateView):
    template_name = 'modir/Admin_History.html'


class AdminChartView(TemplateView):
    template_name = 'modir/Admin_Chart.html'


class AdminHamyarRegisterView(View):
    template_name = 'modir/Hamyar_Register.html'

    def get(self, request, **kwargs):
        form = SignupForm1()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignupForm1(request.POST)
        phone_number = request.POST.get('phone_number')
        national_id = request.POST.get('national_id')
        country = request.POST.get('country')
        city = request.POST.get('city')
        address = request.POST.get('address')
        postal_code = request.POST.get('postal_code')
        report_method = request.POST.get('report_method')
        context = {'phone_number': phone_number, 'report_method': report_method, 'country': country, 'city': city,
                   'postal_code': postal_code, 'address': address, national_id: 'national_id'}
        if form.is_valid():
            print('valiid')
            if len(phone_number) == 11 and phone_number[0:2] == '09':
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                auth_login(request, user)
                member = MyUser.objects.create(user=user, phone_number=phone_number, country=country, city=city,
                                               postal_code=postal_code, address=address, national_id=national_id)
                member.save()
                hamyar = Hamyar.objects.create(user=member, report_method=report_method)
                hamyar.save()
                return HttpResponseRedirect(reverse('hamyar-home'))
            else:
                phone_number_error = "شماره تلفن باید 11 رقمی باشد و با 09 آغاز شود."
                context['phone_number_error'] = phone_number_error
        context['form'] = form
        context['type'] = 'signup'
        return render(request, 'modir/Hamyar_Register.html', context)


class AdminMadadkarRegisterView(View):
    template_name = 'modir/Madadkar_Register.html'

    def get(self, request, **kwargs):
        form = SignupForm1()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignupForm1(request.POST)
        phone_number = request.POST.get('phone_number')
        national_id = request.POST.get('national_id')
        country = request.POST.get('country')
        city = request.POST.get('city')
        address = request.POST.get('address')
        postal_code = request.POST.get('postal_code')
        employment_date = date.today().isoformat()
        context = {'phone_number': phone_number, 'employment_date': employment_date, 'country': country, 'city': city,
                   'postal_code': postal_code, 'address': address, national_id: 'national_id'}
        if form.is_valid():
            print('valiid')
            if len(phone_number) == 11 and phone_number[0:2] == '09':
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                auth_login(request, user)
                member = MyUser.objects.create(user=user, phone_number=phone_number, country=country, city=city,
                                               postal_code=postal_code, address=address, national_id=national_id)
                member.save()
                madadkar = Madadkar.objects.create(user=member, employment_date=employment_date)
                madadkar.save()
                return HttpResponseRedirect(reverse('madadkar-home'))
            else:
                phone_number_error = "شماره تلفن باید 11 رقمی باشد و با 09 آغاز شود."
                context['phone_number_error'] = phone_number_error
        context['form'] = form
        context['type'] = 'signup'
        return render(request, 'modir/Madadkar_Register.html', context)