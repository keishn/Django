from django.urls import path
from . import views

urlpatterns = [
    path('', views.picture, name='picture'),
    path('cafes_table/', views.index_tab, name='main'),
    path('cafes/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('cafe/<int:id>/view/', views.cafe_view, name='cafe_view'),
    path('cafe/<int:id>/edit/', views.cafe_edit, name='cafe_edit'),
    path('cafe/<int:id>/delete/', views.cafe_delete, name='cafe_delete'),

]
