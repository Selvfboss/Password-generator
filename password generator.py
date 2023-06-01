#Password Generator Project
import string
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# genrating the first set of letters 
first_set = ''
for number in range(0, nr_letters):
  first_set = first_set + letters[random.randint(0, 25)]
#print(first_set)

#generating second_set
second_set = ''
for symbol in range(0, nr_symbols):
  second_set += symbols[random.randint(0, 8)]

#generating third set
third_set = ''
for number in range(0, nr_numbers):
  third_set += numbers[random.randint(0, 9)]
  
  
# easy level
password = first_set + second_set + third_set 
#hard level
def randomize_string (input_string):
  character_list = list(input_string)
  random.shuffle(character_list)
  randomized_string = ''.join(character_list)
  return randomized_string

print(randomize_string(password))  
  

  
