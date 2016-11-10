# Bootcamp12_Day_0
	This a python code to return a list of prime numbers between zero an n
	
## Asymptotic Analysis
	To achieve this functionality i used two functions:
		one to check is a number is prime: is_prime(n) and another to generate the list of prime numbers
	This increases the number of iterations to be done per number to be checked and added to the list
	since each number is passed to the is_prime() function first.
	
	The recent commit greatly improves on the performance if the given number n is greater than 1,000,000
		
