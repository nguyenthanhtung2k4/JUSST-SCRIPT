#  UPLOAD NGAY 30/3/2024
#  ///////////////////// NOI DUNG UPLOAD////////////////////////////////////////////
#  NÂNG CẤP LÊN   VISION 4.0
# ###################### Có thêm Tool  GOlike (Tikotk-tym vs follow)
# ###################### Có thêm Tool  GOlike (ig)
# ###################### Nôi dung thêm  phần Xem kênh youtube

from colorama import Fore,Style,Back
import re , os, sys,requests
from time import*
from pystyle import System
do="\033[1;31m"
xanh_lam="\033[1;32m"
vang="\033[1;33m"
xn="\033[1;34m"
tim="\033[1;35m"
blue="\033[1;36m"
trang="\033[1;97m"
nenden = "\033[40m"
nendo  = "\033[41m"
nenxanhla = "\033[42m"
nencam = "\033[43m"
nenxanhduong = "\033[44m"
nentim = "\033[45m"
nenxanhduongnhat = "\033[46m"
f=Style.RESET_ALL
den=Fore.BLACK
ngang=f'{do}=>'
System.Clear()
###########################
def read_exec(file_path): # DOC FILE
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f'{do}Error reading file {file_path}:', str(e))
        return None
###########################
TDS_Token="https://github.com/nguyenthanhtung2k4/AMDIN_JUSST/raw/main/TT_TDS_PROFILE_TOKEN"
### upload  file toool fb new 10/10/2023
TDS_FB_NEW='https://raw.githubusercontent.com/nguyenthanhtung2k4/AMDIN_JUSST/main/TT_TDS_FB%5BV3%5D'
TDS_FB_CU="https://github.com/nguyenthanhtung2k4/AMDIN_JUSST/raw/main/TT_TDS_FB_CA_NHAN_CU"
TDS_TIKTOK="https://github.com/nguyenthanhtung2k4/AMDIN_JUSST/raw/main/TT_TDS_TIKTOK_THUONG"
TDS_TIKTOK_NOW="https://github.com/nguyenthanhtung2k4/AMDIN_JUSST/raw/main/TT_TDS_TIKTOK_NOW"
### TINH NANG IG  LOAI BO  url6="https://run.mocky.io/v3/68a1f442-594b-4062-b475-e9f1016858a1"
GOLIKE_TIKTOK="https://github.com/nguyenthanhtung2k4/AMDIN_JUSST/raw/main/TT_GOLIKE.py"### them tinh nang 
GOLIKE_INSTAGRAM=""
# upload  tinh ngan  tiktok  view 
# LUA CHON  THU 8
VIEW_TIKTOK="https://raw.githubusercontent.com/nguyenthanhtung2k4/AMDIN_JUSST/main/TT_VIEW_TIKTOK"
###########################


###################################################### download file ve chay tiktok
bao_loi='''
                LỖI TẢI VỀ 
             :((     :((
XIN VUI LÒNG LIÊN HỆ VỚI ADMIN  ĐỂ ĐƯỢC HỖ TRỢ


          '''
def download(link_file,name):
          response = requests.get(link_file )
          if response.status_code == 200:
                with open(name, 'wb') as File:
                    File.write(response.content)
                    print(f'Tải về thành công: {name}')
          else:
                   ### BAO LOI  TOOL  TAI FILE VE
                print(f'Không thể tải về: {response.status_code}')
                System.Clear();
                print(bao_loi);
                exit();

