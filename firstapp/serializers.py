from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    emp_name = serializers.CharField(max_length = 20)
    phone = serializers.IntegerField()
    designation = serializers.CharField(max_length = 15)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.emp_name = validated_data.get('emp_name', instance.emp_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.designation= validated_data.get('designation', instance.designation)
        instance.save()
        return instance
