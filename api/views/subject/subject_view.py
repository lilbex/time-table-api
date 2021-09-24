from rest_framework import authentication
from rest_framework import permissions
from lib.response import Response
from rest_framework.views import APIView
from rest_framework import status
from db.serializers.subject_serializer import SubjectSerializer
from db.models.subject import Subject
from db.models.classe import Classe
from db.models.term import Term

class SubjectView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
      """Get all the subjects in a classes using the  class id as the pk"""
      user = request.user
      if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
      serializer = SubjectSerializer(Subject.objects.filter(user=user, classe=pk), many=True).data
      return Response(dict(data=serializer), status=status.HTTP_200_OK)

    def post(self, request, pk):
      user = request.user
      classe = Classe.objects.get(id=pk)
      term =classe.term
      if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
      serializer = SubjectSerializer(data=request.data, context={'request': request})
      if serializer.is_valid():
          serializer.save(user=user, classe=classe, term=term)
          return Response(data=serializer.data, status=status.HTTP_201_CREATED)
      return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)