import hashlib, time, os, shutil
from colorama import Fore

words = set()

jsexp_gay = """
           /$$$$$$$            /$$                           /$$                          
          | $$__  $$          | $$                          | $$                          
 /$$$$$$$$| $$  \ $$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$ 
|____ /$$/| $$  | $$ /$$__  $$| $$__  $$ |____  $$ /$$_____/| $$__  $$ /$$__  $$ /$$__  $$
   /$$$$/ | $$  | $$| $$$$$$$$| $$  \ $$  /$$$$$$$|  $$$$$$ | $$  \ $$| $$$$$$$$| $$  \__/
  /$$__/  | $$  | $$| $$_____/| $$  | $$ /$$__  $$ \____  $$| $$  | $$| $$_____/| $$      
 /$$$$$$$$| $$$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$ /$$$$$$$/| $$  | $$|  $$$$$$$| $$      
|________/|_______/  \_______/|__/  |__/ \_______/|_______/ |__/  |__/ \_______/|__/      
                                                                               
"""

def clear_screen():
    os.system("cls || clear")

def printcenter(text):
    size = shutil.get_terminal_size().columns
    for line in text.split("\n"):
        print(' ' * (round((size/2)-len(line)/2)), line)

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

def main():
    clear_screen()
    print()
    printcenter(f"{Fore.YELLOW}{jsexp_gay}")
    wordlist = input(f"{Fore.RED} [»] {Fore.LIGHTBLUE_EX}Nombre/Ruta de la Wordlist: {Fore.WHITE}")
    if not os.path.isfile(wordlist):
        clear_screen()
        printcenter(f"{Fore.YELLOW}{jsexp_gay}")
        printcenter(f"{Fore.LIGHTBLUE_EX}[ERROR] {Fore.WHITE}No se pudo cargar la Wordlist, intentalo nuevamente.")
        time.sleep(5)
        print()
        main()
    else:
        clear_screen()
        printcenter(f"{Fore.YELLOW}{jsexp_gay}")
        printcenter(f"{Fore.LIGHTBLUE_EX}[LOG] {Fore.WHITE}Cargando la Wordlist, espera..")
        with open(wordlist, 'r', encoding="latin-1") as f:
            lines = f.read().splitlines()
            words.update(lines)
            clear_screen()
            printcenter(f"{Fore.YELLOW}{jsexp_gay}")
            printcenter(f"{Fore.LIGHTBLUE_EX}             [LOG]{Fore.WHITE} Han sido cargadas {Fore.RED}{len(words)} {Fore.WHITE}contraseñas.")
            print()
            printcenter(f"{Fore.LIGHTBLUE_EX}[INFO] {Fore.WHITE}Introduce el Hash, luego el Salt. {Fore.YELLOW}¿No tienes Salt? {Fore.WHITE}Dejalo vacio.")
            print()
            while True:
                hash, salt = "", ""
                hash = input(f"{Fore.RED} [»] {Fore.LIGHTBLUE_EX}Introduce un hash: {Fore.WHITE}")
                print()
                salt = input(f"{Fore.RED} [»] {Fore.LIGHTBLUE_EX}Introduce un salt: {Fore.WHITE}")
                final = bruteforce(hash, salt)
                if final == hash:
                    clear_screen()
                    printcenter(f"{Fore.YELLOW}{jsexp_gay}")
                    printcenter(f"{Fore.LIGHTBLUE_EX}[LOG]{Fore.WHITE} Hash/Salt invalido o contraseña no encontrada.")
                    time.sleep(5)
                    clear_screen()
                    printcenter(f"{Fore.YELLOW}{jsexp_gay}")
                    printcenter(f"{Fore.LIGHTBLUE_EX}             [LOG]{Fore.WHITE} Han sido cargadas {Fore.RED}{len(words)} {Fore.WHITE}contraseñas.")
                    print()
                    printcenter(f"{Fore.LIGHTBLUE_EX}[INFO] {Fore.WHITE}Introduce el Hash, luego el Salt. {Fore.YELLOW}¿No tienes Salt? {Fore.WHITE}Dejalo vacio.")
                    print()
                    continue
                if final != hash:
                    clear_screen()
                    printcenter(f"{Fore.YELLOW}{jsexp_gay}")
                    printcenter(f"{Fore.LIGHTBLUE_EX}[LOG]{Fore.WHITE} Posible contraseña encontrada -> {Fore.RED}{final}")
                    print()
                    printcenter(f"{Fore.YELLOW}(1) {Fore.WHITE}Menu principal {Fore.YELLOW}(2) {Fore.WHITE}Salir")
                    print()
                    option = input(f"{Fore.RED} [»] {Fore.LIGHTBLUE_EX}Selecciona una opcion: {Fore.WHITE}")
                    if option == "1":
                        main()
                    elif option == "2":
                        clear_screen()
                        exit()
                    else:
                        clear_screen()
                        printcenter(f"{Fore.YELLOW}{jsexp_gay}")
                        printcenter(f"{Fore.LIGHTBLUE_EX}[ERROR] {Fore.WHITE}¡Debes de seleccionar una opcion valida!")
                        time.sleep(5)
                        main()

if __name__ == "__main__":
    main()
