def get_primes(target: int) -> list[int]:
    """Nice way of finding primes using sieve of Testothanes"""
    if target < 2:
        return []
    is_prime = [True] * target
    is_prime[0] = False

    if target >= 1:
        is_prime[1] = False

    for num in range(2, int(target**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, target, num):
                is_prime[multiple] = False

    return [idx for idx, prime in enumerate(is_prime) if prime]


def find_highest_prime_factor(target: int) -> int:
    """Finds highest prime factor of given target integer"""

    remaining = target
    factor = 2
    largest = 1

    # You don't need to check factors above the square root of the remainder
    # If you have checked all the factors up to and including the square root, only
    # other option is for the remaining target to be prime itself (i.e., two numbers
    # above the square root will always multiply together to make a too large number)
    while factor**2 <= remaining:
        # Divide out current factor as many times as possible before moving on
        while remaining % factor == 0:
            largest = factor
            remaining //= factor

        # Once you've tested 2, you don't need to test any other even factors
        if factor == 2:
            factor = 3
        else:
            factor += 2

    if remaining > 1:
        largest = remaining

    return largest


def main():

    target = 600851475143
    # target = 13195

    print(find_highest_prime_factor(target))


if __name__ == "__main__":
    main()
