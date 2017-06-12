def prime_number(n):
	primes = []
	if n<2:
		return False

	else:
		for prime in range(2, n):
		    for b in range(2, prime):
		        if (prime % b == 0):
		            break
		    else:
		        primes.append(prime)

		return primes