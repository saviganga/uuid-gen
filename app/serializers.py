from rest_framework import serializers
from app.models import UUIDModel

class UUIDModelSerializer(serializers.ModelSerializer):
    
    """ Returns JSON output for UUIDModel model """

    class Meta:
        model = UUIDModel
        fields = ['timestamp', 'uid']
    