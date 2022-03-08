'''
Today, I learnt about loops, Ranges Code_BLocks.
so, came with a one practical project on the topic learnt!

SO, this is a password generator Project.
'''
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Password Generator\n")

no_letters=int(input("How many letter would you like to be there in your password\n"))
no_symbols=int(input(f"How many symbols would you like to add in your password\n"))
no_numbers=int(input(f"How many numbers you want to add in your password\n"))

# All the inputs are taken from the user.
'''
# (1st method) -> returning the password in terms of string.

password=""
for char in range(1,no_letters+1):
    password+=random.choice(letters)
for char in range(1,no_symbols+1):
    password+=random.choice(symbols)
for char in range(1,no_numbers+1):
    password+=random.choice(numbers)

print(password)
'''
#instead of using string, I can also use list for returning password
password=[]
for char in range(1,no_letters+1):
    password.append(random.choice(letters))
for char in range(1,no_numbers+1):
    password.append(random.choice(numbers))
for char in range(1,no_symbols+1):
    password.append(random.choice(symbols))
# print(password)
# print(str(password))
#printing passoword list
random.shuffle(password)
Password=''
for char in password:
    Password+=char
print(f"Your desired password is - {Password}")




