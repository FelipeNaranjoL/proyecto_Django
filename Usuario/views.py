from email.mime import message
from pyexpat.errors import messages

from django.shortcuts import render, redirect, redirect,get_object_or_404
from .models import Colaborador
from .forms import agregarColaborador
# Create your views here.
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import colaboradorSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

class colaboradorViewset(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = colaboradorSerializer



def homeUsuario (request):
    return render(request,'Usuario/base.html')

#crud
def listarUsuario (request):
    usuarios = Colaborador.objects.all()
    data = {'users' : usuarios}
    return render (request, 'Usuario/listarUsuario.html', data)

def modificarUsuario (request, id):
    usuarios = get_object_or_404(Colaborador, id=id)
    data = {'form': agregarColaborador(instance=usuarios)}
    
    if request.method == 'POST':
        formulario = agregarColaborador(data=request.POST, instance=usuarios, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listaruser")
        data["form"] = formulario
    return render (request, 'Usuario/modificar.html',data)

def agregarUsuario (request):
    data = {'form': agregarColaborador()}
    
    if request.method == 'POST':
        formulario = agregarColaborador(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Colaborador agregado"
        else:
            data["form"] = formulario
    
    return render (request, 'Usuario/agregarUsuario.html',data)

def eliminarUsuario (request, id):
    usuarios = get_object_or_404(Colaborador, id=id)
    usuarios.delete()
    return redirect(to="listaruser")

#api


@api_view(['GET', 'POST'])
def carrera_collection(request):
    if request.method == 'GET':
        alimentos = Colaborador.objects.all()
        serializer = colaboradorSerializer(alimentos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = colaboradorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def carrera_element(request, pk):
    alimentos = get_object_or_404(Colaborador, id=pk)
 
    if request.method == 'GET':
        serializer = colaboradorSerializer(alimentos)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        alimentos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        carrera_new = JSONParser().parse(request) 
        serializer = colaboradorSerializer(alimentos, data=carrera_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)