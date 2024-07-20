#import the SQLAlchemy instance
from app import db

#define an Employee Model
class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.string(100),nullable=False)
    position = db.Column(db.string(100),nullable=False)
    department = db.Column(db.string(100),nullable=False)
    salary = db.Column(db.Float, nullable= False)

    def to_dict(self):
       return {
          'id': self.id,
          'name': self.name,
          'position': self.position,
          'department': self.department,
          'salary': self.salary
        }


