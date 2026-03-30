from django.shortcuts import render, get_object_or_404
from .models import Employee, Department, Role
from django.http import HttpResponse
from django.shortcuts import redirect



# Create your views here.
# Force reload 2
def index(request):
    return render(request,"index.html")

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)

    return render(request,"all_emp.html", context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept = request.POST.get('dept')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')

        emp = Employee(
            first_name=first_name,
            last_name=last_name,
            dept_id=dept,
            salary=salary,
            bonus=bonus,
            role_id=role,
            phone=phone,
            hire_date=hire_date
        )
        emp.save()
        return render(request, "add_emp.html", {'message': 'Employee added successfully!', 'depts': Department.objects.all(), 'roles': Role.objects.all()})
    
    elif request.method == 'GET':
        return render(request, "add_emp.html", {'depts': Department.objects.all(), 'roles': Role.objects.all()})
    else:
        return render(request,"add_emp.html", {'depts': Department.objects.all(), 'roles': Role.objects.all()})

def remove_emp(request, emp_id= 0):   
        if emp_id:
            try:
                emp = Employee.objects.get(id=emp_id)
                emp.delete()
                return redirect('all_emp')  # Redirect to employee list after deletion
            except Employee.DoesNotExist:
                return HttpResponse('Employee not found.')

        emps = Employee.objects.all()
        context = {
            'emps': emps
        }
        print(context)

        return render(request,"remove_emp.html", context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(first_name__icontains=name)
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
        context = {
            'emps': emps 
        }
        return render(request, "all_emp.html", context)
        
    elif request.method == 'GET':
        # If the request method is GET, just render the filter_emp page
        return render(request, "filter_emp.html")

    else:
        return HttpResponse("Invalid request method.")
    



def update_emp(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    if request.method == 'POST':
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.dept_id = request.POST.get('dept')
        employee.salary = request.POST.get('salary')
        employee.bonus = request.POST.get('bonus')
        employee.role_id = request.POST.get('role')
        employee.phone = request.POST.get('phone')
        employee.hire_date = request.POST.get('hire_date')
        employee.save()
        return redirect('all_emp')  # Redirect to the employee list after update
    return render(request, "update_emp.html", {'employee': employee, 'depts': Department.objects.all(), 'roles': Role.objects.all()})

def update_emp_list(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, "update_emp_list.html", context)