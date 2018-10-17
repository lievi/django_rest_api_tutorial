from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a route and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnipperViewSet)
router.register(r'user', views.UserViewSet)

# The API URLS are now determined automatically by the router.
urlpatterns = [path('', include(router.urls))]
