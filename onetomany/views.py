from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.
def create(request):
  # repo1 = Reporter(first_name="Rafael", last_name="Zarate", email="rrzarate4@gmail.com")
  # repo1.save()

  # art1 = Article(headline="Django basico", pub_date=date(2024,4,3), reporter=repo1)
  # art2 = Article(headline="Django intermedio", pub_date=date(2024,5,3), reporter=repo1)
  # art3 = Article(headline="Django avanzado", pub_date=date(2024,5,3), reporter=repo1)

  # art1.save()
  # art2.save()
  # art3.save()

  return HttpResponse("Uno a muchos")

def  consultar (request, id):
  r = Reporter.objects.get(id=id) #trae el registro que coincida con la llave primaria

  print (r)
  return HttpResponse (f"Primer Nombre: {r.first_name}, Apellido: {r.last_name}, email: {r.email}")

def  modificar(request,first_name,last_name,email,id):
    
  r = Reporter.objects.get(id=id)
  r.first_name = first_name
  r.last_name = last_name
  r.email = email
  r.save()
  

  return HttpResponse ('Se actualizaron los Datos')

def eliminar(request,id):
  r = Reporter.objects.get(id=id)
  r.delete()
  return HttpResponse ("Registro Eliminado")


  # repo1=Reporter.objects.get(id=1)
  # query=repo1.article_set.all()
  # return render (request, 'index.html',{
  #   'repo1':repo1,
  #   'query':query
  # }) 
  
  

