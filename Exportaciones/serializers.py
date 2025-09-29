from rest_framework import serializers
from .models import Embarque

class EmbarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embarque
        fields = '__all__'