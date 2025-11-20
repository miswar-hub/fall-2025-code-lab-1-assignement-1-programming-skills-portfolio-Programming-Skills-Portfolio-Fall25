## Exercise 10: Is it even? - 35 Marks

def check_odd_even(number):
    #Function for checking if the number is odd or even
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

def main():
    #Asking the user to input the number
    num = int(input("Enter a number:"))
    #Passing the numer to the function
    result = check_odd_even(num)
    #Print the messgae
    print(result)

if __name__ == "__main__":
    main()