# Imagem base
FROM python:3.12-slim
# Diretório de trabalho
WORKDIR /app
# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Instalar Poetry
RUN pip install --upgrade pip && pip install poetry
# Evitar virtualenv do Poetry
RUN poetry config virtualenvs.create false
# Copiar arquivos de dependência primeiro (cache melhor)
COPY pyproject.toml poetry.lock* /app/
# Instalar dependências
RUN poetry install --no-root
# Copiar restante do projeto
COPY . /app/
# Expor porta
EXPOSE 8000
# Comando correto
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]