import os, csv
import random
from qrcode import QRCode


from sty import fg
from pystyle import Write, Colors, Colorate



def checkFolder(path: str):
    if not os.path.exists(path):
        os.mkdir(path)

R = fg.red
RL = fg.li_red
RD = fg.da_red
G = fg.green
GL = fg.li_green
GD = fg.da_green
B = fg.blue
BL = fg.li_blue
BD = fg.da_blue
A = fg.grey
AL = fg.li_grey
AD = fg.da_grey
C = fg.cyan
CL = fg.li_cyan
CD = fg.da_cyan
Y = fg.yellow
YL = fg.li_yellow
YD = fg.da_yellow
M = fg.magenta
ML = fg.li_magenta
MD = fg.da_magenta
W = fg.white
N = fg.rs

info = f"{W}[{C}i{N+W}]{N}"
error = f"{W}[{R}!{N+W}]{N}"
success = f"{W}[{G}*{N+W}]{N}"
warn = f"{W}[{Y}•{N+W}]{N}"
asking = f"{W}[{C}>{N+W}]{N}"
plus = f"{G}[{W}+{N+G}]{N}"
minus = f"{R}[{W}-{N+R}]{N}"
yesno = f"{B}[{G}Y{B}/{R}N{B}]{N}"


def banner():
    banner = """
  ____  ___    ___________    .__          
  \   \/  / ___\__    ___/___ |  |   ____  
   \     / /    \|    |_/ __ \|  | _/ __ \ 
   /     \|   |  \    |\  ___/|  |_\  ___/ 
  /___/\  \___|  /____| \___  >____/\___  >
        \_/    \/           \/          \/ 
       
"""
    colors = [
        Colors.purple_to_blue, 
        Colors.green_to_cyan, Colors.cyan_to_green, 
        Colors.red_to_purple, Colors.purple_to_red,
        Colors.green_to_yellow, Colors.yellow_to_green,
        Colors.yellow_to_red, Colors.red_to_yellow
    ]
    print(Colorate.Vertical(random.choice(colors), f"{banner}", 1))
    # print(Colorate.Vertical(Colors.cyan_to_green, "          Telegram Advanced Tools         ",True))
    Write.Print(f"       Version: ", Colors.white, interval=0)
    Write.Print(f"7.0", Colors.red, interval=0)
    Write.Print(f" | ", Colors.gray, interval=0)
    Write.Print(f"Author: ", Colors.white, interval=0)
    Write.Print(f"Xnuv3r       \n\n", Colors.yellow, interval=0)

def print_title(teks:str):
    teks = teks.upper()
    return print(f"{Y}» {GL}{teks} {N}:")
    
def print_menu(nomor:int, teks:str, padding:bool=True):
    if nomor > 0:
        color = W if (nomor % 2 == 0) else CL
    else:
        color = RL

    if padding:
        return print(f"  {BL}[{AL}{nomor:02}{BL}] {color}{teks}{N}")
    else:
        return print(f"{BL}[{AL}{nomor:02}{BL}] {color}{teks}{N}")

def badge(teks,color=None):
    if color:
        return f"{AL}({color}{str(teks)}{AL}){N}"
    else:
        return f"{AL}({RL}{str(teks)}{AL}){N}"
    
def hapus():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def halaman_baru():
    hapus()
    banner()
    print(f"{A}="*44+f"{N}\n")

def kembali(text:str=None):
    if text:
        return input(f'\n{text}')
    return input(f'\n{C}Tekan {W}ENTER {C}untuk kembali...')

def keluar():
    halaman_baru()
    exit()

def readFile(filepath: str) -> list:
    data = []
    try:
        with open(filepath, "r", newline="") as readFile:
            header = csv.DictReader(readFile).fieldnames
            reader = csv.DictReader(readFile, header)
            for row in reader:
                data.append(row)
        readFile.close()
    except FileNotFoundError:
        pass
    return data

def writeFile(filepath: str, data: list):
    try:
        header = []
        dict = data[0]
        for key in dict.keys():
            header.append(key)
        
        with open(filepath, "w", newline="") as writeFile:
            writer = csv.DictWriter(writeFile, header)
            writer.writeheader()
            writer.writerows(data)
        writeFile.close()
    except IndexError:
        pass

def appendFile(filepath: str, data: list):
    old_data = readFile(filepath)
    for new_data in data:
        old_data.append(new_data)
    writeFile(filepath, old_data)

