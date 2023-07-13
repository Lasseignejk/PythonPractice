import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(alphabet_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

isOn = True 
while isOn: 
    user_input = input("What would you like to translate? ")
    if user_input == "q" or user_input == "Q":
        isOn = False
        print("Thank you for using this service!")
        break
    answer = [alphabet_dict[letter] for letter in user_input.upper() if letter in alphabet_dict]
    print(answer)
