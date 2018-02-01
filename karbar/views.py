from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from modir.models import Admin
from madadkar.models import Madadkar
from madadju.models import Madadju
from hamyar.models import Hamyar
from .forms import LoginForm
from .models import MyUser


def login(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('submit') == 'ورود':
            form = LoginForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    member = MyUser.objects.get(user=user)
                    try:
                        MyUser.objects.get(member=member)
                        return HttpResponseRedirect(reverse('modir:admin-home'))
                    except Admin.DoesNotExist and Madadkar.DoesNotExist and Madadju.DoesNotExist:
                        return HttpResponseRedirect(reverse('hamyar:hamyar-home'))
                    except Admin.DoesNotExist and Madadkar.DoesNotExist and Hamyar.DoesNotExist:
                        return HttpResponseRedirect(reverse('madadju:madadju-home'))
                    except Admin.DoesNotExist and Madadju.DoesNotExist and Hamyar.DoesNotExist:
                        return HttpResponseRedirect(reverse('madadkar:madadkar-home'))

                else:
                    message = 'حساب شما غیر فعال شده است.'
            else:
                message = 'نام کاربری شناخته شده نیست. لطفا ابتدا عضو شوید.'
            context = {'type': 'login', 'form': form, 'message': message}
    return render(request, 'MySite/login.html', context)
