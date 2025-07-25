from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from koguilator.validate_pass import validar_senha
import uuid


class UsuarioManager(BaseUserManager):
    
    def create_user(self, email, 
                    nome, password=None, 
                    **extra_fields):
        
        if not email:
            raise ValueError("O e-mail é obrigatório")
        
        email = self.normalize_email(email)

        user = self.model(email=email, nome=nome, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, 
                         nome, password=None, 
                         **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, nome, password, **extra_fields)
    
    def get_by_natural_key(self, email):
        return self.get(email=email)


class Usuario(AbstractBaseUser, PermissionsMixin):

    id_usuario = models.UUIDField(primary_key=True,
                          default= uuid.uuid4,
                          editable=False)

    nome = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            verbose_name="Nome")
    
    email = models.CharField(max_length=255,
                             null=False,
                             blank=False,
                             unique=True,
                             verbose_name="Email")

    senha = models.CharField(max_length=128,
                             validators=[validar_senha],
                             null=False,
                             blank=False,
                             verbose_name="Senha")
    
    data_inclusao = models.DateTimeField(auto_now_add=True,
                                      null=False,
                                      blank=False,
                                      verbose_name="Data de Inclusão")
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    def __str__(self):
        return self.email
  
    
class Operacao(models.Model):

    id_operacao = models.UUIDField(primary_key=True,
                                  default=uuid.uuid4,
                                  editable=False)
    
    idUsuario = models.ForeignKey(Usuario, 
                                  on_delete=models.CASCADE, 
                                  related_name="operacoes",
                                  editable=False,
                                  verbose_name="Usuário")
    
    parametros = models.CharField(max_length=255,
                                  null=False,
                                  blank=False,
                                  verbose_name="Parâmetros")
    
    resultado = models.CharField(max_length=255,
                                 null=False,
                                 blank=False,
                                 verbose_name="Resultado")

    data_inclusao = models.DateTimeField(auto_now_add=True,
                                      null=False,
                                      blank=False,
                                      verbose_name="Data de Inclusão")

