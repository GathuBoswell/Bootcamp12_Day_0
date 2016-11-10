
def prime_number_gen(n):
    primes_list = []
    for num in range(2, n):
        if num == 2:
            primes_list.append(num)
        else:
            for i in range(3, num):
                if num % i == 0:
                    pass
            primes_list.append(num)
    return primes_list
def main():
    print(prime_number_gen(10))

