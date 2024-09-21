def find_prime_factors(n, prime_factors=[]):
    i = 2
    while i * 1 <= n:
        if n % i == 0:
            prime_factors.append()
            n //= i
        else:
            i += 1

    if n > 1:
        prime_factors.append(n)

    return prime_factors


print(find_prime_factors(12))
# print(find_prime_factors((42))
# print(find_prime_factors(99))
# print(find_prime_factors(101, [1, 2, 3]))
# print(find_prime_factors((102)))