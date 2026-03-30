#!/usr/bin/env python
import os
import django
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'office_emp_proj.settings')

django.setup()

from emp_app.models import Department, Role, Employee

def populate_sample_data():
    # Create departments
    dept1, created = Department.objects.get_or_create(name='Engineering', location='New York')
    dept2, created = Department.objects.get_or_create(name='Marketing', location='San Francisco')
    dept3, created = Department.objects.get_or_create(name='HR', location='Chicago')

    # Create roles
    role1, created = Role.objects.get_or_create(name='Software Engineer')
    role2, created = Role.objects.get_or_create(name='Marketing Manager')
    role3, created = Role.objects.get_or_create(name='HR Specialist')
    role4, created = Role.objects.get_or_create(name='Data Analyst')

    # Create employees
    emp1, created = Employee.objects.get_or_create(
        first_name='John',
        last_name='Doe',
        defaults={
            'dept': dept1,
            'role': role1,
            'salary': 75000,
            'bonus': 5000,
            'phone': 1234567890,
            'hire_date': '2023-01-15'
        }
    )

    emp2, created = Employee.objects.get_or_create(
        first_name='Jane',
        last_name='Smith',
        defaults={
            'dept': dept2,
            'role': role2,
            'salary': 65000,
            'bonus': 4000,
            'phone': 9876543210,
            'hire_date': '2023-03-20'
        }
    )

    emp3, created = Employee.objects.get_or_create(
        first_name='Bob',
        last_name='Johnson',
        defaults={
            'dept': dept3,
            'role': role3,
            'salary': 55000,
            'bonus': 3000,
            'phone': 5551234567,
            'hire_date': '2023-05-10'
        }
    )

    print("Sample data populated successfully!")

if __name__ == '__main__':
    populate_sample_data()