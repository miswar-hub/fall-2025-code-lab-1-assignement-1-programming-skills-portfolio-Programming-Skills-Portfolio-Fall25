

#Creating a list of names
names = ["Jake","Zac", "Ian", "Ron", "Sam", "Dave"]
#Asking the user to search for a name
search = input("Enter your name:")
#Checking the name the user entered in there on the list
if search in names:
    print(f"{search} is there on the list")
else:
    print(f"{search} is not there in the list")