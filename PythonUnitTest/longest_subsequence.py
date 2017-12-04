import logging

logging.basicConfig(filename="long_seq.log",level=logging.DEBUG)

arr=[10,21,9,30,21,50,41,60,80]

lis=[1]*len(arr)

for i in range (1 , len(arr)):
        for j in range(0 , i):
            logging.debug("Inputs :: {} {}".format(i,arr[i]))
            logging.debug("list : {}".format(lis))
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
print(max(lis))