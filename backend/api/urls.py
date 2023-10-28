from django.urls import include, path, re_path
from djoser import views
from rest_framework.routers import DefaultRouter

from .views import (IngredientViewSet,
                    RecipesViewSet,
                    TagViewSet)

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tags', TagViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
