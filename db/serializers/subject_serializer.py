from rest_framework import serializers
from db.models.subject import Subject 


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'
