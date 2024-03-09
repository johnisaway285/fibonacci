def main():
    a = int(input("Please enter the number for n: "))
    print(condition_det(a))

#This function will determine the number of the fibonacci number
def fibonacci(a_number):
    if a_number ==0:
        return 0
    elif a_number == 1 or a_number ==2:
        return 1
    else:
        return condition_det(a_number-1)+condition_det(a_number-2)
        

if __name__ == "__main__":
    main()