from django.contrib import admin
from django.db import router
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, EditoraViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'editora', EditoraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]