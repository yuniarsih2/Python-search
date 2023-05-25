def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_prime_numbers(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers


bilangan = [7, 10, 13, 6, 17, 22, 19]
bilangan_prima = find_prime_numbers(bilangan)
print("Bilangan prima dalam daftar :", bilangan_prima)
