from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Autor, Libro, Calificacion
from .serializers import AutorSerializer, LibroSerializer, CalificacionSerializer   


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def autor_listar(request):
    autores = Autor.objects.all()
    serializer = AutorSerializer(autores, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def autor_nuevo(request):
    serializer = AutorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def autor_detalle(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response({'error': 'Autor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = AutorSerializer(autor)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def autor_actualizar(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response({'error': 'Autor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = AutorSerializer(autor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def autor_eliminar(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response({'error': 'Autor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    autor.delete()
    return Response({'mensaje': 'Autor eliminado'}, status=status.HTTP_204_NO_CONTENT)


from .models import Genero
from .serializers import GeneroSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def genero_listar(request):
    generos = Genero.objects.all()
    serializer = GeneroSerializer(generos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def genero_nuevo(request):
    serializer = GeneroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def genero_detalle(request, pk):
    try:
        genero = Genero.objects.get(pk=pk)
    except Genero.DoesNotExist:
        return Response({'error': 'Género no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = GeneroSerializer(genero)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def genero_actualizar(request, pk):
    try:
        genero = Genero.objects.get(pk=pk)
    except Genero.DoesNotExist:
        return Response({'error': 'Género no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = GeneroSerializer(genero, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def genero_eliminar(request, pk):
    try:
        genero = Genero.objects.get(pk=pk)
    except Genero.DoesNotExist:
        return Response({'error': 'Género no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    genero.delete()
    return Response({'mensaje': 'Género eliminado'}, status=status.HTTP_204_NO_CONTENT)

from .models import Libro
from .serializers import LibroSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def libro_listar(request):
    libros = Libro.objects.all()
    serializer = LibroSerializer(libros, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def libro_nuevo(request):
    serializer = LibroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def libro_detalle(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return Response({'error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = LibroSerializer(libro)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def libro_actualizar(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return Response({'error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = LibroSerializer(libro, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def libro_eliminar(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return Response({'error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    libro.delete()
    return Response({'mensaje': 'Libro eliminado'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def libro_listar(request):
    libros = Libro.objects.all()
    serializer = LibroSerializer(libros, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def libro_nuevo(request):
    serializer = LibroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def libro_detalle(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return Response({'error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = LibroSerializer(libro)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def libro_actualizar(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return Response({'error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    serializer = LibroSerializer(libro, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def libro_eliminar(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return Response({'error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    libro.delete()
    return Response({'mensaje': 'Libro eliminado'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def calificacion_listar(request):
    calificaciones = Calificacion.objects.all()
    serializer = CalificacionSerializer(calificaciones, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def calificacion_nueva(request):
    serializer = CalificacionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def calificacion_detalle(request, pk):
    try:
        calificacion = Calificacion.objects.get(pk=pk)
    except Calificacion.DoesNotExist:
        return Response({'error': 'Calificación no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CalificacionSerializer(calificacion)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def calificacion_actualizar(request, pk):
    try:
        calificacion = Calificacion.objects.get(pk=pk)
    except Calificacion.DoesNotExist:
        return Response({'error': 'Calificación no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CalificacionSerializer(calificacion, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def calificacion_eliminar(request, pk):
    try:
        calificacion = Calificacion.objects.get(pk=pk)
    except Calificacion.DoesNotExist:
        return Response({'error': 'Calificación no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    calificacion.delete()
    return Response({'mensaje': 'Calificación eliminada'}, status=status.HTTP_204_NO_CONTENT)