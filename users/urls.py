from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_confirmation, UserUpdateView, UserDeleteView, UserListView, UserDetailView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirmation/<str:token>/', email_confirmation, name='email-confirmation'),

    path('users/new/', UserCreateView.as_view(), name='user_new'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('', UserListView.as_view(), name='users_list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user_detail'),


]
