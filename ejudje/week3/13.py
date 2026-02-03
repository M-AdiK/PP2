def isPrime(x):
    if x < 2: return False

    result = True
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            result = False
            break
    return result

nums = list(map(int, input().split()))

prime = list(filter(lambda x : isPrime(x), nums))

if len(prime) > 0:
    print(*prime)

else :
    print("No primes")