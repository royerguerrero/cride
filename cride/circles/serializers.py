"""Circle serializers"""

# Django REST Framerwork
from rest_framework import serializers

# Models
from cride.circles.models import Circle


class CircleSerializer(serializers.Serializer):
    """Circle serializer"""

    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_taken = serializers.IntegerField()
    rides_offerted = serializers.IntegerField()
    members_limit = serializers.IntegerField()


class CreateCircleSerializer(serializers.Serializer):
    """Create circle serialzers"""

    name = serializers.CharField(max_length=140)
    slug_name = serializers.SlugField(max_length=140)
    about = serializers.CharField(max_length=255, required=False)

    def create(self, validate_data):
        """Create circle"""
        return Circle(**validate_data)
