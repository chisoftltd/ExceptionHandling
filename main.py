# Exception Handling

# try:
#     file = open("test_file.txt")
#     test_dictionary = {"key": "value"}
#     print(test_dictionary["key"])
# except FileNotFoundError:
#     file = open("test_file.txt", "w")
#     file.write("Something")
# except KeyError as error_msg:
#     print(f"The key {error_msg} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is error that I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
