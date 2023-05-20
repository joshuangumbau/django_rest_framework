from rest_framework import serializers

from .models import hero

class heroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hero
        fields = ('name' , 'alias')
        
        