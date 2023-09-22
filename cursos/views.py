from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    """
    API de Cursos
    """
    def get(self, request):
        if request.method == 'GET':
            cursos = Curso.objects.all()
            serializer = CursoSerializer(cursos, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        if request.method == 'POST':
            serializer = CursoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class AvaliacaoAPIView(APIView):
    """
    API de Avaliações
    """
    def get(self, request):
        if request.method == 'GET':
            avaliacoes = Avaliacao.objects.all()
            serializer = AvaliacaoSerializer(avaliacoes, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        if request.method == 'POST':
            serializer = AvaliacaoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)