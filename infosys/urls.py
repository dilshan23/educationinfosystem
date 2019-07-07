from django.urls import path
from . import views
#from .views import login

urlpatterns = [
   path("schools/",views.schools,name ='schools'),
]