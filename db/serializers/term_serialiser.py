from rest_framework import serializers
from db.models.term import Term 


class TermSerializer(serializers.ModelSerializer):

    class Meta:
        model = Term
        fields = '__all__'
