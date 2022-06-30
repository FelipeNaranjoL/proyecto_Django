from email.mime import message
from pyexpat.errors import messages
from django.forms import PasswordInput
from django.shortcuts import render, redirect,get_object_or_404
from .models import alimento, agregar
from .forms import agregarForms, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .serializers import AgregarSerializer
# Create your views here.
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AgregarSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
#-------------------------------



class AgregarViewset(viewsets.ModelViewSet):
    queryset = agregar.objects.all()
    serializer_class = AgregarSerializer

#aqui creas la funcion que busca por nombre el archivo al donde quieres llevar a la persona
def home(request):
    return render(request,'pag_perros/home.html')

def alimentos(request):
    return render(request,'pag_perros/alimentos.html')

def formulario(request):
    return render(request,'pag_perros/formulario.html')

def no_producto(request):
    return render(request,'pag_perros/no_producto.html')

def pelis(request):
    return render(request,'pag_perros/pelis.html')

def listar(request):
    alimentos = agregar.objects.all()
    data = {'alimentos' : alimentos}
    return render (request, 'pag_perros/listar.html', data) 

def agregarform(request):
    data = {'form': agregarForms()}
    
    if request.method == 'POST':
        formulario = agregarForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto agregado"
        else:
            data["form"] = formulario
    
    return render (request, 'pag_perros/agregar_producto.html',data)

def modificar_producto(request, id):
    alimento = get_object_or_404(agregar, id=id)
    data = {'form': agregarForms(instance=alimento)}
    
    if request.method == 'POST':
        formulario = agregarForms(data=request.POST, instance=alimento, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar")
        data["form"] = formulario
    return render (request, 'pag_perros/modificar.html',data)

def eliminar(request, id):
    alimento = get_object_or_404(agregar, id=id)
    alimento.delete()
    return redirect(to="listar")

def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],Password= formulario.cleaned_data["password1"])
            login(request,user)
            return redirect(to=home)
        data["form"] = formulario
    
    
    return render (request, 'registration/registro.html',data)


@api_view(['GET', 'POST'])
def carrera_collection(request):
    if request.method == 'GET':
        alimentos = agregar.objects.all()
        serializer = AgregarSerializer(alimentos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AgregarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def carrera_element(request, pk):
    alimentos = get_object_or_404(agregar, id=pk)
 
    if request.method == 'GET':
        serializer = AgregarSerializer(alimentos)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        alimentos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        carrera_new = JSONParser().parse(request) 
        serializer = AgregarSerializer(alimentos, data=carrera_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
