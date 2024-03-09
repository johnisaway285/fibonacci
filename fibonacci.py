# Import math libary, sqrt does not come with python :(
from math import sqrt

#main function
def main():
    a = int(input("Please enter the number for n: "))
    print(int(fibonacci(a)))

#Core function
def fibonacci(a_number):
    return ((1+sqrt(5))**a_number-(1-sqrt(5))**a_number)/(2**a_number*sqrt(5))    

#You know the drill
if __name__ == "__main__":
    main()