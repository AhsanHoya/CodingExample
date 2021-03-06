from math import pi

def day_of_week(d):
	'''
	given an integer, return the string of the 
	full day (first letter capitalized)

	d = int, day of week to return
	'''
	aDict = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
	return aDict[d]
	# aList = ["Sunday", "Monday", "Tuesday", "Wednesday"]
	# return aList[d]


def median_of_list(ls):
	'''
	return the median of this list
	ls = list provided
	'''
	count = len(ls)
	if count % 2 == 1:
		return ls[(count//2)]
	else:
		return (ls[(count//2)] + ls[(count//2) - 1])/ 2

def build_str(i):
	'''
	build and return a string based on the integer provided:
		even: 'a' / odd: 'b'
		divisible by 3: 'c' / not: 'd'
		greater than 7: 'e' / not: 'f'
		divisible by 10: 'g' / not: 'h'

	ex. 55 -> 'bdeh'
	i = integer provided
	'''
	raise NotImplementedError

def formula(x):
	'''
	return y if y = 2x + 1/2(x^2) - 3
	'''
	return 2*x + 0.5*(x**2) - 3

def reverse(s):
	'''
	return the reverse of the string or list provided
	'''
	return s[::-1]

def get_evens(ls):
	'''
	return list of all even numbers in list ls
	'''
	aList = []
	for i in ls:
		if i%2 == 0:
			aList.append(i)
	return aList
	

def area(diameter):
	'''
	given the diameter of a circle, return the area
	'''
	r = diameter/2
	return pi*r**2

def get_last_angle(a,b):
	'''
	given 2 angles of a triangle, return the third angle 
	'''
	return 180 - (a + b)

def binary_search(ls, val):
	'''
	use a binary search to find val in list ls
	return -1 if not found
	'''
	start = 0
	end = len(ls)
	mid = (start + end) //2
	while start <= end and mid < len(ls):
		if ls[mid] > val:
			end = mid - 1
		elif ls[mid] < val:
			start = mid + 1
		else:
			return mid
		mid = (start + end) // 2
	return -1


def list_to_dict(ls):
	'''
	given a ls of values [a,b,c,d...] 
	return a dictionary {a: b, c: d...}
	'''
	aDict = {}
	for i in range(0,len(ls),2):
		aDict[ls[i]] = ls[i + 1]
	return aDict

def max_of_dict(d):
	'''
	return the key of the greatest value  
	in a dictionary of {key: value...}
	ex: d = {"a": 1, "b": 4, "c": 8} -> "c"
	'''
	k = d.keys()[0]
	for i in d.keys():
		if d[i] > d[k]:
			k = i
	return k

if __name__ == "__main__":
	a = [[1,2,3,4,5, 6],
		[2,4,6,8],
		[1,2]]
	for i in a:
		print(list_to_dict(i))