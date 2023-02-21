from django.shortcuts import render

# usando viewset para retornar todos os objetos, sem necessidade de codificar os metodos
from rest_framework import viewsets

# permitir outros domains acessarem nossos metodos da api
from django.views.decorators.csrf import csrf_exempt

# parse dados recebidos em dados para o data model
from rest_framework.parsers import JSONParser

from Store.serializer import DepartmentSerializer, EmployeeSerializer
from Store.models import Departments, Employees
from django.http.response import JsonResponse

# usado pra upload o file
from django.core.files.storage import default_storage


# metodo receberá um id opcional que será usado para deletar
# um registro baseado no id

@csrf_exempt
def dapartmentApi(request,id=0):

    # retorna os dados em formato json
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        
        # tentando converter p json, se houve erro não há problema
        return JsonResponse(departments_serializer.data, safe=False)
    
    elif request.method == 'POST':
        departments_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Department Salvo com Sucesso !!", safe=False)
        return JsonResponse("Falha ao salvar Department!", safe=False)

    elif request.method == 'PUT':
        
        # convertendo p json
        departments_data = JSONParser().parse(request)
        
        # pegando departamento existente no banco
        departments = Departments.objects.get(IdDepartment=departments_data['IdDepartment'])
        
        # salvando novos valores usando serializer
        departments_serializer = DepartmentSerializer(departments,data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Department Alterado com Sucesso !", safe=False)
        return JsonResponse("Falha ao Alterar Department!", safe=False)

    elif request.method == 'DELETE':
        departments = Departments.objects.get(IdDepartment=id)
        departments.delete()
        return JsonResponse("Department Deletado com Sucesso !", safe=False)


@csrf_exempt
def employeesApi(request,id=0):

    # retorna os dados em formato json
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        
        # tentando converter p json, se houve erro não há problema
        return JsonResponse(employees_serializer.data, safe=False)
    
    elif request.method == 'POST':
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Employee Salvo com Sucesso !!", safe=False)
        #print(employees_serializer.errors)
        return JsonResponse("Falha ao salvar Employee ! ", safe=False)

    elif request.method == 'PUT':
        
        # convertendo p json
        employees_data = JSONParser().parse(request)
        
        # pegando departamento existente no banco
        employees = Employees.objects.get(IdEmployee=employees_data['IdEmployee'])
        
        # salvando novos valores usando serializer
        employees_serializer = EmployeeSerializer(employees,data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Employee Alterado com Sucesso !", safe=False)
        return JsonResponse("Falha ao Alterar Employee!", safe=False)

    elif request.method == 'DELETE':
        employees = Employees.objects.get(IdEmployee=id)
        employees.delete()
        return JsonResponse("Employee Deletado com Sucesso !", safe=False)


# metodo para salvar imagens

@csrf_exempt
def saveFile(request):
    file = request.FILES["myFile"]
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name, safe=False)



"""
# Usando viewsets

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
"""