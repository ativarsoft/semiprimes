import sys

def get_next_y(n):
	numerator=3
	denominator=2
	denominator_mod_n=-1
	x=2 # x-th harmonic
	while True:
		x=x+1
		denominator=denominator*x
		numerator=numerator*denominator+1
		denominator_mod_n=denominator%n
		print("x=" + str(x) + " numerator=" + str(numerator) + " denominator=" + str(denominator) + " denominator_mod_n=" + str(denominator_mod_n))
		if denominator_mod_n == 0:
			#print("x=" + str(x))
			return numerator*n/denominator
	
if len(sys.argv) != 2:
	print("Incorrect number of arguments.")
	exit()

n=int(sys.argv[1])
print("numerator*n/denominator=" + str(get_next_y(n)))
