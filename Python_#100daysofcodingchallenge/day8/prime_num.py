def prime_checker(number):
    for num in range(1, number):
        if number % num == 0:
            if num == 1 or num == number:
                continue
            else:
                print("It's not a prime number")
                exit()
    print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)