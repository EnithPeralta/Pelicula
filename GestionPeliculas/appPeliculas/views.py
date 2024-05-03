import os
from django.conf import settings
from django.shortcuts import render,redirect
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
    #return JsonResponse(retorno)
    return render(request,"agregarPelicula.html",retorno)

def vistaAgregarPelicula(request):
    generos = Genero.objects.all()
    retorno = {"generos":generos}
    return render(request,"agregarPelicula.html",retorno)

def consultarPeliculaId(request,id):
    pelicula = Pelicula.objects.get(pk=id)
    generos = Genero.objects.all()
    retorno = {"pelicula":pelicula,"generos":generos}
    return render(request,"actualizarPelicula.html",retorno)

def actualizarPelicula(request):
    try:
        idPelicula = request.POST['idPelicula']
        peliculaActulizar = Pelicula.objects.get(pk=idPelicula)
        peliculaActulizar.codigo = request.POST['codigo']
        peliculaActulizar.titulo = request.POST['titulo']
        peliculaActulizar.protagonista = request.POST['protagonista']
        peliculaActulizar.duracion = int(request.POST['duracion'])
        peliculaActulizar.resumen = request.POST['resumen']
        idGenero = int(request.POST['cbGenero'])

        genero = Genero.objects.get(pk=idGenero)
        peliculaActulizar.genero = genero
        foto = request.FILES.get('fileFotos')
        if (foto):
            os.remove(os.path.join(settings.MEDIA_ROOT + "/" + str(peliculaActulizar.foto)))
            peliculaActulizar.foto = foto
        peliculaActulizar.save()
        mensaje = "Pelicula Actualizada"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje":mensaje}
    return JsonResponse(retorno)

def eliminarPelicula(request,id):
    try:
        peliculaEliminar = Pelicula.objects.get(pk=id)
        peliculaEliminar.delete() 
        mensaje = "Pelicula Eliminada Correctamente"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje":mensaje}
    # return JsonResponse(retorno)
    return redirect('/listarPeliculas')

    