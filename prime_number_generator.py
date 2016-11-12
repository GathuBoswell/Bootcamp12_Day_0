def prime_number_gen(n):
    """
    The is_prime function has been defined in here to hide it from the outer scope

    :param n:
    :return [prime numbers between 0 and n]:
    """
    def is_prime(num):
        """
        returns True if num is prime else, False
        :param num:
        :return bool:
        """
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    primes_list = []
    if type(n) != int:
        return 'Only Numbers allowed'
    elif n < 0:
        return 'Only Positive Numbers allowed'
    elif n <= 1:
        return []
    elif n >= 2:
        primes_list.append(2)
    for x in range(3, n+1, 2):
        if is_prime(x):
            primes_list.append(x)
    return primes_list



def main():
    print(prime_number_gen(1000000))

if __name__ == '__main__':main()

