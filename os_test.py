import os
from os import path
p=os.getcwd()

#for i in os.listdir(p):
#    if path.isdir(path.join(p,i)):
#        print(i)

#print("====>",path.dirname(p))
#print("====>",path.split(p))

#print(dir(path))


#for dirpath,subdir,files in os.walk(p):
#    print("Current path:",dirpath)
#    print("Sub directories:",subdir)
#    print("filenames:",files)

print(os.environ.get('HOME'))