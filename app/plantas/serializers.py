
from plantas.models import Evidencia, Planta
from productos.serializers import ProductoSerializer
from rest_framework import serializers

class EvidenciaSerializer(serializers.ModelSerializer):
    evidencia_text= serializers.SerializerMethodField()
    class Meta:
        model = Evidencia
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1
    def get_evidencia_text(self, obj):
        return obj.evidencia_texto()


class PlantaSerializer(serializers.ModelSerializer):
    evidencias=EvidenciaSerializer(many=True, read_only=True)
    productos=ProductoSerializer(many=True, read_only=True)
    class Meta:
        model = Planta
        fields = '__all__'
        read_only_fields = ['id','evidencias']
        depth = 2

class PlantaIndicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields = ['id', 'nombre', 'especie', 'imagen']
        read_only_fields = ['id','nombre','especie','imagen']
        

