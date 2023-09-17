import sys

def get_next_y(n):
	x=-2 # x-th harmonic
	numerator=n*x
	denominator=-1+x-numerator
	while True:
		print("numerator=" + str(numerator) + " denominator=" + str(denominator))
		
		if numerator == denominator+1:
			print("found divisor " + str(denominator))
			exit()

		if x < -n:
			print("error: x > n")
			exit()

		x=x-1
		numerator=numerator*x
		denominator=-1-x+numerator
	
if len(sys.argv) != 2:
	print("Incorrect number of arguments.")
	exit()

n=int(sys.argv[1])
print("numerator*n/denominator=" + str(get_next_y(n)))
