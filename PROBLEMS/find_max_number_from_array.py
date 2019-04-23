a=[69,692,54,512,541,30,9]

def mycompare(a,b):
	a,b=str(a),str(b)
	m=int(a+b)
	n=int(b+a)
	if m > n:
		return 1
	elif m < n:
		return -1
	else:
		return 0


for i in reversed(range(len(a))):
	for j in range(i):
		if mycompare(a[j],a[j+1]) == -1 :
			a[j],a[j+1]=a[j+1],a[j] 
			
print(a)