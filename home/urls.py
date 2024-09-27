from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
               path('',views.index,name='index'),
               path('addnew/',views.addnew,name='addnew'),#for loading this apge
               path('view/',views.view,name='view'),#this too
               path('insert/',views.insert),
               path('edit/', views.edit, name='edit'), #for loading that page
               path('edit/delete/<int:id>/', views.delete, name='delete'),#for deletion
               path('edit/edit2/<int:id>/', views.edit2, name='edit2'),
               path('update/<int:id>/', views.update, name='update'),
             



]
   
