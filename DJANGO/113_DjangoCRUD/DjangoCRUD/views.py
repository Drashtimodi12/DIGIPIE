from django.shortcuts import render, redirect
from DjangoCRUD.models import *
import os

# Create your views here.

# -----------------------------------------
# SHOW ALL EMPLOYEES
# -----------------------------------------
def Emp_all(request):
    allEmployee = Employee.objects.all()
    return render(request, 'index.html', {"allEmp": allEmployee, "emp": None})


# -----------------------------------------
# CREATE + UPDATE EMPLOYEE
# -----------------------------------------
def Emp_Register(request):

    if request.method == "POST":
        data = request.POST

        empid = data.get("id")         # Hidden input ID from form
        name = data.get("EMP_NAME")
        email = data.get("EMAIL")
        phone = data.get("PHONE_NUMBER")
        age = data.get("AGE")
        image_file = request.FILES.get("EMP_PHOTO")

    
        # -----------------------------------------
        # IF ID EXISTS -> UPDATE EMPLOYEE
        # -----------------------------------------
        if empid:
            emp = Employee.objects.get(pk=empid)
            emp.EMP_NAME = name
            emp.EMAIL = email
            emp.PHONE_NUMBER = phone
            emp.AGE = age

            # if new image uploaded, remove old image and set new one
            if image_file:
                if emp.EMP_PHOTO and os.path.exists(emp.EMP_PHOTO.path):
                    try:
                        os.remove(emp.EMP_PHOTO.path)
                    except Exception as e:
                        print(e)
                emp.EMP_PHOTO = image_file

            emp.save()
            return redirect("emp_all")


        # -----------------------------------------
        # ELSE -> ADD NEW EMPLOYEE
        # -----------------------------------------
        else:
            # 1. trick
            # emp = Employee.objects.create(EMP_NAME=name, EMAIL=email, PHONE_NUMBER=phone, AGE=age, EMP_PHOTO=image_file)
            # if emp:
            #     return render(request,'index.html',{"msg":"Registration successful"})

            # 2 trick
            emp = Employee.objects.create(
                EMP_NAME=name,
                EMAIL=email, 
                PHONE_NUMBER=phone, 
                AGE=age,
                EMP_PHOTO=image_file
            )
            return redirect("emp_all")
    # if GET or anything else, redirect to list
    return redirect("emp_all")


        
        

# -----------------------------------------
# LOAD EMPLOYEE DATA FOR EDIT
# -----------------------------------------
def Emp_update(request):
    emp_id = request.GET.get('emp_id')
    employee = Employee.objects.get(id=emp_id)
    allEmployee = Employee.objects.all()

    return render(request, 'index.html', {
        "emp": employee,
        "allEmp": allEmployee
    })




# -----------------------------------------
# DELETE EMPLOYEE
# -----------------------------------------
def Emp_delete(request):
    emp_id = request.GET.get('emp_id')
    emp = Employee.objects.get(id = emp_id)

    # delete image from folder
    if emp.EMP_PHOTO and os.path.exists(emp.EMP_PHOTO.path):
        try:
            os.remove(emp.EMP_PHOTO.path)
        except Exception as e:
            print(e)

    emp.delete()

    return redirect("emp_all")