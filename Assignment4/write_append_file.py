
user_input = input("Enter some text to write into output.txt: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("Data written successfully!")

append_input = input("Enter some text to append to output.txt: ")

with open("output.txt", "a") as file:
    file.write(append_input + "\n")

print("Data appended successfully!")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
