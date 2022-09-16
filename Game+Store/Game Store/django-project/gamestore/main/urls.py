from django.urls import path
from . import views

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'accounts/login/', LoginView.as_view(
        template_name='login.html'),
         name="login"),
    path(r'accounts/logout/', LogoutView.as_view(
        next_page='/'),
         name='logout'),
    path(r'accounts/signup/', views.signup, name='signup'),
    path(r'games-list/highlighted/', views.show_highlighted_games),
    path(r'games-list/all/', views.show_all_games),
    path(r'cart/', views.ShoppingCartEditView.as_view(), name='user-cart'),
    path(r'cart/add/<int:game_id>/', views.add_to_cart),
]
