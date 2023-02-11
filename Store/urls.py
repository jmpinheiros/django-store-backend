from django.urls import re_path
from Store import views


# precisamos add static path para que possamos acessar as imagens
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    re_path(r'department/$',views.dapartmentApi),
    re_path(r'department/([0-9]+)$',views.dapartmentApi),
    re_path(r'employee/$',views.employeesApi),
    re_path(r'employee/([0-9]+)$',views.employeesApi),

    re_path(r'^employee/saveFile/$', views.saveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
