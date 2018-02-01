from django.views.generic import TemplateView


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
