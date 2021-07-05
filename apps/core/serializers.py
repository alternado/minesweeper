from rest_framework import serializers

from apps.core.models import Username


class UsernameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Username
        fields = '__all__'
