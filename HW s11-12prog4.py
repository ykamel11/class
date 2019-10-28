# Initialize a list
primes = []
for possiblePrime in range(2, 21):

    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False

    if isPrime:
        primes.append(possiblePrime)

print(primes)

inputNumb: int = input("please enter a number from 0 to 21")
if inputNumb in primes:
    print("congrats, the input number" + inputNumb + "is prime!")
else:
    print("the input number " + inputNumb + " is not a prime")
