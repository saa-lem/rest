from rest_framework import serializers
from .models import Property,Profile



class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property


        fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields=['user','image','property','bio','contacts'] 