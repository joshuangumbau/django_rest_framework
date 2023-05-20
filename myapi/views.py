from django.shortcuts import render

# Create your views here.
from .serializers import heroSerializers
from .models import hero

class heroViewSet(viewsets.ModelViewSet):
    queryset = hero.objects.all().order_by('name')
    seializer_class = heroSerializer
    
    
