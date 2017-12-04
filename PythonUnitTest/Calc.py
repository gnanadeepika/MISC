import logging

logging.basicConfig(filename='Calc.log',level=logging.DEBUG)

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        raise ValueError('Cannot divide by zero')
    return x/y

x=10
y=5
result=add(x,y)
logging.debug('Method add : {} + {} = {}'.format(x,y,result))
result=sub(x,y)
logging.debug('Method sub : {} - {} = {}'.format(x,y,result))
result=mul(x,y)
logging.debug('Method sub : {} * {} = {}'.format(x,y,result))
result=div(x,y)
logging.debug('Method sub : {} / {} = {}'.format(x,y,result))
