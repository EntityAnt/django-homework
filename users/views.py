from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import UserRegisterForm
from .models import User
import secrets
from config.settings import EMAIL_HOST_USER


class UserListView(ListView):
    model = User
    template_name = 'users/users_list.html'


class UserDetailView(DetailView):
    model = User


class UserUpdateView(UpdateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:users_list')

    def get_success_url(self):
        return reverse('users:user_detail', args=[self.kwargs.get('pk')])


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users:users_list')


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirmation/{user.token}/'
        send_mail(
            subject='Подтверждение регистрации.',
            message=f'Здравствуйте! Перейдите по ссылке для подтверждения почты: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email, ],
        )
        return super().form_valid(form)


def email_confirmation(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))
