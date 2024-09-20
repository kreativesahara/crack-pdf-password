import pikepdf
import time
from colorama import Fore

password_file = open("passwordfile.txt")

i = 0
start_time = time.time()
for password in password_file:
    i += 1
    print(Fore.RED+f"\r {i} Password is tested {password.strip()}", end = "")
    try:
        with pikepdf.open("2024.pdf",password = password.strip("\n")) as pdf:
            # Added this line to save the decrypted vision of the file inside our project folder.
            extract = pdf.save("unlocked.pdf")
            end_time = time.time()

        print("\n")
        print(Fore.GREEN+ f"password found in {str(end_time-start_time)[:4]} second \nPassword is: ", end = "")
        print(Fore.BLUE+ f" {password}")

        break
    except:
        pass
