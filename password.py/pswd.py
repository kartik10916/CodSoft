import random
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the length of the password: "))
generated_password = password_generator(password_length)
print("Generated Password:", generated_password)






