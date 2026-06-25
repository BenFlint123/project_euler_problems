def get_primes(target: int) -> list[int]:
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


def get_lowest_prime_factor(target: int, primes: list[int] | None = None) -> int:
    if primes is None:
        primes = get_primes(target)

    for prime in primes:
        if target % prime == 0:
            return prime

    raise ValueError("Error: lowest prime factor not found. Try adding larger primes")


def get_prime_factors(target: int) -> list[int]:
    primes = get_prime_factors(target)
    prime_factors = []

    while target not in primes:
        prime_factor = get_lowest_prime_factor(target, primes)
        prime_factors.append(prime_factor)
        target = target // prime_factor

    prime_factors.append(target)
    return prime_factors


def main():
    print(get_prime_factors(600851475143))


if __name__ == "__main__":
    main()
