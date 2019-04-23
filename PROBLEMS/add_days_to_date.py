
def leap_year(yyyy):
	year = int(yyyy)
	month = { '01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
	if(year%4==0 and year%100!=0 or year%400==0):
		month['02']=29
		return month
	else:
		return month

def add_date(days,date):
	dd,mm,yyyy = date.split('-')
	month = leap_year(yyyy)
	dd = int(dd)
	days_sum = dd+days
	if days_sum < month[mm]:
		return '-'.join([str(dd+days).zfill(2),mm,yyyy])
	elif days_sum == month[mm]:
		print("here!")
		return '-'.join([str(month[mm]).zfill(2),mm,yyyy])
	else:
		if mm != '12':
		    days_sum = days_sum - month[mm]
		    mm = str(int(mm)+1).zfill(2)
		    return add_date(days_sum,'-'.join(['00',mm,yyyy]))
		elif mm == '12':
			days_sum = days_sum - month[mm]
			mm = '01'
			yyyy = str(int(yyyy)+1)
			return add_date(days_sum,'-'.join(['00',mm,yyyy]))

print(add_date(30,'01-01-2019'))