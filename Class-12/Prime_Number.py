limit = int(input("Enter a number: "))
count = 0
loop_count = 0
for x in range(2, limit):
    n = x
    isPrime = True

    for i in range(2, n):
        loop_count += 1
        if n % i == 0:
            isPrime = False
            break

    if isPrime:
        count += 1
        print(f"{count} - {x}")
