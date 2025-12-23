from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from API_App.models import *
from API_App.serializer import *

# Create your views here.

@api_view(['GET'])
def view(request):
    allStu = Student.objects.all()
    ser = StudentSerializer(allStu, many = True)
    return Response({"students":ser.data})
    # return Response({"message":"Get api calling..."})

@api_view(['POST'])
def add(request):
    # print(request.data)
    # return Response({"message":"POST API calling..."})
    try:
        ser = StudentSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"errors": ser.error_messages, "message":"Something went wrong..."})
        else:
            ser.save()
            return Response({"data":ser.data, "message":"Data inserted successfully..."})
    except Exception as e:
        return Response({"error":e, "message":"Something went wrong..."})

@api_view(['PUT'])
def update(request, id):
    # return Response({"message":"PUT API calling..."})
    try:
        stu = Student.objects.get(pk=id)
        ser = StudentSerializer(stu, request.data)
        if not ser.is_valid():
            return Response({"errors": ser.error_messages, "message":"Something went wrong..."})
        else:
            ser.save()
            return Response({"data":ser.data, "message":"Data updated successfully..."})
    except Exception as e:
        return Response({"error":e, "message":"Something went wrong..."})

@api_view(['PUT'])
def pupdate(request, id):
    # return Response({"message":"PATCH API calling..."})
    try:
        stu = Student.objects.get(pk=id)
        ser = StudentSerializer(stu, request.data, partial = True)
        if not ser.is_valid():
            return Response({"errors": ser.error_messages, "message":"Something went wrong..."})
        else:
            ser.save()
            return Response({"data":ser.data, "message":"Data updated successfully..."})
    except Exception as e:
        return Response({"error":e, "message":"Something went wrong..."})


@api_view(['DELETE'])
def delete(request, id):
    # return Response({"message":"DELETE API calling..."})
    try:
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"success":True})
    except Exception as e:
        return Response({"error":e, "message":"Something went wrong..."})
