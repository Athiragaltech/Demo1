
from . models import employee
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse



def index(request):
    return render(request,'index.html')
def addnew(request):
    return render(request,'addnew.html') 
def view(request):
    data={
        'emp' :employee.objects.all()
         }
    return render(request,'view.html',data)
def edit(request):
    data={
        'emp' :employee.objects.all()
         }
    return render(request,'edit.html',data)    


def insert(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        place=request.POST.get('place')
        desig=request.POST.get('desig')
        country=request.POST.get('country')
        mobile=request.POST.get('mobile')
        query=employee(name=name,age=age,place=place,desig=desig,country=country,mobile=mobile)
        query.save()
        return HttpResponse(f'<script>alert("File Saved successfully!"); window.location.href = "/";</script>')
    return render(request,'index.html') 


def delete(request,id):
    dlt=employee.objects.get(id=id)
    dlt.delete()
    return HttpResponse(f'<script>alert("File Deleted successfully!"); window.location.href = "/";</script>') 
    return render(request,'index.html')   

def edit2(request,id):
    data ={
        'emp' :employee.objects.get(id=id)

    }
    return render(request,'updation.html',data)    
def update(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        place=request.POST.get('place')
        desig=request.POST.get('desig')
        country=request.POST.get('country')
        mobile=request.POST.get('mobile')
       
        edit=employee.objects.get(id=id)
        edit.name=name
        edit.age=age
        edit.place=place
        edit.desig=desig
        edit.country=country
        edit.mobile=mobile
      
        edit.save()
        return HttpResponse(f'<script>alert("File Updated successfully!"); window.location.href = "/";</script>')
        return render(request,'index.html') 