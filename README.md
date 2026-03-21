# 🎬 CineReserve API

API RESTful para gerenciamento de sessões de cinema, reservas de assentos e geração de tickets

---

## 🚀 Tecnologias utilizadas

- Python 3.12
- Django
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Poetry
- JWT (SimpleJWT)

---

## 📦 Funcionalidades

- 🔐 Autenticação com JWT
- 🎥 CRUD de filmes
- 🕒 CRUD de sessões
- 🔎 Listagem de sessões por filme
- 💺 Reserva de assentos com lock de 10 minutos
- ❌ Cancelamento de reservas
- 🎟️ Geração de tickets (Purchased)
- 👤 Gestão de usuários
- 📄 Documentação com Swagger

---

## ⚙️ Pré-requisitos

Antes de começar, você precisa ter instalado:

- Docker
- Docker Compose

---

## 🐳 Como rodar o projeto (Docker)

### 1. Clonar o repositório

```bash
git clone https://github.com/Luisf66/cinereserve.git
cd cinereserve
```
### 2. Criar .env

- Copiar o .env_example para um .env
- Criar uma chave com o comando
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 3. Subir os containers 

```bash
docker compose up --build
```
### 4. Se necessário 

- aplique as migrations com migrate
- crie um superusuário com createsuperuser

### 5. Acesse a aplicação

- http://127.0.0.1:8000/api/docs/#/

  
