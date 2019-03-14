from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'post_api'

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
