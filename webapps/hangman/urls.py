
#from django.contrib.auth import views as auth_views
from . import views
from django.urls import include, re_path,path
from django.contrib.auth.views import LoginView,LogoutView,logout_then_login,redirect_to_login
from django.conf import Settings,settings
from django.conf.urls.static import static
urlpatterns = [
    re_path(r'^$', views.home),
    re_path(r'^login$', LoginView.as_view(), {'template_name':'login.html'}, name='login'),
    re_path(r'^logout$', logout_then_login),
    re_path(r'^register$', views.register),
    re_path(r'^game$', views.start_game)
]
"""
urlpatterns = [
    path('', views.home),
    path('login/',LoginView.as_view(), {'template_name':'login.html'}, name='login'),
    path('logout/',logout_then_login),
    path('register/',views.register),
    path('game/',views.start_game)
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)"""