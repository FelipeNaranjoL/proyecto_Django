from django.shortcuts import render, redirect,get_object_or_404
from .models import alimento, agregar
from .forms import agregarForms
# Create your views here.

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
