# Use a imagem Python base
FROM python:3.8-slim-buster

# Define o diretório de trabalho como /app
WORKDIR /app

# Copie o arquivo requirements.txt para o container
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install -r requirements.txt

# Copie todo o conteúdo da sua aplicação para o container
COPY . .

# Exponha a porta 8000 para que a aplicação possa ser acessada externamente
EXPOSE 8000

# Defina a variável de ambiente DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE Setup.settings

# Defina o comando padrão para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
