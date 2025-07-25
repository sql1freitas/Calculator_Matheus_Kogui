from django.contrib import admin
from .models import Usuario, Operacao
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = "__all__"

class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ("email", "nome")

@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    
    list_display = ("nome", "email", "is_staff", "is_active", "data_inclusao")
    list_filter = ("is_staff", "is_active", "data_inclusao")
    search_fields = ("email", "nome")
    ordering = ("nome",)
    readonly_fields = ("data_inclusao",)
    
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("nome",)}),
        (_("Permissions"), {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
        }),
        (_("Important dates"), {"fields": ("data_inclusao",)}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "nome", "password1", "password2"),
        }),
    )

@admin.register(Operacao)
class OperacaoAdmin(admin.ModelAdmin):
    
    list_display = ("nome_do_usuario", "parametros", "resultado", "data_inclusao")
    list_filter = ("data_inclusao",)
    search_fields = ("parametros", "resultado", "idUsuario__nome", "idUsuario__email")
    ordering = ("-data_inclusao",)
    readonly_fields = ("data_inclusao", "idUsuario")

    @admin.display(description="Usuário")
    def nome_do_usuario(self, obj):
        return obj.idUsuario.nome