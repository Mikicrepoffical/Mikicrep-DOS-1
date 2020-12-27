# Importing Libraries And Loading OS
import time
import os

print("33% loaded")

catche = 0
one = 0
two = 0

print("66% loaded")

# +
def addcalc(x, y):
    return x + y

# -
def subtractcalc(x, y):
    return x - y

# *
def multiplycalc(x, y):
    return x * y

# /
def dividecalc(x, y):
    return x / y

print("100% loaded")

# NOTICES
print("Before you load... You need to know something:\n")
print("Use it maximized for best expirience\n\nOnly lowercase accepted\n\nEnter any text to continue and press enter")
catche = input()

# Asking where to boot
print("From Where To Boot\n\n1.) Hard Drive\n2.) MDisc")
one = input()

if one == "1":
    print("BOOTING... PLEASE WAIT")
    time.sleep(10)
    print("SOON")
    time.sleep(5)

if one == "2":
    print("Select MDisc:")
    print("1.) Calculator")
    print("2.) Timer")
    two = input()

    print("Loading... Please Wait")
    time.sleep(2)

if two == "1":
    while True:

        print("Select operation:")
        print("1 = +")
        print("2 = -")
        print("3 = *")
        print("4 = /")
        print("version = show current version of calculator")
        print("ver = show current version of calculator")
        print("exit = exits calculator")

        # Take input from the user
        choicecalc = input("Enter choice(1/2/3/4/version/ver/exit): ")

        if choicecalc in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choicecalc == '1':
                print(num1, "+", num2, "=", addcalc(num1, num2))

            elif choicecalc == '2':
                print(num1, "-", num2, "=", subtractcalc(num1, num2))

            elif choicecalc == '3':
                print(num1, "*", num2, "=", multiplycalc(num1, num2))

            elif choicecalc == '4':
                print(num1, "/", num2, "=", dividecalc(num1, num2))
                break
                    
        if choicecalc == "version":
            print("Version 1.0")
                
        if choicecalc == "ver":
            print("Version 1.0")

        if choicecalc == "exit":
            break

if two == "2":
    mu = 0
    s = 0

    print("Enter How Many Seconds To Count")
    mu = int(input())

    while s <= mu:
        print(s, "seconds is passed")
        time.sleep(1)
        s += 1
    print("Finished")
    time.sleep(10)

