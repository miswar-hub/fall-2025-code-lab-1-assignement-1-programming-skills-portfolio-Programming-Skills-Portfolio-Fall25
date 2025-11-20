

#Dictionary of the European countries and their capitals
info = {
    "Spain": "Madrid",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "russia" : "moscow",
    "Italy": "Rome",
    "Portugal": "Lisbon",
    "Croatia": "Zagreb",
    "Belgium": "Brussels",
    "finland": "helsinki",
}
marks = 0
#Asking the questions
for country, capital in info.items():
    answer = input(f"What is the capital of {country}? ")
    #Ignoring capitalization
    if answer.strip().lower() == capital.lower():
        print("The answer you entered is correct!")
        marks += 1
    else:
        print(f"Wrong! The correct answer is {capital}.")
#Print final score
print(f"\nYou got {marks} out of {len(info)} correct!")