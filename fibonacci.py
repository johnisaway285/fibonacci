from math import sqrt
def main():
    a = int(input("Please enter the number for n: "))
    print(int(fibonacci(a)))

#This function will determine the number of the fibonacci number
def fibonacci(a_number):
    return ((1+sqrt(5))**a_number-(1-sqrt(5))**a_number)/(2**a_number*sqrt(5))    

if __name__ == "__main__":
    main()