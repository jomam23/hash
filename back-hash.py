import string

# Define character set
char = string.ascii_letters + string.digits + string.punctuation

# Read the key from key.txt
with open("key.txt", "r") as file:
    key = file.read()

# Input from user
ine = input("write: ")

# First encryption
text = ""
for letter in ine:
    if letter in char:
        index = char.index(letter)
        text += key[index]
    else:
        text += letter  # If char not in set, leave it unchanged

# Second encryption
text3 = ""
for letter in text:
    if letter in char:
        index = char.index(letter)
        text3 += key[index]
    else:
        text3 += letter

# Read the stored encrypted password
with open("ciphertext.txt", "r") as file:
    stored_password = file.read().strip()  # Strip to remove trailing newline

# Check if encrypted password matches
if text3 == stored_password:
    print("Password is correct")
else:
    print("Password is incorrect")
