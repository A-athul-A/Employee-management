from django.urls import path, include
from .views import Role,Employee, Department

urlpatterns = [
    path("", Employee.as_view(), name="employee"),
    path("department/", Department.as_view(), name="department"),
    path("role/", Role.as_view(), name="role"),

]
