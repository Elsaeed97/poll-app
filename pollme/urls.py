from django.urls import path 
from . import views 
urlpatterns = [
	path('', views.index, name='index'),
	path('create/', views.create, name='create'),
	path('<int:id>/vote/', views.vote, name='vote'),
	path('<int:id>/results/', views.results, name='results'),
]