################################################
tds=(f'''{trang}╔═════════════════════╗
║{vang}  Tool Trao Đổi Sub  {trang}║    
╚═════════════════════╝      
{ngang} {xanh_lam}Nhập Số {vang}[1] {xanh_lam}Tool TDS Profile{vang}[TOKEN]
----------------------------------------------
{ngang} {xanh_lam}Nhập Số {vang}[2] {xanh_lam}Tool {do}Upload{xanh_lam} TDS FB_New{vang}[v3]
{ngang} {xanh_lam}Nhập Số {vang}[3] {xanh_lam}Tool Phien Ban Cu TDS FB{vang}[v2]
----------------------------------------------
{ngang} {xanh_lam}Nhập Số {vang}[4] {xanh_lam}Tool TDS Tiktok{vang}[V0]
{ngang} {xanh_lam}Nhập Số {vang}[5] {xanh_lam}Tool TDS {vang}TIKTOK-NOW{vang}[V1]

{trang}╔═══════════════════════════════╗
║{vang}     Tool {tim}GOLIKE{trang} VS TIKTOK{trang}     ║    
╚═══════════════════════════════╝ 

{ngang} {xanh_lam}Nhập Số {vang}[6] {xanh_lam}Tool GOLIKE-TikTok{do} [New]
{ngang} {xanh_lam}Nhập Số {vang}[7] {xanh_lam}Tool GOLIKE-Insagram{do} [New]
{ngang} {xanh_lam}Nhập Số {vang}[8] {xanh_lam}Tool TikTok-View

{trang}╔══════════════════════╗
║{vang}     Tool - JUSST{trang}     ║    
╚══════════════════════╝ 
{ngang}{do}Download {xanh_lam}Tool CHECK PROXY
└────╼[ https://www.youtube.com/watch?v=lontD8W03rg ]
{ngang}{do}Watch {xanh_lam}Setup ISH(ios)
└────╼[ https://www.youtube.com/watch?v=2hhK3yrbEdQ ]
{ngang}{do}Download {xanh_lam}Tool Tạo 10k Page
└────╼[ https://www.youtube.com/watch?v=1kTziATAvDY ]

{f}''')
print(tds)

lua_chon=int(input(f'{vang}=>{trang}Nhập Số Chạy :')) 
################################################
try:     
    if lua_chon ==1 :
        print('')
        System.Clear()
        # logo
        read_exec('.logo.txt')
        exec(requests.get(url=TDS_Token).text)
    if lua_chon ==2 :
        print('')
        System.Clear()
        # logo
        read_exec('.logo.txt')
        exec(requests.get(url=TDS_FB_NEW).text)
    if lua_chon ==3 :
        print('')
        System.Clear()
        # logo
        read_exec('.logo.txt')
        exec(requests.get(url=TDS_FB_CU).text)
    if lua_chon ==4 :
        print('')
        System.Clear()
        # logo
        read_exec('.logo.txt')
        exec(requests.get(url=TDS_TIKTOK).text)
    if lua_chon ==5 :
        print('')
        System.Clear()
        # logo
        read_exec('.logo.txt')
        exec(requests.get(url=TDS_TIKTOK_NOW).text)
    if lua_chon ==6 :
        print('')
        System.Clear()
        # logo
        read_exec('.logo.txt')
        exec(requests.get(url=GOLIKE_TIKTOK).text)
    if lua_chon ==7 :
        print('')
        System.Clear()
        # logo
        read_exec('.logo.txt')
        exec(requests.get(url=GOLIKE_INSTAGRAM).text)
    
    if lua_chon==8:
            #  tiktok view
          print('Tool TikTok-View')
          System.Clear();
          
          ### kiem tra file co ton taiv hay khnog 
          # cac ten file
          name1='config.json'
          name2='devices.txt'
          name3='proxies.txt'
          link_file1='https://github.com/nguyenthanhtung2k4/AMDIN_JUSST/raw/main/config.json'
          link_file2='https://github.com/nguyenthanhtung2k4/AMDIN_JUSST/raw/main/devices.txt'
          link_file3='https://github.com/nguyenthanhtung2k4/AMDIN_JUSST/raw/main/proxies.txt'
          ktra1=os.path.isfile(name1)
          ktra2=os.path.isfile(name2)
          ktra3=os.path.isfile(name3)
          if(ktra1==True):
                   print("File ton tai")
          else:
                   download(link_file1,name1)
          if(ktra2==True):
                   print("File ton tai")
          else:
                   download(link_file2,name2)
          if(ktra3==True):
                   print("File ton tai")
          else:
                   download(link_file3,name3)
          ########################33 VAO TOOL TIKTOK VIEW 
          System.Clear()
          read_exec('.logo.txt')
          exec(requests.get(url=VIEW_TIKTOK).text)
    if lua_chon==9:
          System.Clear();
          print('UPLOAD')
          read_exec('.logo.txt')
          exit();
except:
    System.Clear();
    print(f'Chạy  lại {do}:((')
    print("Chạy lại không được liên hệ Admin ")
    print(f'{blue}Liên hệ: {do}https://www.jusst.x10.bz/{trang}')
    exit;
