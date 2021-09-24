from rest_framework import authentication
from rest_framework import permissions
from lib.response import Response
from rest_framework.views import APIView
from rest_framework import status
from db.serializers.term_serialiser import TermSerializer
from db.models.term import Term
# from rest_framework.response import Response

class TermView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
      user = request.user
      if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
      serializer = TermSerializer(Term.objects.filter(user=user), many=True).data
      return Response(dict(data=serializer), status=status.HTTP_200_OK)

    def post(self, request):
      user = request.user
      print(user)
      if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
      serializer = TermSerializer(data=request.data, context={'request': request})
      if serializer.is_valid():
          serializer.save(user=user)
          return Response(data=serializer.data, status=status.HTTP_201_CREATED)
      return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)