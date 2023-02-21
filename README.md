# Criar venv
    python3 -m venv venv
    source venv/bin/activate
    
# Instalar pacote pip
    pip install django
    pip install djangorestframework
    pip install django-cors-headers

# Criar projeto django
    django-admin startproject Setup 
# Criar app django
    python manage.py startapp app

# Criar super user
    python manage.py createsuperuser

# dentro de settings.py
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

# No Setup/settings.py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'app',
        'rest_framework',
        'corsheaders',
    ]

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
    ]

# Importante para não bloquear o REACT
    REST_FRAMEWORK = {'DEFAULT_PERMISSION_CLASSES':[
            'rest_framework.permissions.AllowAny']}

# aceita requisição de todos 
    CORS_ORIGIN_ALLOW_ALL = True


## views e urls
    Nesse projeto não usamos router no url, nem viewset no views.
    usamos maneira antiga de fazer, criando funções na viwe e usando re_path para adicionar as urls do arquivo url.py

# ViewSets
    ViewSets are just a type of class based view but it do not provide request method handlers like "get ()", "post ()", "patch ()", "delete ()", etc. But, it provides actions such as "create ()", "list ()", "retrieve ()", "update ()", "partial_update ()" and "destroy ()".


# Upload de Imagens
    Dentro do backend criamos a pasta /media
    colocamos nossas imagens nela

# No arquivo settings.py adicione o caminho
    import os
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR,"media")

# Crie o método para pegar as imagens no views

# adicione o caminho as urls do projeto static path


## FRONTEND ##

    react store-frontend
