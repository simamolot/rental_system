"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static

# Настройка Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Rental Housing API",
        default_version='v1',
        description="Backend application for renting and renting housing",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,  # Измените на False, если требуется закрытый доступ
)

# Основные пути
urlpatterns = [
    path('admin/', admin.site.urls),  # Админ-панель
    path('', include('apps.router')),  # Основные маршруты приложения
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger-документация
]

# Подключение статических и медиа-файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



