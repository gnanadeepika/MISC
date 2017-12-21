import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler=logging.FileHandler('employee.log')
logger.addHandler(file_handler)
file_handler.setFormatter(formatter)


class Employee:
    bonus=1.10
    count_emp=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        Employee.count_emp=Employee.count_emp+1
        logger.debug("Employee create :: Employee({},{},{})".format(self.first,self.last,self.pay))

    @property
    def email(self):
        return '{0}.{1}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{0} {1}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        self.first,self.last=name.split()

    @fullname.deleter
    def fullname(self):
        self.first=None
        self.last=None


    def raise_pay(self):
        self.pay=int(int(self.pay) * self.bonus)



Employee('gnanadeepika','nadimpalli',750000)
Employee('harshavikram','kesavareddy',900000)
