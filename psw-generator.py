import random
import string
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password= "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    pswd_length = int(input("Enter length of password: "))

    if pswd_length < 1:
        print("Password must be at least 1 character")
    else:
        generated_password = generate_password(pswd_length)
        print("Your generated password is:", generated_password)
