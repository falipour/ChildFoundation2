from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Hamyar
# from .forms import HamyarForm
from karbar.models import MyUser
from django.shortcuts import render, redirect
from MySite.forms import ContactForm


class HamyarHomeView(TemplateView):
    template_name = 'hamyar/Hamyar_Home.html'


class HamyarGoalsView(TemplateView):
    template_name = 'hamyar/Hamyar_Goals.html'


class HamyarContactView(TemplateView):
    template_name = 'hamyar/Hamyar_Contact.html'


class HamyarHistoryView(TemplateView):
    template_name = 'hamyar/Hamyar_History.html'


class HamyarChartView(TemplateView):
    template_name = 'hamyar/Hamyar_Chart.html'


class EnserafView(TemplateView):
    template_name = 'hamyar/Enseraf.html'


class EntekhabView(TemplateView):
    template_name = 'hamyar/Entekhab.html'


class EhdaView(TemplateView):
    template_name = 'hamyar/Ehda.html'


class EhdaReceiptView(TemplateView):
    template_name = 'hamyar/Ehda_Receipt.html'


class LettersBoxView(TemplateView):
    template_name = 'hamyar/Letters_Box.html'


class MadadjooContactView(TemplateView):
    template_name = 'hamyar/Madadjoo_Contact.html'

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


class MadadjooListView(TemplateView):
    template_name = 'hamyar/Madadjoo_List.html'


class PayView(TemplateView):
    template_name = 'hamyar/Pay.html'


class PayReceiptView(TemplateView):
    template_name = 'hamyar/Pay_Receipt.html'


class SearchView(TemplateView):
    template_name = 'hamyar/Search.html'


class SendMessageView(TemplateView):
    template_name = 'hamyar/Send_Message.html'


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

# @login_required
# def edit_profile(request):
#     user = request.user
#     user_form = HamyarForm(instance=user)
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             user_form = HamyarForm(request.POST, instance=request.user)
#             hamyar = Hamyar.objects.get(user=request.user)
#             if user_form.is_valid():
#                 user_form.save()
#                 hamyar.user = user
#                 hamyar.report_method = request.POST.get('report-method')
#                 hamyar.save()
#                 return HttpResponseRedirect(reverse('site:manager:account'))
#         return render(request, 'hamyar/Edit_Profile.html', {'user': user, 'form': user_form})