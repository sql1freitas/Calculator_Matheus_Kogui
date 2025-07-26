# 🧮 Koguilator – Calculadora com Histórico e Login Seguro

**Koguilator** é uma aplicação Django que permite aos usuários realizar operações matemáticas simples (soma, subtração, multiplicação e divisão) após login, e armazena o histórico dos últimos cálculos feitos por cada usuário. O sistema também possui uma tela de registro com validação de senha segura e interface moderna.

---

## ✨ Funcionalidades

- ✅ Registro e login com validação robusta de senha
- ✅ Operações matemáticas: `+`, `-`, `×`, `÷`
- ✅ Histórico dos últimos 5 cálculos por usuário
- ✅ Logout seguro
- ✅ Interface responsiva com Tailwind CSS
- ✅ Testes automatizados com Pytest

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Django**
- **SQLite (banco local padrão)**
- **Tailwind CSS (via CDN)**
- **Pytest** para testes
- **python-decouple** para gerenciamento de variáveis de ambiente

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/koguilator.git
cd koguilator
```
### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Crie o arquivo .env
Crie um arquivo chamado .env na raiz do projeto com o seguinte conteúdo:
```bash
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```
Você pode gerar uma nova chave secreta com o comando abaixo em Python:
```bash
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

### 5. Rode as migrações

```bash
python manage.py migrate
```

### 6. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

## Para uma melhor experiência, execute o projeto utilizando Docker com os arquivos disponibilizados no repositório.




