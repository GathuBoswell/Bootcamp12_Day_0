# Bootcamp12_Day_0
	This a pyhton code to return a list of prime numbers between zero an n
	
## Asymptotic Analysis
	To achieve this functionality i used two functions:
		one to check is a number is prime: is_prime(n) and another to generate the list of prime numbers
	This increases the number of iterations to be done per number to be checked and added to the list
	since each number is passed to the is_prime() function first.
	
	__Asymptotic test for is_prime__
	Every number which is even is returned as false imediately this reduces number of iterations by half
		
