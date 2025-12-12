from django.shortcuts import render, redirect
from STUDENT_APP.models import *
import os

# Create your views here.

def all_students(request):
    allstu = Student.objects.all()
    return render(request, 'Stu_Form.html', {'student' : allstu})

def register_students(request):

    if request.method == 'POST':
        data = request.POST
        sid = data.get('SID')        
        name = data.get('STU_NAME')
        surname = data.get('STU_SURENAME')
        sbirthdate = data.get('STU_BIRTHDATE')
        email = data.get('EMAIL')
        contact = data.get('CONTACT_NUMBER')
        sphoto = request.FILES.get('STU_PHOTO')

        # ----------------------
        #   UPDATE STUDENT
        # ----------------------
        if sid:
            stu = Student.objects.get(pk=sid)

            stu.STU_NAME=name
            stu.STU_SURENAME=surname
            stu.STU_BIRTHDATE=sbirthdate
            stu.EMAIL=email
            stu.CONTACT_NUMBER=contact

            if sphoto:
                if stu.STU_PHOTO and os.path.isfile(stu.STU_PHOTO.path):
                    os.remove(stu.STU_PHOTO.path)
                stu.STU_PHOTO=sphoto
            stu.save()
            return redirect('all_students')
        
        else: 
            
            # ----------------------
            #   ADD STUDENT
            # ----------------------
            Student.objects.create(
                STU_NAME=name,
                STU_SURENAME=surname,
                STU_BIRTHDATE=sbirthdate,
                EMAIL=email,
                CONTACT_NUMBER=contact,
                STU_PHOTO=sphoto
            )
            return redirect('all_students')

    return render(request, 'Stu_Form.html')


def update_students(request):
    stu_id = request.GET.get('stu_id')
    stu = Student.objects.get(pk=stu_id)
    allstu = Student.objects.all()
    return render(request, 'Stu_Form.html', {'stu' : stu, 'student': allstu})


def delete_students(request):
    stu_id = request.GET.get('stu_id')
    stu = Student.objects.get(pk=stu_id)

    if stu.STU_PHOTO and os.path.isfile(stu.STU_PHOTO.path):
        os.remove(stu.STU_PHOTO.path)
    stu.delete()
    return redirect('all_students')
