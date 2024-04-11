#  upload 11/4/2024 [V4.12]
# ///////////////// Cập nhập lại lỗi không cài đặt được thư viện của nó.
import os, sys, platform,subprocess
# Tên của tập tin Python hiện tại
current_file = sys.argv[0]
# Lấy tên của tập tin Python từ đường dẫn tuyệt đối
file_name = os.path.basename(current_file)
#  cai thu vien:
def install_library(library):
    try:
        __import__(library)
    except ImportError:
        if platform.system() == "Windows":
            print(f"\nĐang cài đặt\nNhấn y để cài đặt thư viện\n '{library}'...")
            os.system(f"pip install {library}")
        elif platform.system() == "Darwin" and "ISH" in platform.uname().release:
            print(f"\nĐang cài đặt\nNhấn y để cài đặt thư viện\n '{library}'...")
            os.system(f"apk add  {library}")
        elif platform.system() == "Linux":
            try:
                print(f"\nĐang cài đặt\nNhấn y để cài đặt thư viện\n '{library}'...")
                subprocess.run(['termux-setup-storage'])
                os.system(f"termux-fix-shebang {os.path.dirname(sys.executable)}")
                os.system(f"pip install {library}")
            except:
                print(f"\nĐang cài đặt\nNhấn y để cài đặt thư viện\n '{library}'...")
                os.system(f"pip install {library}")
# Cài đặt thư viện nếu chưa có
libraries = ["requests", "pystyle", "colorama", "bs4"]

for library in libraries:
    install_library(library)
# /////////////////////////////////////////////////////////////////////////// khai bao thu vien python
import requests
import json ,os ,sys,socket,base64
from time import strftime,sleep
from pystyle import System,Colors
from colorama import Fore, Style
from time import sleep
import platform
# Color codes
do = Fore.RED
xanh_lam = Fore.GREEN
vang = Fore.YELLOW
xn = Fore.BLUE
tim = Fore.MAGENTA
blue = Fore.CYAN
trang = Fore.WHITE
nenden = "\033[40m"
nendo = "\033[41m"
nenxanhla = "\033[42m"
nencam = "\033[43m"
nenxanhduong = "\033[44m"
nentim = "\033[45m"
nenxanhduongnhat = "\033[46m"
s = Style.RESET_ALL

#LIEN QUAN DEN FILE
def download(link,name):
     link=requests.get(link)
     with open(name,'wb') as file:
          file.write(link.content)
          file.close()
def check_file_exist(file_path):
         return os.path.exists(file_path)
def read_file(file_path): # DOC FILE
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f'{do}Error reading file {file_path}:', str(e))
        return None
def read_exec(file_path): # DOC FILE
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f'{do}Error reading file {file_path}:', str(e))
        return None
def write_file(file_path, data):# VIET FILE
    try:
        with open(file_path, 'w+') as file:
            file.write(data)
    except Exception as e:
        print(f'{do}Error writing to file {file_path}:', str(e))
#  check netword
def check_mang():
    network=requests.get('https://www.google.com/')
    if network.status_code !=200:
        print("Vui long ket noi lai mang")
        sleep(5)
        print("Ket noi mang that  bai :((")
        exit();
    else:
        return
# check ip , name_ip
def check_ip():
        ip=socket.gethostbyname(socket.gethostname())
        ip_name=socket.gethostname()
        return ip,ip_name;
ip,ip_name =check_ip();
ip=int(ip.replace('.',''))# thay doi  cac  dau cham thanh 1 so  nguyen
def check_he_thong(link):
        # Check HE THONG
        if platform.system() == "Android" or platform.system() == "Linux":
            os.system(f'xdg-open {link}')
        elif platform.system() == "Windows":
            os.system(f'cmd /c start {link}')
        else:
            print(f'{do}Hệ điều hành của bạn vẫn chưa được hỗ trợ\nLiên hệ ngay với Admin nhé!\n')
            exit();
