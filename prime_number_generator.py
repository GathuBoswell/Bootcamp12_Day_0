def is_prime(num):
    if num % 2 != 0: # only pass odd numbers
        for i in range(3, num):
            if num % i == 0:
                return False
        return True

def prime_number_gen(n):
    primes_list = []
    if type(n) != int:
        return 'Only Numbers allowed'
    elif n < 0:
        return 'Only Positve Numbers allowed'
    elif n <= 1:
        return []
    elif n >= 2:
        primes_list.append(2)
    for x in range(3, n+1):
        if is_prime(x):
            primes_list.append(x)
    return primes_list



def main():
    print(prime_number_gen(100000))

if __name__ == '__main__':main()

