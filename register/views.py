from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import RegisterSerializer

from .models import Register
# Create your views here.

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return HttpResponse("This will be a CRM project")

@api_view(['GET','POST'])
def register_list(request, format=None):

    if request.method== 'GET':
        register =Register.objects.all()
        serializer  = RegisterSerializer(register, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        print (request.data)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            print('-------------------------------')
            serializer.save()
            print (serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def register_detail(request,id, format = None):
    try:
        register=Register.objects.get(pk=id)
    except Register.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer=RegisterSerializer(register)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer=RegisterSerializer(register, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        register.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST','GET'])
def login(request):
    if request.method == 'POST':
        Auth= request.data
        email= Auth['Email']
        password = Auth['Password']
        print(email,password)
        DB= Register.objects.filter(Email=email)
        serialdata=RegisterSerializer(DB)
        print(serialdata, serialdata.data)
        return Response('Ok')
        
            
    