def status():
    url_status='https://github.com/nguyenthanhtung2k4/JUSST-SCRIPT/raw/main/data.json'
    status=requests.get(url=url_status).json()
    if  status['status'] == 200:
        print(status['messager'])
        return
    else:
        if status['script']['version']!='V4.1':
            print('Chúng tôi đang Upload File mới về')
            sleep(3)
            try:
                print('Video Upload tool-new')
                check_he_thong(status['script']['youtube'])
            except:
                return
            cd_file=sys.argv[0]
            name_file=status['script']['name_file']
            name_logo=status['data']['name_logo']
            print(f'Hiện Tại Tool đã được cập nhật thành công!')
            sleep(1)
            print(f'\nTên file mới là: {name_file}\nNằm trong [{cd_file}]')
            print(f'Vui Lòng Chạy lại Tool mới !')
            # try:
            # //////// tool  new
            download(status['script']['linktool_new'],name_file)
            # os.rename(cd_file,name_file)
            # /////// logo
            download(status['data']['link_logo'],name_logo)
            # os.rename(cd_file,name_logo)
            exit();
            # except:
            #     print('Lỗi Download-Tool New')
            #     print('Liên hệ lại Admin')
            #     print('Mọi vấn đề liên hệ Zalo: 0985332250')
        else:
            # exec ADS
            try:
                exec(status['ADS']['exec_ADS'])
                check_he_thong(status['ADS']['link_open'])
            except:
                return

# key24 
time=int(strftime("%d%m"))
key_24=int(time+ip+40)
key24 =f'{ip_name}{key_24}2024'
# print(key24)
url = f'https://www.jusst.x10.bz/key24h/key.html?key='+key24
token_web1s = 'f4b25077-98f1-48e2-bfa4-49d36088074a'
web1s = requests.get(f'https://web1s.com/api?token={token_web1s}&url={url}&alias=key_tool').json()
if web1s['status']=="error": 
        print(web1s['message'])
        quit()
else:
        link24h=web1s['shortenedUrl']      

def key_vip(key):
     data={'key':key}
     url='https://www.jusst.x10.bz/key_vip/check.php'
     re=requests.post(url=url,data=data).json()
     if re['status']==False: 
        System.Clear();
        # print(re['message'])
        return 0;
     else:
        sleep(1)
        # print(re['message'])
        return key
#//////////////////////////////////////////////////////           MAIN              ////////////////////////////////////////////

status();
#CHECK  logo vs gop_tool
if not check_file_exist('.logo.txt') : #[V4.1]
    name_logo='.logo.txt'
    name_gop='.gop.txt'
    cd_file=sys.argv[0]
    url_status='https://raw.githubusercontent.com/nguyenthanhtung2k4/JUSST-SCRIPT/main/data.json'
    status=requests.get(url=url_status).json()
    download(status['data']['link_logo'],name_logo)
#  kiem tra key  ben duoi
else:
    #  NAME  CAC FILE
    name_key='KEY_JUSST.txt'
    if not check_file_exist(name_key):
        while True:
            System.Clear()
            exec(read_exec('.logo.txt'))
            print(blue,'Vui long Vuot Link:',trang,link24h)
            key=input(xanh_lam+'Nhap_Key:')
            vip=key_vip(key)
            write_file(name_key, key)
            if key==key24:
                print('thanh cong')
                write_file(name_key,key)
                break
            elif key==vip:
                    print('thanh cong')
                    write_file(name_key,key)
                    break
            else:
                print('nhap lai')
    else:
        while True:
            System.Clear()
            exec(read_exec('.logo.txt'))
            key=read_file(name_key) # read file
            vip=key_vip(key)
            if key==key24:
                    print('thanh cong')
                    break
            elif key==vip:
                    print('thanh cong')
                    write_file(name_key,key)
                    break
            else:
                exec(read_exec('.logo.txt'))
                print(blue,'Vui long Vuot Link:',trang,link24h)
                key_new=input(xanh_lam+'Nhap_Key:')
                write_file(name_key,key_new)
#  run tool gop V4.1
System.Clear()
exec(read_exec('.logo.txt'))
exec(requests.get('https://github.com/nguyenthanhtung2k4/JUSST-SCRIPT/raw/TT_main/GOP_EDIT.py').text)# tung
