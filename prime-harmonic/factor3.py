import sys

def get_next_y(n):
	numerator=3
	denominator=2
	denominator_mod_n=n%denominator
	n_mod_denominator=-1
	x=2 # x-th harmonic
	while True:
		x=x+1
		old_denominator=denominator
		denominator=denominator*x
		numerator=numerator*x+old_denominator
		
		# if w is (the result of sum) then numerator*n/denominator = x*n-(x-1)
		print("x=" + str(x) + " numerator=" + str(numerator) + " denominator=" + str(denominator))
		#l1 = numerator*n
		#l2=l1-denominator
		#print("l1=" + str(l1) + " l2=" + str(l2))
		#print("l1%l2=" + str(l1%l2))
		if numerator%denominator==1:
			print("found  harmonic " + str(x))
			return numerator*n/denominator

		if x > n:
			print("error: x > n")
			exit()
	
if len(sys.argv) != 2:
	print("Incorrect number of arguments.")
	exit()

n=int(sys.argv[1])
print("numerator*n/denominator=" + str(get_next_y(n)))
