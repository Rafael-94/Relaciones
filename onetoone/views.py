from django.shortcuts import render
from django.http import HttpResponse
from.models import Place, Restaurant

# Create your views here.

def create(request):
  #place = Place(name= "centro", adress="calle 45 No 20 -13")
  #place.save()

  #place = Place.objects.get(id=1)

  #restaurant = Restaurant(place=place, employes=25)
  #restaurant.save()

  restaurante = Restaurant.objects.get(place_id=3)
  print(restaurante.place.adress)

  return HttpResponse("Datos creados correctamente")

def  consultar (request, id):
  r = Place.objects.get(id=id) #trae el registro que coincida con la llave primaria

  print (r)
  return HttpResponse (f"Nombre: {r.name}, Direccion: {r.adress}")  

def  modificar(request,name,adress,id):
    
  r = Place.objects.get(id=id)
  r.name = name
  r.adress = adress
  r.save()
  

  return HttpResponse ('Se actualizaron los Datos')

def eliminar(request,id):
  r = Place.objects.get(id=id)
  r.delete()
  return HttpResponse ("Registro Eliminado")