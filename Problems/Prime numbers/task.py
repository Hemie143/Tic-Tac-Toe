prime_numbers = [n for n in range(2, 1001) if all(n % x for x in range(2, n))]
