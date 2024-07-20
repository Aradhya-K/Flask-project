from flask import Blueprint, jsonify, request
from .model import Employee, db
from .schemas import EmployeeSchema

#create blueprint
main = Blueprint('main', __name__)

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

@main.route('/')
def index():
    return jsonify({"message":"Welcome to the Employee Management System!"})

@main.route('/employees', methods = ['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify({"employees": [employee.to_dict() for employee in employees]})   #placeholder for employee list

#create an employee
@main.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    new_employee = Employee(
        name= data['name'],
        position= data['position'],
        department = data['department'],
        salary = data['salary']
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({"message": "employee created successfully"}), 201

#updating details of existing emp

@main.route('/employee/<int:id', methods = ['PUT'])
def update_employee(id):
    data = request.get_json()
    employee= Employee.query.get_or_404(id)
    employee.name = data['name']
    employee.position = data['position']
    employee.department = data['department']
    employee.salary = data['salary']
    db.session.commit()
    return jsonify({"message": "employee updated successfully!"})

#route for deleting an emp
@main.route('/employee/<int:id>', methods = ['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message":"employee deleted successfully!"})