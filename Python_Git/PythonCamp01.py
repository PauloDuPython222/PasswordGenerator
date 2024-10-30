

from random import choice
from random import shuffle



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
l = []

print("\33[31mWelcome to the PyPassword Generator!")
nr_letters= int(input("\33[34mHow many letters would you like in your password?\n"))
for c in range(0, nr_letters):
    l.append(choice(letters))


nr_symbols = int(input(f"How many symbols would you like?\n"))
for c in range(0, nr_symbols):
    l.append(choice(symbols))

nr_numbers = int(input(f"How many numbers would you like?\n"))
for c in range(0, nr_numbers):
    l.append(choice(numbers))

random.shuffle(l)
l = "".join(l)
print(f"\33[mYour New Password is: \33[31m{l}")









#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P