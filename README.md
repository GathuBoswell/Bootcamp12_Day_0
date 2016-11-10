# Bootcamp12_Day_0
	This a python code to return a list of prime numbers between zero an n
	
## Asymptotic Analysis
	To achieve this functionality i used two functions:
		one to check is a number is prime: is_prime(n) and another to generate the list of prime numbers
	This increases the number of iterations to be done per number to be checked and added to the list
	since each number is passed to the is_prime() function first.
	
	It does well for numbers below 10000 but takes a lot of time for numbers above 10000
	Hence this solution is a good base case but requires improvment or a better algorithm
		
