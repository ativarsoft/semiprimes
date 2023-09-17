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
		#if numerator >= denominator<<2:
		#	numerator_mod_denominator=numerator%denominator
		#	if numerator_mod_denominator == 0:
		#		numerator=numerator/denominator
		#		# denominator/=denominator
		#		denominator=1
		#if denominator >= n:
		#	print "denominator >= n"
		#	denominator_mod_n=denominator%n
		#	if denominator_mod_n == 0:
		#		print("found  harmonic " + str(x))
		#		return numerator*n/denominator
		#	#print("error? denominator > n")
		#	#exit()
		print("x=" + str(x) + " numerator=" + str(numerator) + " denominator=" + str(denominator))
		if denominator >= n:
			print "denominator >= n"
			n_mod_denominator=n%denominator
			"n_mod_denominator=" + str(n_mod_denominator)
			if n_mod_denominator == n:
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
