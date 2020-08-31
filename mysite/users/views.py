from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from .decorators import logout_message_required, login_message_required
from .models import User
from django.views.generic import View
from django.contrib import messages
from django.core.exceptions import PermissionDenied, ValidationError
from .forms import CsRegisterForm
from django.views.generic import CreateView
from django.urls import reverse
from .cert import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.views.generic import FormView
from django.contrib.auth import logout


def index(request):
    # ip = get_ip(request)
    # if ip is not None:
    #     print (ip)
    # else:
    #     print ("IP FIND ERROR")

    return render(request, 'users/index.html')

def logout_view(request):
    logout(request)
    return redirect('/')

@login_message_required
def main_view(request):
    """ notice_list = Notice.objects.order_by('-id')[:5]
    calendar_property = [x.event_id for x in Calender.objects.all() if x.d_day == False]
    calendar_list = Calender.objects.exclude(event_id__in=calendar_property).order_by('start_date')[:5]
    free_list = Free.objects.filter(category='Information').order_by('-id')[:5]
    anonymous_list = sorted(Anonymous.objects.all(), key=lambda t: t.like_count, reverse=True)[:5]

    context = {
        'notice_list' : notice_list,
        'calendar_list' : calendar_list,
        'free_list' : free_list,
        'anonymous_list' : anonymous_list,
    } """
    return render(request, 'users/main.html')

#@method_decorator(logout_message_required, name='dispatch')
class AgreementView(View):
    def get(self, request, *args, **kwargs):
        request.session['agreement'] = False
        return render(request, 'users/agreement.html')

    def post(self, request, *args, **kwarg):
        if request.POST.get('agreement1', False) and request.POST.get('agreement2', False):
            request.session['agreement'] = True

            if request.POST.get('csregister') == 'csregister':
                return redirect('/users/csregister/')
            else:
                return redirect('/users/register/')
        else:
            messages.info(request, "Please agree to all terms and conditions.")
            return render(request, 'users/agreement.html')

class CsRegisterView(CreateView):
    model = User
    template_name = 'users/register_cs.html'
    form_class = CsRegisterForm

    def get(self, request, *args, **kwargs):
        if not request.session.get('agreement', False):
            raise PermissionDenied
        request.session['agreement'] = False
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        self.request.session['register_auth'] = True
        messages.success(self.request, 'A verification email has been sent to the email address you entered. After authentication, you can log in.')
        return reverse('users:register_success')

    def form_valid(self, form):
        self.object = form.save()

        send_mail(
            'This is the member registration verification email of {}'.format(self.object.user_id),
            [self.object.email],
            html=render_to_string('users/register_email.html', {
                'user': self.object,
                'uid': urlsafe_base64_encode(force_bytes(self.object.pk)).encode().decode(),
                'domain': self.request.META['HTTP_HOST'],
                'token': default_token_generator.make_token(self.object),
            }),
        )
        return redirect(self.get_success_url())

def activate(request, uid64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uid64))
        current_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
        messages.error(request, 'Mail authentication failed.')
        return redirect('users:login')

    if default_token_generator.check_token(current_user, token):
        current_user.is_active = True
        current_user.save()

        messages.info(request, 'Mail authentication is complete. Congratulations on signing up!')
        return redirect('users:login')

    messages.error(request, 'Mail authentication failed.')
    return redirect('users:login')

def register_success(request):
    if not request.session.get('register_auth', False):
        raise PermissionDenied
    request.session['register_auth'] = False

    return render(request, 'users/register_success.html')

@method_decorator(logout_message_required, name='dispatch')
class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = '/users/main/'

    def form_valid(self, form):
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=user_id, password=password)

        if user is not None:
            self.request.session['user_id'] = user_id
            login(self.request, user)

        return super().form_valid(form)