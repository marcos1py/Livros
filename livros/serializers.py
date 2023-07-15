from rest_framework import serializers



class LivrosSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    titulo = serializers.CharField(max_length=100)
    descricao1 = serializers.CharField(max_length=200)