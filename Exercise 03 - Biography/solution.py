

#Making the user input the details
name = str(input("Enter your name:"))
hometown = str(input("Enter your hometown:"))
#Checking if the age given by the user is string or integer
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid age.")
#Storing the information in a dictionary
Biography={
    "Name":name,
    "Hometown":hometown,
    "Age":age}
#Print the values
print(f"Name: {Biography['Name']} \nHometown: {Biography['Hometown']} \nAge: {Biography['Age']}")
