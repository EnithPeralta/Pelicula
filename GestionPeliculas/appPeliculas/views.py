from django.shortcuts import render
from django.db import Error
from django.http import JsonResponse
from appPeliculas.models import Genero,Pelicula
from django.views.decorators.csrf import csrf_protect,csrf_exempt


# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def vistaAgregarGenero(request):
    return render(request,'agregarGenero.html')

@csrf_exempt
def agregarGenero(request):
    try:
        nombre = request.POST['nombre']
        genero = Genero(nombre=nombre)
        genero.save()
        mensaje = "Genero Agregado Correctamente"
    except Exception as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje}
    return JsonResponse(retorno)

def listarPeliculas(request):
    peliculas = Pelicula.objects.all()
    retorno = {"peliculas": (peliculas)}
    return render(request,"listarPelicula.html",retorno)

@csrf_exempt
def agregarPelicula(request):
    try:
        codigo = request.POST['codigo']
        titulo = request.POST['titulo']
        protagonista = request.POST['protagonista']
        duracion = int(request.POST['duracion'])
        resumen = request.POST['resumen']
        foto = request.FILES['fileFoto']
        idGenero = int(request.POST['cbGenero'])
        
        genero = Genero.objects.get(pk=idGenero)
        
        pelicula = Pelicula(
            codigo = codigo,
            titulo = titulo,
            protagonista = protagonista,
            duracion = duracion,
            resumen = resumen,
            foto = foto,
            genero = genero
        )  
        pelicula.save()
        mensaje = "Pelicula Agregada Correctamente"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje":mensaje,'idPelicula':pelicula.id}
    return JsonResponse(retorno)

def vistaAgregarPelicula(request):
    generos = Genero.objects.all()
    retorno = {"generos":generos}
    return render(request,"agregarPelicula.html",retorno)

def eliminarPelicula(request,pelicula_id):
    try:
        pelicula = Pelicula.objects.get(pk=pelicula_id)
        pelicula.delete() 
        mensaje = "Pelicula Eliminada Correctamente"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje":mensaje,'idPelicula':pelicula.id}
    return JsonResponse(retorno)
    