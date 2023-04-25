from rest_framework import serializers
from .models import Department, Role, Emp


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            "id",
            "name",
        )


class RoleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            "id",
            "name",
        )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone",

            "salary",
            "hire_date"
        )
