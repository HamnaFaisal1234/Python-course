def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_two_digit_primes():
    two_digit_primes = []
    for num in range(10, 100):
        if is_prime(num):
            two_digit_primes.append(num)
    return two_digit_primes


primes = find_two_digit_primes()
print("Two-digit prime numbers are:", primes)
