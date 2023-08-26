numbers = [i for i in range(1, 10)]

def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

result = list(map(lambda n: is_prime(n), numbers))
print(result)
