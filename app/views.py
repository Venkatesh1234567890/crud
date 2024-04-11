from django.shortcuts import redirect, render
from .models import Student
from django.contrib import messages
# Create your views here.
def index(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "app/index.html", context)

def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        messages.info(request, "Data Inserted Successfully")
        return redirect('/')  # Redirect to the index page after successful insertion
    return render(request, "app/about.html")

def updatedata(request, id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']

        edit = Student.objects.get(id=id)
        edit.name=name
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request, "Data updated Successfully")
        return redirect('/')

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "app/edit.html", context)

def deletedata(request,id):
    
    d = Student.objects.get(id=id)
    d.delete()
    messages.error(request, "Data deleted Successfully")
    return redirect('/')

def about(request):
    return render(request, "app/about.html")
