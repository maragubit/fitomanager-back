from .models import Indicacion 
from rest_framework import serializers  
from plantas.serializers import PlantaSerializer
from .models import Departamento
from productos.serializers import ProductoSerializer

class IndicacionesSerializer(serializers.ModelSerializer):
    plantas=PlantaSerializer(many=True, read_only=True)
    productos=serializers.SerializerMethodField()
    class Meta:
        model = Indicacion
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1  # Profundidad para incluir relaciones foráneas

    def get_productos(self, obj):
        return ProductoSerializer(obj.get_products(), many=True, context={'request': self.context['request']}).data
        
        
class DepartamentoIndicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
        read_only_fields = ['id']