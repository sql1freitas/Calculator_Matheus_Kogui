from django.db import models
from koguilator.validate_pass import validar_senha
import uuid

class Usuario(models.Model):

    idUsuario = models.UUIDField(primary_key=True,
                          default= uuid.uuid4,
                          editable=False)

    nome = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            verbose_name= "Nome")
    
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
    
    dtInclusao = models.DateTimeField(auto_now_add=True,
                                      null=False,
                                      blank=False,
                                      editable=False,
                                      verbose_name="Data de Inclusão")
    
class Operacao(models.Model):

    idOperacao = models.UUIDField(primary_key=True,
                                  default=uuid.uuid4,
                                  editable=False)
    
    idUsuario = models.ForeignKey(Usuario, 
                                  on_delete=models.CASCADE, 
                                  related_name= "operacoes",
                                  editable=False,
                                  verbose_name= "Usuário")
    
    parametros = models.CharField(max_length=255,
                                  null=False,
                                  blank=False,
                                  verbose_name="Parâmetros")
    
    resultado = models.CharField(max_length=255,
                                 null=False,
                                 blank=False,
                                 verbose_name="Resultado")

    dtInclusao = models.DateTimeField(auto_now_add=True,
                                      null=False,
                                      blank=False,
                                      editable=False,
                                      verbose_name="Data de Inclusão")