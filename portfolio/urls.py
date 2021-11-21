from django.contrib import admin
from django.urls import path, include
from tasks.views import TasksViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', TasksViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
]
