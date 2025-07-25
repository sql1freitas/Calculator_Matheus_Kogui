import re
from django.core.exceptions import ValidationError

def validar_senha(valor):
    if len(valor) < 8:
        raise ValidationError("A senha deve ter no mínimo 8 caracteres.")

    if not re.search(r'[A-Z]', valor):
        raise ValidationError("A senha deve conter ao menos uma letra maiúscula.")

    if not re.search(r'[a-zA-Z]', valor):
        raise ValidationError("A senha deve conter letras.")

    if not re.search(r'\d', valor):
        raise ValidationError("A senha deve conter ao menos um número.")

    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]', valor):
        raise ValidationError("A senha deve conter ao menos um caractere especial.")
