def is_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
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
    elif n == 0:
        return []
    for x in range(2, n+1):
        if is_prime(x):
            primes_list.append(x)
    return primes_list



def main():
    print(is_prime(2))
    print(prime_number_gen(2))

if __name__ == '__main__':main()

