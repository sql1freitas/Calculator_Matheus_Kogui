from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from koguilator.models import Operacao
from django.shortcuts import render, redirect
from django.contrib.auth import login
from koguilator.models import Usuario
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError

from django.core.exceptions import ValidationError

def login_registro_view(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "login":
            email = request.POST.get("username")
            senha = request.POST.get("password")
            user = authenticate(request, username=email, password=senha)
            if user is not None:
                login(request, user)
                return redirect("calculadora")
            else:
                return render(request, "index.html", {"login_erro": "Credenciais inválidas."})

        elif form_type == "registro":
            nome = request.POST.get("nome")
            email = request.POST.get("email")
            senha = request.POST.get("senha")
            confirmar = request.POST.get("confirmar_senha")

            if senha != confirmar:
                return render(request, "index.html", {"registro_erro": "As senhas não coincidem."})

            if Usuario.objects.filter(email=email).exists():
                return render(request, "index.html", {"registro_erro": "Email já registrado."})

            try:
                usuario = Usuario.objects.create_user(email=email, nome=nome, password=senha)
                login(request, usuario)
                return redirect("calculadora")

            except ValidationError as e:
                erro_msg = e.messages[0] if e.messages else "Erro ao registrar."
                return render(request, "index.html", {
                    "registro_erro": erro_msg,
                    "registro_ativo": True
                })

            except Exception as e:
                return render(request, "index.html", {
                    "registro_erro": str(e),
                    "registro_ativo": True
                })

    return render(request, "index.html")



@login_required
def calculadora_view(request):
    resultado = None
    operacao_realizada = None

    if request.method == "POST":
        valor1 = float(request.POST["valor1"])
        valor2 = float(request.POST["valor2"])
        operacao = request.POST["operacao"]
        operacao_realizada = f"{valor1} {operacao} {valor2}"

        if operacao == "soma":
            resultado = valor1 + valor2
            operacao_realizada = f"{valor1} + {valor2}"

        elif operacao == "subtracao":
            resultado = valor1 - valor2
            operacao_realizada = f"{valor1} - {valor2}"

        elif operacao == "multiplicacao":
            resultado = valor1 * valor2
            operacao_realizada = f"{valor1} × {valor2}"

        elif operacao == "divisao":
            if valor2 == 0:
                resultado = "Erro: divisão por zero"
            else:
                resultado = valor1 / valor2
                operacao_realizada = f"{valor1} ÷ {valor2}"

        if isinstance(resultado, (float, int)):
            Operacao.objects.create(
                idUsuario=request.user,
                parametros=operacao_realizada,
                resultado=str(resultado)
            )

    historico = Operacao.objects.filter(idUsuario=request.user).order_by('-data_inclusao')[:5]

    return render(request, "calculadora.html", {
        "resultado": resultado,
        "historico": historico
    })