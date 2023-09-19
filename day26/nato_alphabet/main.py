import pandas

data = pandas.read_csv("day26/nato_alphabet/nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(alphabet_dict)

isOn = True 
while isOn: 
    user_input = input("What would you like to translate? ").upper()
    if user_input == "q" or user_input == "Q":
        isOn = False
        print("Thank you for using this service!")
        break
    try:
        answer = [alphabet_dict[letter] for letter in user_input]
        print(answer)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
