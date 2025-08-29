from django.shortcuts import render, get_object_or_404
from .models import Employee
from django.http import HttpResponse
from django.shortcuts import redirect



# Create your views here.
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
        return render(request, "add_emp.html", {'message': 'Employee added successfully!'})
        # Optionally, you can redirect to another page or render a success message
        # For example, you can return a success message or redirect to the all_emp view
        # return HttpResponse("Employee added successfully!")
        # or
        # return render(request, "add_emp.html", {'message': 'Employee added successfully!'})
        # Uncomment the following line if you want to redirect to the all_emp view
        # If you want to redirect to another page after adding an employee
        # return redirect('all_emp')
    
    elif request.method == 'GET':
        return render(request, "add_emp.html")
    else:
        return render(request,"add_emp.html")

def remove_emp(request, emp_id= 0):   
        if emp_id:
            try:
                emp = Employee.objects.get(id=emp_id)
                emp.delete()
                return HttpResponse("Employee Removed Successfully")
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
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.department = request.POST.get('department')
        employee.save()
        return redirect('all_emp')  # Redirect to the employee list after update
    return render(request, "update_emp.html", {'employee': employee})

def update_emp_list(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, "update_emp_list.html", context)