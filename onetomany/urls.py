from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('consultar/<int:id>',views.consultar,name="consultar"),
    path('modificar/<int:id>/<str:first_name>/<str:last_name>/<str:email>/',views.modificar,name="modificar"),
    path('eliminar/<int:id>',views.eliminar,name="eliminar")
]