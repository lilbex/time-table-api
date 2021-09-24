from rest_framework import serializers
from db.models.classe import Classe 


class ClasseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classe
        fields = '__all__'
