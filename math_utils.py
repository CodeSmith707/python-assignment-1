'''
1.	Design a module math_utils.py with functions:
factorial(n)
is_prime(n)
gcd(a,b)
Include exception handling for invalid or negative inputs. Import and test these functions from another script.
Concepts: Loops, recursion, functions, input validation.
'''

#factorial function

usrFacInput = int(input("\nenter number:"))

def factorial(n):
    fac  = 1
    i = 0
    while fac != 0 and i !=n:
        fac = fac*(n-i)
        i = i + 1
    
    return fac

usrFacOutput = factorial(usrFacInput)
print("factorial is ", usrFacOutput)


#is_prime function

usrPrimeInput = int(input("\n enter number:"))

def is_prime(n):
    counter = 0
    i=1
    while i<=n:
        if n%i == 0:
            counter = counter + 1
        i = i + 1
    if counter == 2:
        return True
    else:
        return False

usrPrimeOutput = is_prime(usrPrimeInput)
if usrPrimeOutput == True:
    print("number is prime")
else:
    print("number is not prime")

#gcd function
n1 = int(input("enter number:"))
n2 = int(input("enter number:"))

def gcd(a,b):
    aList = [0] * (a+1)   
    bList = [0] * (b+1)

    i_a = 1
    j_a = 0
    while (i_a <= a):
        if a % i_a == 0:
            aList[j_a] = i_a   
            j_a = j_a + 1
        i_a = i_a + 1

    i_b = 1
    j_b = 0
    while (i_b <= b):
        if b % i_b == 0:
            bList[j_b] = i_b   
            j_b = j_b + 1
        i_b = i_b + 1 

    if j_a > j_b:
        MaxCompIndex = j_b
    else:
        MaxCompIndex = j_a

    great_cd = 1   

    i = 0
    while i < MaxCompIndex:   
        if aList[i] == bList[i] and aList[i] != 0:
            great_cd = aList[i]
        i = i + 1
    
    return great_cd

g_cd = gcd(n1, n2)
print("GCD:", g_cd)
