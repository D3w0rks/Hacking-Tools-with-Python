import hashlib

def crackhack(inputPass):
    try:
        passFile = open("worldlist.txt","r")
    except:
        print("File not found")

    for password in passFile:
        encPass = password.encode('utf-8')
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest == inputPass:
            print(f"Password found {password}")


if __name__ == '__main__':
    crackhack("your_password")
