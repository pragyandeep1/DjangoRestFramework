from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from myapp.models import Employee
from rest_framework.response import Response
from myapp.serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

class EmployeeListAPIView(ListAPIView):
    qs = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
'''
class EmployeeListAPIView(APIView):
    def get(self,request):
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs,many=True)
        return Response(serializer.data)
'''





