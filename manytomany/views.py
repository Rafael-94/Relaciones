from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article
# Create your views here.

def create(request):

  p1 = Publication(title="Titulo1")
  p2 = Publication(title="Titulo2")
  p3 = Publication(title="Titulo3")
  p4 = Publication(title="Titulo4")
  p5 = Publication(title="Titulo5")
  p6 = Publication(title="Titulo6")
  p7 = Publication(title="Titulo7")
  p8 = Publication(title="Titulo8")
  
  p1.save()
  p2.save()
  p3.save()
  p4.save()
  p5.save()
  p6.save()
  p7.save()
  p8.save()

  a1 = Article(headline="Articulo1")
  a2 = Article(headline="Articulo2")
  a3 = Article(headline="Articulo3")

  a1.save()
  a2.save()
  a3.save()

#relacionamos los modelos
  a1.publications.add(p1)
  a1.publications.add(p2)
  a1.publications.add(p3)

  a2.publications.add(p4)
  a2.publications.add(p5)
  a2.publications.add(p6)

  a3.publications.add(p7)
  a3.publications.add(p8)

  return HttpResponse("Datos creados correctamente")

def  consultar (request, id):
  r = Publication.objects.get(id=id) #trae el registro que coincida con la llave primaria

  print (r)
  return HttpResponse (f"Id: {r.id},Titulo: {r.title}")  

def  modificar(request,title,id):
    
  r = Publication.objects.get(id=id)
  r.title = title
  r.save()
  

  return HttpResponse ('Se actualizaron los Datos')

def eliminar(request,id):
  r = Publication.objects.get(id=id)
  r.delete()
  return HttpResponse ("Registro Eliminado")

 