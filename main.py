##############################################################################################

import hashlib, time, os, shutil
from colorama import Fore

words = set()

##############################################################################################

logo = """
·▄▄▄▄  ▄▄▄ . ▄ .▄ ▄▄▄· .▄▄ ·  ▄ .▄▄▄▄ .▄▄▄  
██▪ ██ ▀▄.▀·██▪▐█▐█ ▀█ ▐█ ▀. ██▪▐█▀▄.▀·▀▄ █·
▐█· ▐█▌▐▀▀▪▄██▀▐█▄█▀▀█ ▄▀▀▀█▄██▀▐█▐▀▀▪▄▐▀▀▄ 
██. ██ ▐█▄▄▌██▌▐▀▐█ ▪▐▌▐█▄▪▐███▌▐▀▐█▄▄▌▐█•█▌
▀▀▀▀▀•  ▀▀▀ ▀▀▀ · ▀  ▀  ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀  ▀
"""
error = """
▄▄▄ .▄▄▄  ▄▄▄        ▄▄▄  
▀▄.▀·▀▄ █·▀▄ █·▪     ▀▄ █·
▐▀▀▪▄▐▀▀▄ ▐▀▀▄  ▄█▀▄ ▐▀▀▄ 
▐█▄▄▌▐█•█▌▐█•█▌▐█▌.▐▌▐█•█▌
 ▀▀▀ .▀  ▀.▀  ▀ ▀█▄▀▪.▀  ▀
"""

##############################################################################################

def printcenter(text):
    size = shutil.get_terminal_size().columns
    for line in text.split("\n"):
        print(' ' * (round((size/2)-len(line)/2)), line)

##############################################################################################

def bruteforce(hash, salt):
    if len(hash) == 64:
        for password in words:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            if password_hash == hash:
                return password
    elif len(hash) == 86 or len(hash) == 85:
        parts = hash.split("$")
        salt1 = parts[2]
        hash1 = parts[3]
        for word in words:
            var2 = hashlib.sha256(word.encode()).hexdigest()
            final = hashlib.sha256((var2 + salt1).encode()).hexdigest()
            if final == hash1:
                return word
    elif len(hash) == 128:
        for word in words:
            var2 = hashlib.sha512(word.encode()).hexdigest()
            final = hashlib.sha512((var2 + salt).encode()).hexdigest()
            if final == hash:
                return word
    elif "SHA256" in hash:
        parts = hash.split("$")
        salt = parts[1]
        wow = parts[2]
        for word in words:
            word_hash = hashlib.sha256(hashlib.sha256(word.encode()).hexdigest().encode() + salt.encode()).hexdigest()
            if word_hash == wow:
                return word
    elif "SHA512" in hash:
        parts = hash.split("$")
        salt = parts[1]
        wow = parts[2]
        for word in words:
            passenc = hashlib.sha512(word.encode()).hexdigest()
            word_hash = hashlib.sha512((passenc + salt).encode()).hexdigest()
            if word_hash == wow:
                return word
    return hash

##############################################################################################

def main():
    os.system("cls || clear")
    print()
    printcenter(f"{Fore.YELLOW}{logo}")
    print()
    wordlist = input(f"{Fore.RED} [»] {Fore.LIGHTBLUE_EX}Indica el nombre de la wordlist: {Fore.RESET}")
    if not os.path.isfile(wordlist):
        os.system("cls || clear")
        printcenter(f"{Fore.YELLOW}{logo}")
        print()
        printcenter(f"{Fore.RESET}La wordlist no ha sido cargada.")
        time.sleep(3)
        print()
        main()
    else:
        os.system("cls || clear")
        printcenter(f"{Fore.YELLOW}{logo}")
        print()
        with open(wordlist, 'r', encoding="latin-1") as f:
            lines = f.read().splitlines()
            words.update(lines)
            print(f"{Fore.LIGHTBLUE_EX}             [LOG]{Fore.RESET} Han sido cargadas {Fore.RED}{len(words)} {Fore.RESET}contraseñas.", end="\r")
            print()
            print()
            while True:
                hash, salt = "", ""
                hash = input(f"{Fore.RED} [»] {Fore.LIGHTBLUE_EX}Introduce un hash: {Fore.RESET}")
                print()
                if len(hash) == 128:
                    salt = input(f"{Fore.RED} [»] {Fore.LIGHTBLUE_EX}Introduce un salt: {Fore.RESET}")
                final = bruteforce(hash, salt)
                if final == hash:
                    os.system("cls || clear")
                    printcenter(f"{Fore.YELLOW}{logo}")
                    print()
                    printcenter(f"{Fore.LIGHTBLUE_EX}[LOG]{Fore.RESET} La contraseña no ha sido encontrada.")
                    time.sleep(3)
                    main()
                if final != hash:
                    os.system("cls || clear")
                    printcenter(f"{Fore.YELLOW}{logo}")
                    print()
                    printcenter(f"{Fore.LIGHTBLUE_EX}[LOG]{Fore.RESET} La contraseña es -> {Fore.RED}{final}")
                    print()
                    printcenter(f"{Fore.YELLOW}(1) {Fore.RESET}Volver")
                    printcenter(f"{Fore.YELLOW}(2) {Fore.RESET}Salir")
                    print()
                    option = input(f"{Fore.RED} [»] {Fore.LIGHTBLUE_EX}Seleccione una opcion: {Fore.RESET}")
                    if option == "1":
                        main()
                    elif option == "2":
                        os.system("cls || clear")
                        exit()
                    else:
                        os.system("cls || clear")
                        printcenter(f"{Fore.RED}{error}")
                        printcenter(f"{Fore.RESET}¡Debes de seleccionar una opcion valida!")
                        time.sleep(3)
                        main()


##############################################################################################

main()
