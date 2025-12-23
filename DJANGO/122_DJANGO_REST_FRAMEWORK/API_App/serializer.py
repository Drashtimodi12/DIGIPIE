from rest_framework import serializers
from API_App.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['id', 'name']
        # exclude = ['name']