def updateData(filepath: str, nik: str, keys: str, value):
    old_data = readFile(filepath)
    new_data = []
    for data in old_data:
        NIK = data['nik']
        if NIK == nik:
            data[keys] = value
        new_data.append(data)
    writeFile(filepath,new_data)

def getData(filepath: str, phone: str):
    accounts = readFile(filepath)
    for account in accounts:
        try:
            PHONE = account['phone']
        except KeyError:
            PHONE = account['id']
            
        if PHONE == phone:
            return account
    return None

def setData(filepath: str, phone: str, new_dict: dict):
    old_data = readFile(filepath)
    new_data = []
    for data in old_data:
        PHONE = data['phone']
        if PHONE == phone:
            new_data.append(new_dict)
        else:
            new_data.append(data)
    writeFile(filepath,new_data)

def deleteData(filepath: str, value):
    lines = list()
    value = str(value)

    try:
        with open(filepath, "r", newline="") as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == value:
                        lines.remove(row)
        readFile.close()

        with open(filepath, "w", newline="") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        writeFile.close()
    except FileNotFoundError:
        pass

    if os.path.exists(filepath) and countData(filepath) == 0:
        os.remove(filepath)

def existData(filepath: str, value) -> bool:
    try:
        with open(filepath, "r", newline="") as readFile:
            reader = csv.reader(readFile, delimiter=",", lineterminator="\n")
            for row in reader:
                for field in row:
                    if field == str(value):
                        readFile.close()
                        return True
        readFile.close()
    except FileNotFoundError:
        pass
    return False

def countData(filepath: str) -> int:
    data = []
    try:
        with open(filepath, "r", newline="") as readFile:
            header = csv.DictReader(readFile).fieldnames
            reader = csv.DictReader(readFile, header)
            for row in reader:
                data.append(row)
        readFile.close()
    except FileNotFoundError:
        pass
    return len(data)


path_data = "data.csv"
qr = QRCode()

def display_url_as_qr(login_url):
    print(f'{info} Pindai Kode QR Berikut:')
    print()
    qr.clear()
    qr.add_data(login_url)
    qr.print_ascii(tty=False,invert=True)
    print()

while True:
    halaman_baru()
    print_menu(1,"Get Data None")
    print_menu(2,"Get Data Valid")
    print_menu(3,"Get Data Invalid")

    

    try:
        menu = int(input(f"\n{asking} Masukkan Menu Yang Dipilih: {Y}"))
    except ValueError:
        continue

    if menu == 0:
        halaman_baru()
        break

    elif menu == 1:
        halaman_baru()
        while True:
            data_regis = [x for x in readFile(path_data) if x['status'] == '-']
            if len(data_regis) == 0:
                print(f"{error} {R}Tidak Ada Data Yang Tersimpan")
                kembali()
                break
            data = random.choice(data_regis)
            while True:
                halaman_baru()
                display_url_as_qr(f"SMSTO:4444:{data['nik']}#{data['kk']}#")
                print(f"{info} NIK    : {data['nik']}")
                print(f"{info} KK     : {data['kk']}")
                print(f"{info} STATUS : {data['status']}")
                print()
                print_menu(1,"Next Data",False)
                print_menu(2,"Set Valid",False)
                print_menu(3,"Set Invalid",False)
                print_menu(4,"Set None",False)
                print_menu(0,"Exit",False)
                try:
                    sub_menu = int(input(f"\n{asking} Masukkan Menu Yang Dipilih: {Y}"))
                except ValueError:
                    continue
                
                if sub_menu == 0:
                    break

                elif sub_menu == 1:
                    break

                elif sub_menu == 2:
                    updateData(path_data, data['nik'], 'status', 'valid')
                    data['status'] = 'valid'
                    continue

                elif sub_menu == 3:
                    updateData(path_data, data['nik'], 'status', 'invalid')
                    data['status'] = 'invalid'
                    continue

                elif sub_menu == 4:
                    updateData(path_data, data['nik'], 'status', '-')
                    data['status'] = '-'
                    continue
            
            if sub_menu == 0:
                break
        
    elif menu == 2:
        halaman_baru()
        data_regis = readFile(path_data)
        for data in data_regis:
            print (f"{data['nik']:<8} {data['kk']:<15} {data['status']:<10}")

