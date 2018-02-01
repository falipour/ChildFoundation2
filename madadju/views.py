from django.shortcuts import render
from django.views.generic import TemplateView
from madadju.models import Madadju
from karbar.models import Message
from modir.models import Admin

from MySite.forms import ContactForm,MessageForm


def madadjuhome(request):
    return render(request, 'madadju/madadju.html')


def madadjugoal(request):
    return render(request, 'madadju/madadju-goals.html')


def madadjuhistory(request):
    return render(request, "madadju/madadju-history.html")


def madadjuchart(request):
    return render(request, "madadju/madadju-chart.html")


class MadadjuContact(TemplateView):
    template_name = 'madadju/madadju-contact.html'

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


def madadkarchange(request):
    if (request.GET.get('mybtn')):
        user=request.user
        admin=Admin.objects.all()
        if(type(user)==Madadju):
           madakar=Madadju.objects.filter(pk=user.pk).madadkar
           text='لطفا ممدکار مرا تغییر دهید'
        Message.objects.create(text=text, sender=user, receiver=admin)
    return render(request, "madadju/madadkarchange.html")


def madadjuprofile(request):
    return render(request, "madadju/profile.html")


class MadadjuMsg(TemplateView):
    template_name = 'madadju/sendmsg.html'

    def get(self, request, **kwargs):
        form = MessageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        sender=request.user
        form = MessageForm(request.POST)
        text = {'sender':sender}
        if form.is_valid():
            # post = form.save(commit=False)
            # post.user = request.user
            # post.save()
            form.save()
            text = form.cleaned_data
            form = MessageForm()

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


