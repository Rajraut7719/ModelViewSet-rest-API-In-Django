
from django.contrib import admin
from django.db import router
from django.urls import path,include
from app import views
from rest_framework.routers import DefaultRouter
 
router=DefaultRouter()

router.register('api',views.StudentModelViewSet,basename='student')
router.register('api1',views.StudentReadOnlyViewSet,basename='student1')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
