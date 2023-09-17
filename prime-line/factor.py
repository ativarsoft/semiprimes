import sys

def factor(n):
	a=3 # current number
	b=n-n%2 # n / a, number of integer divisors times a
	c=0 # n % a
	d=0 # a - c
	
	while True:
		# print first to print 1
		for i in range(0, a):
			print("-", end='')
		for i in range(0, b - a):
			print("*", end='')
		for i in range(0, c):
			print("#", end='')
		for i in range(0, d):
			print("$", end='')
		print(" a=" + str(a) + " b=" + str(b))
		
		
		#if b != n // a * a and a != 1:
		#	print("b is " + str(b) + " should be " + str(n//a * a))
		#	exit()
		
		#if c != n % a and a != 1:
		#	print("c is " + str(c) + " should be " + str(n%a))
		#	exit()
		
		#if d != a-(n%a):
		#	print("d should be " + str(a-(n%a)))
		
		if a == n:
			return a
		
		#if c == 0 and d == 0:
		#	return a
		
		#if c == 0 and d > 0:
		#	print("error: c == 0 and d > 0")
		#	exit()
		
		# calculate next number
		a=a+1
		#adiciona-se a ao c porque cada devisor de n agora tem mais uma unidade
		# (x+1)//n-x//n = x
		#
		if b+a>n:
			b=b-a
		else:
			b=b+a
	
	
if len(sys.argv) != 2:
	print("Incorrect number of arguments.")
	exit()

n=int(sys.argv[1])
print(str(factor(n)))
