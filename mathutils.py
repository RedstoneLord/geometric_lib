def gcd(a,b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a,b):
    return abs(a * b) // gcd(a, b)

def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True