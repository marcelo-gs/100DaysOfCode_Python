#Write your code below this line 👇
def prime_checker(number):
    if number in (1,2,3,5,7):
        print("prime!")
        return
    for num in (2,3,5,7):
        if divisible(number, num):
            print("not prime!", num)
            return
    print("It's prime!")

def divisible(n, x):
    return (n % x == 0)

def Teachers_soluction(number):
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)