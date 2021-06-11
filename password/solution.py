# Import String And Random (Inbuilt With Python)
import string
import random

# Make A List Of Special Characters
special_char = ["!", "@", "#", "$", "%", "&","?"]

# Select 3 Random Letters
letter1 = random.choice(string.ascii_letters)
letter2 = random.choice(string.ascii_letters)
letter3 = random.choice(string.ascii_letters)
letter4= random.choice(string.ascii_letters)

# Select 3 Random Numbers And Convert To String
number1 = str(random.randint(1, 10))
number2 = str(random.randint(1, 10))
number3 = str(random.randint(1, 10))

# Pick A Random Character From The `special_char` List
character = random.choice(special_char)

# Combine
password = letter1 + letter2 + letter3 + letter4 + number1 + number2 + number3 + character

# Append Each Letter To A List
pass_list = []
for i in password:
    pass_list.append(i)

# Shuffle The List
random.shuffle(pass_list)

# Join The List
password = ''.join(pass_list)

# Print The Password
print(password)
