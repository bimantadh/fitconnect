from rest_framework import serializers
from rest_framework import validators

from gym.models import Gym


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'




