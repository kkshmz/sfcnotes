class Person(object):
  """
    Person's class
  """

  def setname(self, fullname):
    self.fullname = fullname

  def getname(self):
    return self.fullname

  def setdob(self, dob):
    self.dob = dob

  def getdob(self):
    return self.dob

  def setsex(self, sex):
    if sex == "Male" or sex == "Female":
      self.sex = sex

  def getsex(self):
    return self.sex

  def __str__(self):
    return "Name: %s, %s, DOB: %s"%(self.fullname, self.sex, self.dob)


class Employee(Person):
  """
    Employee's class.
  """
  employee_id_pool = 0
  #
  created_employees  = {}

  def __init__(self, fullname, job='Engineer'):
    self.fullname = fullname
    self.job = job
    Employee.employee_id_pool += 1
    self.employee_id = Employee.employee_id_pool
 #
    if job not in Employee.created_employees:
      Employee.created_employees[job] = 1
    else:
      Employee.created_employees[job] += 1
      
#
  @staticmethod
  def created_jobs():
    return Employee.created_employees    
  
  def setjob(self, job):
    self.job = job

  def getjob(self):
    return self.job

  def setsalary(self, salary):
    self.salary = salary

  def getsalary(self):
    return self.salary

  def giveraise(self, percent = 0.1):
    self.salary = int(self.salary * (1 + percent))

  def __str__(self):
    return 'Name: %s, %s ID: %d, Salary: %d'%(self.fullname, self.sex, self.employee_id, self.salary)

class Manager(Employee):
  def __init__(self, fullname):
    Employee.__init__(self, fullname, 'Manager')

  def giveraise(self, percent = 0.1, bonus = 0.1):
    Employee.giveraise(self, percent + bonus)


if __name__ == "__main__":
  myemployee = Employee('SFC Taro')
  myemployee.setsalary(2000)
  myemployee.setsex('Male')
  myemployee.setdob('1990/5/1')
  print myemployee

  mymanager = Manager('SFC Hanako')
  mymanager.setsex('Female')
  mymanager.setdob('1990/5/1')
  mymanager.setsalary(5000)
  mymanager.giveraise(0.2)
  print mymanager, mymanager.getsalary()
  
  
  print Employee.created_jobs()
#  print Employee.created_employees 
#  print Employee.employee_id_pool
