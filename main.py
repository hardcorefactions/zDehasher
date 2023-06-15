import hashlib, argparse, time
from colour import Color
from PIL import ImageColor

class textUtil:
    RESET = '\033[0m'

    def printg(text, c1, c2):
        if text == "":
            print()
            return ""
        else:
            def get_color_escape(r, g, b, background=False):
                return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

            def get_rgb_code(hex):
                return ImageColor.getcolor(hex, "RGB")

            c1 = Color(c1)
            c2 = Color(c2)
            lt = len(text)
            cl = list(c1.range_to(c2,lt))
            col=0
            ft = ""
            for i in cl:
                i = str(get_rgb_code(str(i))).replace('(', '').replace(')', '').split(', ')
                i = get_color_escape(i[0], i[1], i[2])
                ft+=f"{i}{text[col]}"
                col+=1
            ft+=textUtil.RESET
            return ft

def bruteforce(hash, salt):
    if len(hash) == 86 or len(hash) == 85: # SHA256 - AuthMe - 1
        salt1 = hash.split("$")[2]
        hash1 = hash.split("$")[3]
        for word in words:
            var2 = hashlib.sha256(word.encode()).hexdigest()
            final = hashlib.sha256(var2.encode() + salt1.encode()).hexdigest()
            if final == hash1:
                return word
    if len(hash) == 128: # SHA512 - DBA
        for word in words:
            var2 = hashlib.sha512(word.encode()).hexdigest()
            final = hashlib.sha512((var2 + salt).encode()).hexdigest()
            if final == hash:
                return word
    return hash

words = []
parser = argparse.ArgumentParser(description='Dictionary requirement')
parser.add_argument('-f', '--file', type=str, help='Route to dictionary.')
args = parser.parse_args()
file = args.file
for _ in range(100): print()

logo = """██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗     ██████╗ ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗ █████╗ ██████╗ ██╗   ██╗
██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝     ██╔══██╗██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝
██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗    ██║  ██║██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████║██████╔╝ ╚████╔╝ 
██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║    ██║  ██║██║██║        ██║   ██║██║   ██║██║╚██╗██║██╔══██║██╔══██╗  ╚██╔╝  
███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝    ██████╔╝██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║██║  ██║██║  ██║   ██║   
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝ ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   """

for i in logo.split("\n"):
    print(textUtil.printg(i, "#ff0000", "#0000ff"))
print()
try:
    words = open(file, encoding='latin-1').readlines()
    print("  [~] Loaded succesfully " + str(len(words)) + " passwords.")
    time.sleep(3)
except Exception as e:
    print("  [~] Invalid file.")
    print()
    exit()

for _ in range(100): print()

logo = r"""████████▄     ▄████████    ▄█    █▄       ▄████████    ▄████████    ▄█    █▄       ▄████████    ▄████████ 
███   ▀███   ███    ███   ███    ███     ███    ███   ███    ███   ███    ███     ███    ███   ███    ███ 
███    ███   ███    █▀    ███    ███     ███    ███   ███    █▀    ███    ███     ███    █▀    ███    ███ 
███    ███  ▄███▄▄▄      ▄███▄▄▄▄███▄▄   ███    ███   ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀███▀  ▀███████████ ▀███████████ ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███    ███   ███    █▄    ███    ███     ███    ███          ███   ███    ███     ███    █▄  ▀███████████ 
███   ▄███   ███    ███   ███    ███     ███    ███    ▄█    ███   ███    ███     ███    ███   ███    ███ 
████████▀    ██████████   ███    █▀      ███    █▀   ▄████████▀    ███    █▀      ██████████   ███    ███ """

for i in logo.split("\n"):
    print(textUtil.printg(i, "#ff0000", "#0000ff"))
print()

hash, salt = "", ""

hash = input(textUtil.printg("[$] Insert the hash: ", "#ff0000", "#0000ff"))
if len(hash) == 128:
    salt = input(textUtil.printg("[$] Insert the salt: ", "#ff0000", "#0000ff"))

logo = r"""
▓█████▄ ▓█████  ██░ ██  ▄▄▄        ██████  ██░ ██  ██▓ ███▄    █   ▄████                
▒██▀ ██▌▓█   ▀ ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒               
░██   █▌▒███   ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░               
░▓█▄   ▌▒▓█  ▄ ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ░██░▓██▒  ▐▌██▒░▓█  ██▓               
░▒████▓ ░▒████▒░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░██░▒██░   ▓██░░▒▓███▀▒ ██▓  ██▓  ██▓ 
 ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒  ▒▓▒  ▒▓▒  ▒▓▒ 
 ░ ▒  ▒  ░ ░  ░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░  ░   ░  ░▒   ░▒   ░▒  
 ░ ░  ░    ░    ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░ ▒ ░   ░   ░ ░ ░ ░   ░  ░    ░    ░   
   ░       ░  ░ ░  ░  ░      ░  ░      ░   ░  ░  ░ ░           ░       ░   ░    ░    ░  
 ░                                                                         ░    ░    ░  
"""

for _ in range(100): print()

for i in logo.split("\n"):
    print(textUtil.printg(i, "#ff0000", "#0000ff"))
print("  [~] Wait till the magic is done...")

final = bruteforce(hash, salt)
if final == hash:
    print("  [~] Password not found :(")
if final != hash:
    print("  [~] Password found: "+final)
