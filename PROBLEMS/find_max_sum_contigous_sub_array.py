a=[-2,-3,4,-1,-2,1,5,-3]

def find_max_sum_contigious_array(a):
	max=a[0]
	sum=a[0]
	for i in range(1,len(a)):
		sum=sum+a[i]
		if sum < 0 : sum =0
		if sum > max : max = sum
	return max

print(find_max_sum_contigious_array(a))


