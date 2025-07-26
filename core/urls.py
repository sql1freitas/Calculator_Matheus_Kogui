from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from koguilator import views


urlpatterns = [

    path("admin/", admin.site.urls),
    path("", views.calculadora_view, name="calculadora"),
    path("index/", views.login_registro_view, name="index"),
    path("logout/", LogoutView.as_view(next_page="index"), name="logout"),
    
] 

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)