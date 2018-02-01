from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .forms import HamyarForm
from .models import Hamyar


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

# @login_required
# def edit_profile(request):
#     user = request.user
#     form = HamyarForm(instance=user)
#
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             user_form = HamyarForm(request.POST, instance=request.user)
#             member = Member.objects.get(user=request.user)
#             if user_form.is_valid():
#                 user_form.save()
#                 member.user = request.user
#                 member.phone_number = request.POST.get('phone_number')
#                 member.save()
#                 return HttpResponseRedirect(reverse('site:manager:account'))
#     return render(request, 'manager/edit_profile.html', {'user': user, 'form': user_form})
