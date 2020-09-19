from rest_framework import serializers
from .models import Property,Profile



class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property


        fields = '__all__'

    def create(self,validated_data):
        return Property.objects.create(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields=['user','image','property','bio','contacts'] 

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.property = validated_data.get('property', instance.property)
        instance.save()
        return instance