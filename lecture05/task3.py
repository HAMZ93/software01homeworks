def is_prime(number):
    if number <= 1:
        return False, None
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False, i  # return the divisor that proves it's not prime
    return True, None

num = int(input("Enter an integer: "))

prime, divisor = is_prime(num)

if prime:
    print(f"{num} is a prime number.")
else:
    if divisor:
        print(f"{num} is not a prime number because it is divisible by {divisor}.")
    else:
        print(f"{num} is not a prime number.")





