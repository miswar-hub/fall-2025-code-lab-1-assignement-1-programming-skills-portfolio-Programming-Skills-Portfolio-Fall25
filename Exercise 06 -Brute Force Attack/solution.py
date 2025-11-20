

#Defining the correct password
password = 53412
#Maximum number of attempts
max_attempts = 5
attempts = 0
#Using while loop to control the attempts
while attempts < max_attempts:
    a = int(input("Enter your password:"))
    attempts += 1
    if a == password:
        print("The password you entered is correct!")
        break
    else:
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You only have {remaining_attempts} attempts left!")
        else:
            print("You have entered too many incorrect passwords!")