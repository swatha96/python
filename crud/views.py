from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import EmployeeModel

def show(request):
    allemployees = EmployeeModel.objects.all()
    d={"allemp":allemployees}
    return render(request,"show.html",d)

def emp(request):
    if request.method=="POST":
        #execute when form is submitted
        formobj = EmployeeForm(request.POST)
        formobj.save()
        return redirect("/show/")
    else:
        #execute when <a> for Add New Employee is clicked
        formobj = EmployeeForm()
        d={"empform":formobj}
        return render(request,"addnew.html",d)

def remove(request,empid):
    emp = EmployeeModel.objects.get(id=empid)
    emp.delete()
    return redirect("/show/")

def edit(request,empid):
    emp = EmployeeModel.objects.get(id=empid)
    return render(request,"edit.html",{"form":emp})

def update(request,empid):
    emp = EmployeeModel.objects.get(id=empid)
    formobj = EmployeeForm(request.POST,instance=emp)
    if formobj.is_valid():
        formobj.save()
        return redirect("/show/")
    else:
        return render(request,"edit.html",{"form":emp})




  

























