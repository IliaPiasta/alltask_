def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def prime_divisors(number):
    divisors = []
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            divisors.append(i)
    return divisors

num = 30
print("Прості дільники:", prime_divisors(num))