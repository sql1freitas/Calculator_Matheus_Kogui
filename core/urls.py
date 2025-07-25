from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from koguilator import views

urlpatterns = [

    path("admin/", admin.site.urls),
    path('', views.calculadora_view, name='calculadora'),
    path('auth/', views.login_registro_view, name='login_registro'),
    path('logout/', LogoutView.as_view(next_page='login_registro'), name='logout'),
]


