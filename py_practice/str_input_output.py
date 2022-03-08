''''#input function practice
my_name = input("What is your name?\n")
print("Hello " + my_name + "!!")

#Concatenation pratice
name= input("Enter your name: \n")
new_string = "Hello " +name
print(new_string + "!!")'''

# String functions cases

name = input("What is your name?\n")
choice = input("Enter your choice (1.Capitalize, 2.Upper, 3. Concatenate, 4.Lower) \n")
if choice == '1':
    x = name.capitalize()
    print("Hello " + x)
    #New comment
elif choice == '2':
    x = name.upper()
    print("Hello " + x)
elif choice == '3':
    x = input("Enter your friend name: \n")
    print(name.capitalize() + " " + x + " are friends!!")
    #new comment
elif choice == '4':
    print("Hello " + name.lower() + "!!")
else:
    print("Invalid choice!!!")