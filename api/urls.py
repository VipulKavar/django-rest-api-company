from django.urls import path, include
from .views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers

#Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
