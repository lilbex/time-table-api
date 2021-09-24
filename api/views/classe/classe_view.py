from rest_framework import authentication
from rest_framework import permissions
from lib.response import Response
from rest_framework.views import APIView
from rest_framework import status
from db.serializers.classe_serializer import ClasseSerializer
from db.models.classe import Classe
from db.models.term import Term

class ClasseView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
      """Get all the classes relating to a term using the term_id as pk"""
      user = request.user
      if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
      serializer = ClasseSerializer(Classe.objects.filter(user=user, term=pk), many=True).data
      return Response(dict(data=serializer), status=status.HTTP_200_OK)

    def post(self, request, pk):
      user = request.user
      term = Term.objects.get(id=pk)
      print(user)
      if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
      serializer = ClasseSerializer(data=request.data, context={'request': request})
      if serializer.is_valid():
          serializer.save(user=user, term=term)
          return Response(data=serializer.data, status=status.HTTP_201_CREATED)
      return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)