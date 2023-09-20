# try:
#     file = open("day30/a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt","w")
#     print("FileNotFound, file created.")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally: 
#     raise KeyError("This is an error that I made up.")

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 300:
#     raise ValueError("Human height should not be over 300cm.")

# bmi = weight / height ** 2
# print(bmi)
